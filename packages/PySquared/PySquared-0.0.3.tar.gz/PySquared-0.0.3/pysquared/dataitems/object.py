import copy

from .decorators import register_dataitem
from .abstract_data import DataItem, ColumnType
from .keynames_layers import GroundKeynamingLayer, KeynamingLayer


@register_dataitem('object')
class ObjectItem(DataItem):
    def __init__(self, keys: list, **kwargs) -> None:
        super().__init__(index_expectation=ColumnType.VARIABLE, **kwargs)

        self.keys = keys
        self._key_mapping = GroundKeynamingLayer(keys=keys)

        self.objects = []

        self.modtime_control = 'manual'

    def include_element(self, object, **keys) -> None:
        """Include one object into `self`

        Args:
            object (Any): object to include
            **kwargs (str): values of all keys
        """

        for key in keys.keys():
            assert key in self.public_keys
        keys = self._key_mapping.map_to_internal(keys)

        if not self._conforms_keys_control(keys):
            return

        if self._is_null:
            self.objects = []
        
        if self.contains_keys(keys=keys):
            index = self._get_index(keys=keys)
            self.objects[index] = object
        else:
            index = len(self.objects)
            self.objects.append(object)

        super().include_element(index=index, keys=keys)
        
    def access_element(self, **keys):
        """Access object by its full set of keys

        Returns:
            Any: the retrieved object

        Raises:
            AssertionError: on incomplete set of provided keys or multiple objects matched
        """

        for key in keys.keys():
            assert key in self.public_keys
        keys = self._key_mapping.map_to_internal(keys)
        index = self._get_index(keys)
        return self.objects[index]

    def get_restricted(self, keys: dict, **kwargs):
        """Get the restricted (filtered) version of the ObjectItem.
        It's very important to pass only the necessary objects into transforms.
        Restricted version can be updated from inside transforms and then manually merged into the main ObjectItem.

        Args:
            keys (Dict[str, Any]): values of keys used for restriction

        Returns:
            ObjectItem: restricted version of ObjectItem.
            It is detached from the `self` ObjectItem, however, the objects themselves are not copied.
        """

        # This takes care of 99% of stuff
        restricted_item = super().get_restricted(keys,
            constructor_kwargs={
                # Pass to the constructor of new ObjectItem
                # a list of all keys that were not restricted
                'keys': [
                    key for key in self._key_names
                    if key not in keys
                ],
                **kwargs
            }
        )

        # On the ObjectItem level, we just need to load the objects into the new ObjectItem,
        # and assign a more natural indexing (0, 1, 2, etc.)
        indices = restricted_item._get_indices()
        index_mapping = {}
        for index in indices:
            new_index = len(restricted_item.objects)
            index_mapping[index] = new_index
            restricted_item.objects.append(self.objects[index])
        restricted_item._rename_indices(index_mapping)

        return restricted_item
    
    def __iadd__(self, other):
        """Merge with another ObjectItem

        Args:
            other (ObjectItem): Usually, restricted version of ObjectItem
            produced by transform is merged into the main ObjectItem

        Returns:
            ObjectItem: updated main ObjectItem
        """

        # This only performs a few assertions
        super().__iadd__(other)

        for keys, object in other.private_iterator():
            self.include_element(object=object, **keys)
        return self
    
    def restore_key_mapping(self) -> None:
        self._key_mapping = {
            keyname: keyname
            for keyname in self.keys
        }

    def __iter__(self):
        pub_keys = self.public_keys
        return self._base_iter(
            call=lambda index, keys: (
                self.objects[index],
                {
                    key: value
                    for key, value in self._key_mapping.map_to_external(keys).items()
                    if key in pub_keys
                }
            )
        )
    
    def private_iterator(self):
        return self._base_iter(
            call=lambda index, keys: (keys, self.objects[index])
        )

    def cleanup(self) -> None:
        # Delete all stored object refs
        self.objects = []

        # This will cleanup the table
        super().cleanup()

    def __contains__(self, item):
        return self.contains_keys(item['keys'])

    @property
    def _key_names(self):
        """Access the list of keys of this ObjectItem

        Returns:
            List[str]: List of keys
        """
        return copy.copy(self.keys) + super()._key_names
    
    @property
    def _is_null(self):
        return self.objects is None
