import networkx as nx
import itertools
import inspect
import time

from chemscripts.mylogging import createLogger
from .accessgraph import AccessGraph
from .transform_concrete import TransformConcrete
from .transform_executor import TransformExecutor, TransformState, TransformResult
from ..transforms import Transform
from ..utils import get_logger_shortcuts
from ..workflow import InstructionFactories as instr
from ..workflow.stack import HandlerStatus

class Transformator:
    def __init__(self,
            storage,
            transformations=[],
            logger=None
        ):

        self.storage = storage
        self.logger = logger
        self.log = get_logger_shortcuts(logger)

        # Hack when lists/tuples are included
        new_transformations = []
        for x in transformations:
            if isinstance(x, tuple) or isinstance(x, list):
                for tr in x:
                    new_transformations.append(tr)
            else:
                new_transformations.append(x)
        transformations = new_transformations

        for t in transformations:
            assert t.NAME != Transform.DEFAULTS['NAME'], \
                f"Attempting to construct Transformator from untitled transformation '{t.__name__}'"
        self.transformations = {t.NAME: t for t in transformations}
        self.graph = nx.DiGraph()

        for tr_name, tr_obj in self.transformations.items():
            assert not self.graph.has_node(tr_name), f"Transform '{tr_name}' is already registered"
            for source in tr_obj.SOURCE_ITEMS:
                self.graph.add_edge(source, tr_name, transform=tr_obj)
                self.graph.nodes[source]['is_item'] = True
            for target in tr_obj.TARGET_ITEMS:
                self.graph.add_edge(tr_name, target, transform=tr_obj)
                self.graph.nodes[target]['is_item'] = True
            for item in tr_obj.NOTE_ITEMS:
                self.graph.add_node(item, is_item=True)
            self.graph.nodes[tr_name]['is_item'] = False
            self.graph.nodes[tr_name]['transform'] = tr_obj

        for item_node in self.graph.nodes:
            if not self.graph.nodes[item_node]['is_item']:
                continue
            
            assert item_node in self.storage, f"Unregistered item '{item_node}'"
            # assert self.graph.in_degree(item_node) + self.graph.out_degree(item_node) > 0, \
            #     f"Item '{item_node}' is not involved in any transforms"

            self.graph.nodes[item_node]['item'] = getattr(storage, item_node)
        
        for item_name, _ in self.storage:
            if not self.graph.has_node(item_name):
                self.log.error(f"Item '{item_name}' is not involved in any transforms")
            
    def _find_path_to(self, target_name: str) -> list:
        assert self.graph.has_node(target_name), f"Transform graph does not contain the target node '{target_name}'"

        # Isolate connected component containing the target
        active_graph = nx.Graph()
        active_graph.add_edges_from(self.graph.edges)
        active_graph.add_nodes_from(self.graph.nodes)
        for comp in nx.connected_components(active_graph):
            if target_name in comp:
                main_component_set = comp
                break
        
        ag = AccessGraph(self.graph, main_component_set, logger=self.logger)

        found_seqs = []
        starting_items = []
        for seq in ag.paths_iterate(target_name):
            found_seqs.append(seq)
            starting_items.append(ag.get_all_ends(seq))
            break
        
        assert len(found_seqs) != 0, f"No route to target '{target_name}' was found"
        assert not len(found_seqs) > 1, f"Several paths to the target '{target_name}' were found. {repr(found_seqs)}"

        found_seq = found_seqs[0]
        
        starting_items = starting_items[0]
        startitems_message = "Initial DataItems: " + ", ".join(starting_items)
        seq_message = "Sequence of transforms: " + " -> ".join(found_seq)
        self.log.info("\n\n{sep}\n{startitems_message}\n{seq_message}\n{sep}" \
            .format(
                startitems_message=startitems_message,
                seq_message=seq_message,
                sep=''.join(['-']*len(seq_message))
            )
        )
        return found_seq, starting_items
    
    def contains_dataitem(self, item_name: str) -> bool:
        return self.graph.has_node(item_name) and self.graph.nodes[item_name]['is_item']

    def plan_transformation(self,
            stack_frame,
            transformator_name: str,
            target: str,
            sources: list=None,
            forward: dict={}
        ) -> None:

        if sources is not None:
            raise NotImplementedError
        transform_path, start_items = self._find_path_to(target)

        # TODO Do some checks with startitems

        instructions = []
        for transform_name in transform_path:
            instruction = instr.prepare_transform(
                transformator=transformator_name,
                transform=transform_name,
                path=transform_path,
                forward=forward
            )
            instruction.info.activates = []
            instruction.info.activated_by = []
            instructions.append(instruction)
        for prev_tr, next_tr in zip(instructions, instructions[1:]):
            prev_tr.info.activates.append(next_tr.info.name)
            next_tr.info.activated_by.append(prev_tr.info.name)
        stack_frame.include_instructions(instructions)

    def prepare_transform(self,
            stack_frame,
            transformator_name: str,
            transform_name: str,
            transform_path: list,
            forward: dict={}
        ) -> None:

        transform_inst = TransformConcrete(
            transformator=self,
            transform_name=transform_name,
            logger=self.logger
        )
        transform_inst.prepare_instance(forward=forward)
        
        instructions = []
        for key_combination in transform_inst.get_key_combinations():
            # By default, entry point is the 'exec'-method for all transform
            instruction = instr.execute_transform(
                transformator=transformator_name,
                transform=transform_name,
                unmerged_keys=key_combination,
                forward=forward
            )
            instruction.info.activates = []
            instruction.info.activated_by = []
            instructions.append(instruction)
        
        stack_frame.include_instructions(instructions)
        stack_frame.info.transform_instance = transform_inst
    
    def execute_transform(self,
            stack_frame,
            instruction,
            transformator_name: str,
            transform_name: str,
            unmerged_keys: dict,
            forward: dict={}
        ) -> HandlerStatus:

        if 'keys_control' in forward and not forward['keys_control'](unmerged_keys):
            return HandlerStatus.DONE # Skip transform if user requested so
        
        if 'transform_executor' not in instruction.info:
            instruction.info.transform_executor = TransformExecutor(
                transform_instance=stack_frame.info.transform_instance,
                transformator_name=transformator_name,
                transform_name=transform_name,
                logger=self.logger
            )
        transform_executor = instruction.info.transform_executor

        result: TransformResult = transform_executor.execute(
            unmerged_keys=unmerged_keys,
            forward=forward,
        )

        if result == TransformResult.FINISHED or result == TransformResult.FAILED:
            return HandlerStatus.DONE
        elif result == TransformResult.REPEAT:
            return HandlerStatus.REPEAT
        elif result == TransformResult.LATER:
            return HandlerStatus.LATER
        else:
            raise ValueError(f"Cannot process transform result '{result}'")
