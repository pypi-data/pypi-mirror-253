import copy
import pandas as pd

from .decorators import register_dataitem    
from ..utils import get_logger_shortcuts
from .keynames_layers import GroundKeynamingLayer, KeynamingLayer

from enum import Enum

class ColumnType(Enum):
    # Same value set of UNIQUE keys implies overwriting
    # Example: all keys that are defined by outside user,
    # or itemnames within internal 'dirs' and 'modtimes' tables
    UNIQUE = 1

    # This one is constant for given set of UNIQUE keys
    # Implies the corresponding assertions when overwriting
    # Example: Paths of PathItems, 'dirobject' in 'dirs' table
    CONSTANT = 2

    # Is not required to be constant for given set of UNIQUE keys
    # Example: 'modtime' or all currently used index columns
    VARIABLE = 3

@register_dataitem('None')
class DataItem:
    """
    This is an abstract class, parent for all DataItems.
    However, this is not always an abstract class - it can be used as 'None' dataitem
    It's basic properties are:
    (1) It is always known/discovered/computed
    (2) It has no keys

    TODO WHAT ABOUT DataItems with no keys and one element?
    """

    def __init__(self,
            name: str,
            storage,
            index_expectation: ColumnType,
            restrictions: dict = {},
            restriction_id: int = None,
            additional_keys: dict = {},
            logger=None,
            allow_overwrite: bool = False,
            keys_control = None,
            **kwargs):
        
        assert len(kwargs) == 0, f"DataItem {name} recieved some unprocessed " \
            f"kwargs={repr(tuple(key for key in kwargs.keys()))}"

        self.name = name
        self.storage = storage
        self.restrictions = restrictions
        self.restriction_id = restriction_id

        self.logger = logger
        self.log = get_logger_shortcuts(logger)
        self.allow_overwrite = allow_overwrite
        self.keys_control = keys_control

        self.constructor_kwargs = {}
        if logger is not None:
            self.constructor_kwargs['logger'] = logger
        self.constructor_kwargs['allow_overwrite'] = allow_overwrite
        
        assert isinstance(additional_keys, dict)
        self.additional_keys = additional_keys
        self.index_expectation = index_expectation
        assert self.index_expectation is not ColumnType.UNIQUE # Either CONSTANT or VARIABLE are supported
        
        # Main storage request is used to access the main table of the DataItem even if `self` is restricted
        self.main_storage_request = {
            'name': self.name,
        }
        # Basic storage request is used to access the table of the restriced DataItem if appropriate
        self.storage_request = {
            'name': self.name,
            'key_restrictions': self.restrictions,
        }
        # if self.restriction_id is not None:
        self.storage_request['restriction_id'] = self.restriction_id

        self.log.debug(f"Initialized {self.name}")

    def _restriction_request(self, key_restrictions: dict) -> dict:
        """Get a request to storage object that includes additional restrictions

        Args:
            key_restrictions (dict): additional restrictions

        Returns:
            dict: updated request to storage object
        """

        for key, value in key_restrictions.items():
            if key in self.restrictions:
                assert value == self.restrictions[key], \
                    f"Provided keys conflict with restricted keys of currect DataItem: " \
                    f"{repr(key_restrictions)} vs. {repr(self.restrictions)}"
                
        request = copy.copy(self.storage_request)
        request['key_restrictions'] = {
            **key_restrictions,
            **request['key_restrictions']
        }
        return request

    def include_element(self, keys: dict, index = None) -> None:
        """Store new index with its corresponding values of keys.
        This should be called only from child methods

        Args:
            index (Any): index of the new element
            keys (dict): values of all keys
        """

        assert set(keys.keys()) == set(self._key_names), \
            "Passed key names disagree with existing keys of this DataItem. " \
            f"Passed={list(keys.keys())}, Expected={self._key_names}"
        
        for key, value in keys.items():
            if key in self.restrictions:
                assert value == self.restrictions[key], \
                    f"Provided keys conflict with restricted keys of currect DataItem: " \
                    f"{repr(keys)} vs. {repr(self.restrictions)}"
        keys = {
            **keys,
            **{
                key: value
                for key, value in self.restrictions.items()
            }
        }
        self.storage.index_element(index=index, keys=keys, **self.storage_request)

    def _get_index(self, keys: dict):
        """Get index within storage table by values of keys

        Args:
            keys (dict): values of all keys

        Returns:
            Any: the retrieved object

        Raises:
            AssertionError: on incomplete set of provided keys or multiple objects matched
        """

        assert self.non_empty, \
            f"Container {self.name} is empty, can not get object. Restrictions = {repr(self.restrictions)}"

        assert set(keys.keys()) == set(self.public_keys), \
            f'Not all keys were specified. Passed={list(keys.keys())}, Expected={self.public_keys}'
        
        return self.storage.process_request(
            return_value='index',
            expect_single_element=True,
            **self._restriction_request(keys)
        )

    def _get_indices(self) -> list:
        """Assemble a list of indices of all elements

        Returns:
            list: the resulting list
        """
        return self.storage.process_request(
            return_value='index',
            **self.storage_request
        )

    def _get_keys(self, index=None, **keys) -> dict:
        """Get keys of some item element by its index

        Args:
            index (Any): index of the element

        Returns:
            dict: dict of all keys and values
        """
        
        return self.storage.process_request(
            return_value='keys',
            index_restrictions=([index] if index is not None else None),
            expect_single_element=True,
            **self._restriction_request(key_restrictions=keys)
        )

    def _conforms_keys_control(self, keys: dict) -> bool:
        return self.keys_control is None or self.keys_control(keys)

    def get_restricted(self, keys: dict, constructor_kwargs: dict={}):
        """Build restriction of current DataItem. This does not copy
        any data besides the table of assignments index <-> key values

        Args:
            keys (dict): values of keys used for restriction
            constructor_kwargs (dict): keywords provided by child method `get_restricted`
            that are specific for the exact DataItem being created
            (i.e. cannot be provided via `self.constructor_kwargs`)

        Returns:
            DataItem: the new restricted version of the `self` DataItem that
            has already been registered in the storage and assigned self.restriction_id
        """

        assert self._key_mapping.is_ground

        return self.storage.new_restricted_item(
            **self._restriction_request(keys),
            constructor_kwargs={
                # Passes stuff like self.logger
                **self.constructor_kwargs,

                # Passes what child method `self.get_restricted` has specifically requested
                # like self.keys, self.filename_mask, etc.
                **constructor_kwargs,
            }
        )

    def _rename_indices(self, index_mapping: dict) -> None:
        """Rename indices using `index_mapping`

        Args:
            index_mapping (dict): provided index mapping: keys=old_indices, values=new_indices
        """
        self.storage.rename_indices(index_mapping, **self.storage_request)

    def __iadd__(self, other) -> None:
        """This just implements a few assertions that are
        universal for all DataItem childred. The core expectation
        is that `other` must be a restriction of `self`. The process of
        concatenation must be implemented within children classes
        using pattern like this:
        ```
        super().__iadd__(other)
        for index, keys, some_data in other:
            self.include_element(index=index, keys=keys, some_data=some_data)
        ```

        Args:
            other (DataItem child): other DataItem - a restriction of `self`
            containing some new elements that must be included into `self`.
            Most likely, the `other` object will soon be removed via `other.retire()`
        """

        assert self.name == other.name, \
            f"Merging FileItems with different names: FileItem({repr(self.name)}) += FileItem({repr(other.name)})"
        
        assert self._key_mapping.is_ground # No keys are currently renamed

        if not self.allow_overwrite:
            for index, keys in other._base_iter():
                assert not self.contains_keys(keys), \
                    f"Main DataItem already contains element with {repr(keys)}"

    def contains_keys(self, keys: dict) -> bool:
        """Check if given set of keys specifies any element
        in the DataItem's table.

        Args:
            keys (dict): values of ALL keys of this DataItem

        Returns:
            bool: True (exactly one element found),
            False (no elements found), AssertionError otherwise
        """
        
        assert set(keys.keys()) == set(self._key_names), \
            "Passed key names disagree with existing keys of this DataItem. " \
            f"Passed={list(keys.keys())}, Expected={self._key_names}"
        return self.storage.check_item(**self._restriction_request(keys))

    def contains_index(self, index) -> bool:
        """Check if a row with given index is present in this DataItem

        Args:
            index (Any): index of interest

        Returns:
            bool: True (found element with `index`), False (didn't find an element)
        """
        return self.storage.contains_index(index, **self.storage_request)

    def retire(self) -> None:
        """All restrictions of DataItems are meant to have limited lifetime, so
        at some point they are unbound from the storage in order to be garbage collected
        """
        
        assert self.restriction_id is not None, \
            f"Attempting to remove DataItem that is not a restriction"
        self.storage.unbind_restriction(**self.storage_request)

    def access_key_table(self) -> pd.DataFrame:
        """Access a table that matches indices with values of all keys within current DataItem

        Returns:
            pd.DataFrame: dataframe (NOT a copy!) that stores indices, keys and they values
        """
        
        return self.storage.access_key_table(**self.storage_request)

    def __len__(self) -> int:
        return len(self.access_key_table())

    def get_values_of_key(self, keyname: str) -> list:
        """Summarize all values that a given key has within this DataItem

        Args:
            keyname (str): the key to summarize

        Returns:
            List[str]: list of all existing values of this key
        
        Raises:
            AssertionError: when incorrect key name is provided
        """

        assert keyname in self._key_names, f'Incorrect key {keyname} was provided'
        return self.storage.unique_keyvalues(keyname, **self.storage_request)

    def get_keyvalue_entries(self) -> list:
        pub_keys = self.public_keys
        return [
            {
                key: value
                for key, value in keys.items()
                if key in pub_keys
            }
            for index, keys in self._base_iter()
        ]

    def cleanup(self) -> None:
        self.storage.clear_table(**self.storage_request)

    def _base_iter(self, **settings):
        """This iterator factory is meant to be used within
        all DataItem child classes 

        Returns:
            DataItemIterator: iterator that exposes indices, key-value pairs
            of elements and custom data supplied from child classes
        """
        return DataItemIterator(self, request=self.storage_request, **settings)

    def __iter__(self):
        raise RuntimeError("Cannot iterate over DataItems"
                           "(use a child class like ObjectItems or FileItems)")

    def checkin(self) -> None:
        """Placeholder of a method that will be overloaded in DataItem children
        that need to interact with self.storage to finish initialization (e.g. FileItem)
        """
        pass

    def with_renamed_keys(self, all_keys_mapping: dict):
        new_keys_mapping = {
            keyname: 
                all_keys_mapping[keyname] if keyname in all_keys_mapping
                else keyname
            for keyname in self.public_keys
        }
        self._key_mapping = KeynamingLayer(
            key_mapping=new_keys_mapping,
            base=self._key_mapping
        )
        return self

    def release_keyname_layer(self) -> None:
        self._key_mapping = self._key_mapping.get_base()

    def __len__(self) -> int:
        return self.storage.number_of_elements(**self.storage_request)

    @property
    def public_keys(self) -> list:
        return self._key_mapping.get_public_keys()

    @property
    def _key_names(self) -> list:
        return list(self.additional_keys.keys())

    @property
    def is_empty(self):
        return len(self) == 0
    
    @property
    def non_empty(self):
        return len(self) > 0


class DataItemIterator:
    def __init__(self,
            base_instance,
            request: dict,
            call=None
        ):
        """Initializes iterator that is inteded to be used for
        all child classes of DataItem 

        Args:
            base_instance (DataItem or child): instance to iterate over
            request (dict): request to self.storage
            calls (None/Callable/Dict, optional): allows to customize
            the third element of the tuple for various children of DataItem.
            Can be a function that returns whatever must be put at the third place, or
            a dict of functions - then there is a dict at the third place
            (key=key of self.calls, value=output of self.calls[key]).
            These custom callables must take {'index': index, 'keys': keys} as the only arg.
        """
        
        self.storage_iter = base_instance.storage.iter(**request)

        assert call is None or callable(call)
        self.call = call

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        """On each iteration it returns a tuple of two or three element

        Returns:
            tuple: (index: Any, keys: Dict, additional_output: depends on self.calls)
        """
        next_dict = next(self.storage_iter)

        iteration_raw = (next_dict['index'], next_dict['keys'])
        if self.call is None:
            return iteration_raw
        else:
            return self.call(*iteration_raw)
