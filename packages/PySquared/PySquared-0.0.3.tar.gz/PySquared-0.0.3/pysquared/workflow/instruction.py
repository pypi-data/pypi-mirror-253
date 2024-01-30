import copy

class InstructionInfo:
    """This thing allows access via attibutes (info.type = ...)

    Args:
        dict (_type_): _description_
    """
    def __init__(self, input={}):
        super().__setattr__('_data', input)

    def __getitem__(self, name):
        return self._data[name]
    
    def __setitem__(self, name, value):
        self._data[name] = value

    def __getattr__(self, name):
        return self._data[name]

    def __setattr__(self,name,value):
        self._data[name] = value

    def __contains__(self, name):
        return name in self._data

    def __getstate__(self):
        return copy.deepcopy(self._data)

    def __setstate__(self, new_data):
        super().__setattr__('_data', new_data)


class Instruction:
    def __init__(self, data: dict):
        self.info = InstructionInfo(data)
        self.finished = False

    def activate_dependents(self, stack) -> None:
        if 'activates' not in self.info:
            return

        for instruction_name in self.info.activates:
            activated = False
            for instruction in stack.instructions:
                if instruction_name == instruction.info.name:
                    assert not activated
                    assert self.info.name in instruction.info.activated_by
                    index = instruction.info.activated_by.index(self.info.name)
                    del instruction.info.activated_by[index]
                    stack.log.info(f"Stack {repr(self.info.name)}: Activated instruction '{instruction.info.name}'")
                    activated = True
            assert activated
            
    @property
    def is_subframe(self):
        return self.info.type == 'subframe'

    @property
    def is_active(self):
        return not self.finished and (not 'activated_by' in self.info or len(self.info.activated_by) == 0)
