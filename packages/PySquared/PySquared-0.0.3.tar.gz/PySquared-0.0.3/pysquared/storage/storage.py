import os
import copy
import string
import fnmatch
import time
from pathlib import Path

import numpy as np
import pandas as pd
from ..dataitems import REGISTERED_DATAITEM_TYPES, ColumnType, PathItem
from ..utils import get_logger_shortcuts


class DataStorage:
    def __init__(self,
            item_list: list=None,
            logger=None, wd: str=None,
            instantiate_prototypes: bool=True,
            allow_overwrite: bool=False
        ) -> None:

        self.data = {}
        
        self.logger = logger
        self.log = get_logger_shortcuts(logger)
        
        self.additional_kwargs = {}
        if logger is not None:
            self.additional_kwargs['logger'] = logger
        self.additional_kwargs['allow_overwrite'] = allow_overwrite
        
        if wd is None:
            self.wd = os.path.abspath('.')
        else:
            self.wd = os.path.abspath(wd)
        self.log.info(f"Using '{self.wd}' as the base directory for the project")

        self._initialize_directories_item()
        self._initialize_modtimes_item()

        self.items_prototypes = copy.copy(item_list)
        self.instantiate_prototypes = instantiate_prototypes

        if item_list is not None and self.instantiate_prototypes:
            for item_name, item_attrs in item_list.items():
                if 'type' in item_attrs:
                    item_attrs['item_type'] = item_attrs['type']
                    del item_attrs['type']
                self.new_item(name=item_name, **item_attrs)
    
    def new_item(self, name: str, item_type: str, **kwargs) -> None:
        """Initialize a new DataItem to storage

        Args:
            name (str): Name of the new DataItem
            item_type (str): Type of the DataItem as recorded in REGISTERED_DATAITEM_TYPES
            **kwargs: everything that needs to be passed into constructor of the requeted type of DataItem
        """
        assert name not in self.data, f"Item '{name}' is already registered"

        assert item_type in REGISTERED_DATAITEM_TYPES, \
            f"DataItem type '{item_type}' is not registered " \
            f"(registered types are {repr(tuple(REGISTERED_DATAITEM_TYPES.keys()))})"
        
        pass_kwargs = {
            **kwargs,
            **{
                key: value
                for key, value in self.additional_kwargs.items()
                if key not in kwargs
            }
        }
        data_item = REGISTERED_DATAITEM_TYPES[item_type](name=name, storage=self, **pass_kwargs)

        assert hasattr(data_item, 'modtime_control')
        assert isinstance(data_item.modtime_control, dict) and \
                    len(data_item.modtime_control) == 1 and \
                    'column' in data_item.modtime_control or \
                data_item.modtime_control == 'manual'

        self.data[name] = {
            'name': name,
            'type': item_type,
            'item': data_item,
            'table': self._create_table(data_item._key_names),
            'modtime_control': data_item.modtime_control,
            'restrictions': {},
        }
        self.log.info(f"DataItem '{name}' of type '{item_type}' is registered successfully")

        # 1) Create DirectoriesItem that is stored at self.wd
        # 2) Include '.' as the only element
        # 3) FileItems in general, when checking-in first of all do a request for underlying wd to be created
        data_item.checkin()

        return data_item

    def _initialize_directories_item(self) -> None:
        self.new_item(
            name=self._internal('directories'),
            item_type='dirs',
            mask='.',
            wd='.',
            skip_autoindexing=True,
            additional_keys={
                self._internal('itemname'): ColumnType.UNIQUE,
                self._internal('dirobject'): ColumnType.CONSTANT,
            }
        )
        # print(repr(self.data[self._internal('directories')]['table']))

    def _initialize_modtimes_item(self) -> None:
        self.new_item(
            name=self._internal('modtimes'),
            item_type='object',
            keys=[],
            additional_keys={
                self._internal('itemname'): ColumnType.UNIQUE,
                self._internal('restriction_id'): ColumnType.UNIQUE,
                self._internal('element_index'): ColumnType.UNIQUE,
                self._internal('modtime'): ColumnType.VARIABLE,
            }
        )

    def new_restricted_item(self,
            name: str,
            key_restrictions: dict,
            restriction_id: int=None,
            constructor_kwargs={}
        ):
        """Initialize a new restriction of an existing DataItem

        Args:
            name (str): name of the base DataItem
            key_restrictions (dict): key restrictions to be imposed on the new DataItem
            restriction_id (int, optional): restriction ID in cases when
            a new restriction is created not from the main DataItem but from
            another restriction. Defaults to None.
            constructor_kwargs (dict, optional): will be passed to constructor of the new DataItem.
            Defaults to {}.

        Returns:
            DataItem or child: the created restriction
            (note that `checkin` method is not called)
        """

        assert restriction_id is None, 'Not implemented'

        # Get ID for new restriction
        new_restriction_id = 0
        for id in sorted(self.data[name]['restrictions'].keys()):
            if id == new_restriction_id:
                new_restriction_id += 1
            else:
                break
        
        item_type = self.data[name]['type']
        data_item = REGISTERED_DATAITEM_TYPES[item_type](
            name=name,
            storage=self,
            restrictions=copy.copy(key_restrictions),
            restriction_id=new_restriction_id,
            **constructor_kwargs,
        )

        self.data[name]['restrictions'][new_restriction_id] = {
            'name': name,
            'fixed_keys': data_item.restrictions,
            'item': data_item,

            # Keep the original rows that comply with restrictions. TODO Add kwarg to remove fixed columns
            'table': self._request_table(
                name=name,
                key_restrictions=key_restrictions,
                restriction_id=restriction_id,
            ).copy(),
        }
        return data_item

    def _create_table(self, keys: list) -> pd.DataFrame:
        """Prepare empty pandas df that will later be used to
        access/filter/include separate items by their values of keys.

        Args:
            keys (List[str]): key list of the DataItem being created

        Returns:
            pd.DataFrame
        """

        return pd.DataFrame(columns=keys)

    def _access_item_record(self,
            name: str,
            key_restrictions: dict,
            restriction_id: int = None,
            no_additional_restrictions: bool = False
        ) -> dict:
        """This method abstracts access to main record of DataItem and
        calls to access restricted DataItems

        Args:
            name (str): name of the dataitem
            key_restrictions (dict): key restrictions to be applied
            restriction_id (int, optional): ID of restricted item
            no_additional_restrictions (bool): enables additional assertion that no
            restrictions are present (except the base restrictions of restricted DataItems)

        Returns:
            dict: record in self.data. Either main record `self.data[name]` or
            record of a restriction `self.data[name]['restrictions'][restriction_id]`
        """

        assert name in self.data, f"DataItem with name '{name}' is not registered"

        if restriction_id is None:
            if no_additional_restrictions:
                assert len(key_restrictions) == 0, \
                    f"Unexpected restrictions are provided: {repr(key_restrictions)}"
                
            return self.data[name]
        else:
            assert restriction_id in self.data[name]['restrictions'], \
                f"Restrictions with ID={restriction_id} of DataItem '{name}' is not registered"

            item_record = self.data[name]['restrictions'][restriction_id]
            
            # TODO Check carefully!!!
            assert all(item in key_restrictions.items() for item in item_record['fixed_keys'].items()), \
                "Restrictions provided do not conform to base restrictions imposed on restricted DataItem " \
                f"({repr(item_record['fixed_keys'])} != {repr(key_restrictions)})"
            if no_additional_restrictions:
                assert key_restrictions == item_record['fixed_keys'], \
                    "Unexpected restrictions are provided " \
                    f"({repr(item_record['fixed_keys'])} != {repr(key_restrictions)})"
            
            return item_record

    @staticmethod
    def _get_available_index(df: pd.DataFrame) -> int:
        index = 0
        while index in df.index:
            index += 1
        return index

    def index_element(self, keys: dict, index=None, **request) -> None:
        """Add element to indexing table of requested DataItem

        Args:
            index (Any): index of the element of the dataitem
            keys (dict): values of keys for the new element
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted
        """

        item_record = self._access_item_record(**request)
        item = item_record['item']
        
        check_request = {
            key: value
            for key, value in request.items()
            if key != 'key_restrictions'
        }
        raw_restrictions = {**keys, **request['key_restrictions']}
        
        final_restrictions = {
            key: value
            for key, value in raw_restrictions.items()
            if key in item.public_keys or key in item.restrictions or \
                (key in item.additional_keys and item.additional_keys[key] == ColumnType.UNIQUE)
        }
        check_request['key_restrictions'] = final_restrictions

        short_df = self._request_table(**check_request)
        assert len(short_df) <= 1
        drop_item = len(short_df) == 1

        if drop_item: # Drop old item to overwrite with new index
            assert item_record['item'].allow_overwrite
            old_index = short_df.index[0]

            # Assertions for constant keys
            old_keys = short_df.loc[old_index].to_dict()
            old_const_keys = {
                key: value
                for key, value in old_keys.items()
                if key in item.additional_keys and item.additional_keys[key] == ColumnType.CONSTANT
            }

            for key, old_value in old_const_keys.items():
                assert raw_restrictions[key] == old_value

            # Assertion if index is constant
            if index is not None and item.index_expectation == ColumnType.CONSTANT:
                assert index == old_index

            # Remove the row that has to be overwritten
            item_record['table'].drop(old_index, inplace=True)
        
        if index is None:
            assert item.index_expectation != ColumnType.CONSTANT
            index = self._get_available_index(item_record['table'])
        
        item_record['table'].loc[index] = keys
        self.log.debug(f"Item {item_record['name']} indexed element {index} - {repr(keys)}")

        if request['name'] != self._internal('modtimes'):
            modtime_control = item_record['item'].modtime_control
            assert modtime_control is not None

            do_not_record = False
            if modtime_control == 'manual':
                modtime = time.time()
            elif isinstance(modtime_control, dict) and \
                        len(modtime_control) == 1 and \
                        'column' in modtime_control:
                pathname = keys[modtime_control['column']]
                if os.path.isdir(pathname) or os.path.isfile(pathname):
                    modtime = os.path.getmtime(pathname)
                else:
                    do_not_record = True
            else:
                raise Exception(f'Unexpected format of modtime_control: {modtime_control}')
            
            if not do_not_record:
                self.index_element(
                    {
                        self._internal('itemname'): request['name'],
                        self._internal('restriction_id'): request['restriction_id'] 
                            if request['restriction_id'] is not None else np.nan,
                        self._internal('element_index'): index,
                        self._internal('modtime'): modtime,
                    },
                    **self._get_modtimes_request()
                )
            
        
    def _request_table(self, index_restrictions: list=None, **request) -> pd.DataFrame:
        """Get table of elements for given request

        Args:
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted

        Returns:
            pd.DataFrame: the requested dataframe
        """

        item_record = self._access_item_record(**request)
        df = item_record['table']

        if index_restrictions is not None:
            df = df[df.index.isin(index_restrictions)]
        
        if len(request['key_restrictions']) == 0:
            return df
        else:
            restrictions = [
                df[key] == value
                for key, value in request['key_restrictions'].items()
            ]
            total_restriction = restrictions[0]
            for item in restrictions[1:]:
                total_restriction = total_restriction & item
            return df[total_restriction]

    def _assign_table(self, new_df: pd.DataFrame, **request) -> None:
        """Reassign table to some DataItem record.

        Args:
            new_df (pd.DataFrame): the new table (dataframe)
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted
        """

        item_record = self._access_item_record(**request, no_additional_restrictions=True)
        
        # Not doing any extensive checks of `new_df` since this method is not expected
        # to be called from outside of DataStorage
        item_record['table'] = new_df

    def unbind_restriction(self,
            name: str,
            key_restrictions: dict,
            restriction_id: int = None
        ) -> None:
        """Unregister a restriction

        Args:
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted

        Raises:
            RuntimeError: If unbinding of a non-restricted DataItem is requested
        """
        
        if restriction_id is None:
            raise RuntimeError('Cannot unbind DataItem that is not a restriction of another DataItem')
        
        # This is just to go over a few assertions impelemented in _access_item_record
        self._access_item_record(
            name=name,
            key_restrictions=key_restrictions,
            restriction_id=restriction_id,
            no_additional_restrictions=True
        )

        del self.data[name]['restrictions'][restriction_id]
        self.remove_elements(elements_data=[
                {'keys': {
                    self._internal('itemname'): name,
                    self._internal('restriction_id'): restriction_id,
                }}
            ],
            allow_multiple_rows=True,
            **self._get_modtimes_request()
        )

    def process_request(self,
            return_value: str = 'keys',
            expect_single_element: bool = False,
            **request
        ):
        """_summary_

        Args:
            return_value (str, optional): _description_. Defaults to 'keys'.
            expect_single_element (bool, optional): _description_. Defaults to False.

        Returns:
            dict of key-value pairs:
                when return_value=='keys' & expect_single_element
            
            value of the index:
                when return_value=='index' & expect_single_element
            
            (value of the index, dict of key-value pairs):
                when return_value=='keys&index' & expect_single_element

            list of dicts of key-value pairs:
                when return_value=='keys' & not expect_single_element
            
            list of index values:
                when return_value=='index' & not expect_single_element
                
            {index_value: {key-value pairs}}:
                when return_value=='keys&index' & not expect_single_element
        """
        

        df = self._request_table(**request)

        assert return_value in ('keys', 'index', 'keys&index')
        if expect_single_element:
            assert len(df) > 0, f"Element corresponding to request '{repr(request)}' not found"
            assert len(df) == 1, f"Multiple elements corresponding to request '{repr(request)}' were found"
        
            if return_value == 'keys':
                df_dict = df.to_dict(orient='index')
                index, keys = next(iter(df_dict.items()))
                return keys
            elif return_value == 'index':
                return df.index[0]
            else: # 'keys&index'
                df_dict = df.to_dict()
                return df_dict
        else:
            if return_value == 'keys':
                df_dict = df.to_dict(orient='records')
                return df_dict
            elif return_value == 'index':
                return df.index.to_list()
            else: # 'keys&index'
                df_dict = df.to_dict()
                return df_dict

    def rename_indices(self, index_mapping: dict, **request):
        """Rename indices of the table specified by **request.

        Args:
            index_mapping (dict): index mapping for renaming: keys=old_index, value=new_index
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted
        """

        df = self._request_table(**request)
        df = df.rename(index=index_mapping)
        self._assign_table(df, **request)

    def access_key_table(self, **request) -> pd.DataFrame:
        """Access a table that matches indices with values of all keys within current DataItem

        Returns:
            pd.DataFrame: dataframe (NOT a copy!) that stores indices, keys and they values
        """

        return self._access_item_record(
            **request,
            no_additional_restrictions=True
        )['table']

    def unique_keyvalues(self, keyname: str, /, **request) -> list:
        """Get unique values of some key within given DataItem

        Args:
            keyname (str): name of the key
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted

        Returns:
            list: list of unique values of the key
        """

        df = self._request_table(**request)
        return df[keyname].unique().tolist()

    def iter(self, **request):
        """Iterate over rows of a table correspoing to the requested DataItem

        Returns:
            Iterable: returning {'index': index, 'keys': dict of key-value pairs}
        """
        return ItemTableIterator(self, **request)

    def __iter__(self):
        return StoredItemsIterator(self)

    def check_item(self, **request) -> bool:
        """Check if given request specifies any existing element.
        Only complete sets of key values must be specified

        Args:
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted

        Returns:
            bool: if any element was found
        
        Raises:
            AssertionError: when incomplete set of keys was provided
        """
        df = self._request_table(**request)
        assert len(df) == 1 or len(df) == 0, \
            f"Unexpected length of df = {len(df)}"
        return len(df) == 1
    
    def contains_index(self, index, **request) -> bool:
        """Check if a row with given index is present in the table of requested DataItem

        Args:
            index (Any): index of interest
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted

        Returns:
            bool: if row with a given index was found
        """

        df = self._request_table(**request)
        return index in df.index
    
    def _get_dirs_request(self) -> dict:
        return {
            'name': self._internal('directories'),
            'key_restrictions': {},
            'restriction_id': None,
        }
    
    def _get_modtimes_request(self) -> dict:
        return {
            'name': self._internal('modtimes'),
            'key_restrictions': {},
            'restriction_id': None,
        }

    def _get_containing_diritem(self, path: str=None, itemname: str=None):
        assert path is not None or itemname is not None
        assert path is None or itemname is None

        dirs_request = self._get_dirs_request()
        if path is not None:
            dirs_request['key_restrictions'] = {
                self._internal('path'): path,
            }
        else:
            dirs_request['key_restrictions'] = {
                self._internal('itemname'): itemname,
            }

        found_items = self.process_request(return_value='keys', **dirs_request)

        if len(found_items) == 0:
            return None
        
        assert len(set((keys[self._internal('dirobject')] for keys in found_items))) == 1, \
            f"Multiple DirectoryItems describe the same path/itemname"
        dir_object = found_items[0][self._internal('dirobject')]
        return dir_object

    def _request_base_directory(self, dirname: str, create_diritem: bool=False, **request) -> None:
        if create_diritem:
            # Check if appropriate object is already registered
            dir_object = self._get_containing_diritem(path=dirname)

            if dir_object is None:
                # If no DirItems describing the requested dirname were found,
                # the create a new one
                diritem_name = self._internal('dirtemplate').format(itemname=request['name'])
                self.new_item(
                    name=diritem_name,
                    item_type='dirs',
                    mask=dirname,
                    **self.additional_kwargs
                )
                dir_object = diritem_name
        else:
            dir_object = self._internal('directories')

        self.index_element(
            {
                self._internal('path'): dirname,
                self._internal('itemname'): request['name'],
                self._internal('dirobject'): dir_object,
            },
            **self._get_dirs_request()
        )
    
    def number_of_elements(self, **request) -> int:
        """Get the number of elements within required DataItem

        Args:
            **request: `name` - the name of DataItem,
            `restriction_id`, optional - ID of the DataItem restriction if needed
            `key_restrictions`, optional - values of restricted keys if item is restricted

        Returns:
            int: number of elements
        """
        df = self._request_table(**request)
        return df.shape[0]

    def __contains__(self, item_name: str) -> bool:
        assert item_name not in DataStorage.INTERNALS['items'], \
            f"The item name '{item_name}' is protected"
        return item_name in self.data

    def __getattr__(self, item_name: str):
        """Allows to access items as `storage.item_name`

        Args:
            item_name (str): name of the DataItem

        Returns:
            DataItem or child: The object of DataItem or child class

        Raises:
            AssertionError: Name of nonregistered item or some unknown attrubute is provided
        """

        assert item_name in self.data, f"Item with name '{item_name}' is not registered"
        return self.data[item_name]['item']

    def propose_storage_directory(self, item_name: str) -> str:
        abspath = os.path.join(self.wd, f"{item_name}_data")
        relpath = self.preprocess_wd(abspath)
        return relpath

    def preprocess_wd(self, provided_wd: str) -> str:
        if provided_wd == '.':
            return '.'
        
        provided_wd = os.path.normpath(provided_wd)
        if os.path.isabs(provided_wd): # Absolute path
            assert Path(provided_wd).is_relative_to(Path(self.wd)), \
                f"PathItems must be stored inside '{self.wd}' which is the storage for project files"
        elif len(os.path.split(provided_wd)) > 1: # Relative path
            provided_wd = os.path.abspath(os.path.join(self.wd, provided_wd))
            # provided_wd = os.path.abspath(provided_wd)
            
        relpath = os.path.relpath(provided_wd, self.wd)
        if relpath != '.':
            relpath = os.path.join('.', relpath)
        return relpath

    def preprocess_mask(self, mask: str) -> tuple:
        if len(os.path.split(mask)[0]) > 0:
            mask_path = Path(mask)
            return mask_path.name, self.preprocess_wd(str(mask_path.parent))
        else:
            return mask, None

    def postprocess_path(self, provided_relpath: str, absolute: bool=False) -> str:
        if not absolute:
            assert not os.path.isabs(provided_relpath)
            return os.path.normpath(os.path.join(self.wd, provided_relpath))
        else:
            assert Path(provided_relpath).is_relative_to(Path(self.wd)), \
                f"Provided {provided_relpath} is not relative to {self.wd}"
            return provided_relpath

    def verify_parent_directory(self, name: str, **kwargs):
        diritem = self.get_containing_diritem(name=name)
        self.verify_directory(diritem=diritem, **kwargs)

    def verify_directory(self, diritem, key_restrictions: dict, **kwargs):
        diritem_name = diritem.name

        if diritem_name == self._internal('directories'):
            dir_keyvalues = {}
        else:
            dir_keyvalues = {
                key: value
                for key, value in key_restrictions.items()
                if key in diritem.public_keys
            }
        dirname = diritem.get_path(**dir_keyvalues)

        if not os.path.isdir(dirname):
            self.log.info(f"Creating directory '{dirname}'")
            os.mkdir(dirname)

            if diritem_name != self._internal('directories'):
                diritem.include_element(
                    filename=dirname,
                    **dir_keyvalues
                )
        else:
            self.log.debug(f"Directory '{dirname}' already exists")
    
    def get_containing_diritem(self, name: str, key_restrictions: dict={}, **kwargs):
        diritem_name = self._get_containing_diritem(itemname=name)
        assert diritem_name is not None, f"Cannot find DirItem containing the item '{name}'"
        
        res_item = self.data[diritem_name]['item']
        diritem_restriction = {
            key: value
            for key, value in key_restrictions.items()
            if key in res_item.public_keys
        }
        if len(diritem_restriction) == 0:
            return res_item
        else:
            return res_item.get_restricted(keys=diritem_restriction)

    @staticmethod
    def entry_extends(entry, test_entry):
        return all(
            key in test_entry and test_entry[key] == value
            for key, value in entry.items()
        )

    # This is the crucial logic of Transformators and has to be implemented elsewhere
    def key_combinations(self, items: list, nonmerged_keys: list) -> list:
        split_entries = {}
        for itemname in items:
            item = self.data[itemname]['item']
            kv_pairs = item.get_keyvalue_entries()
            split_entries[itemname] = [{
                    key: value
                    for key, value in kv_pair.items()
                    if key in nonmerged_keys
                }
                for kv_pair in kv_pairs
            ]

        # TODO Additional checks??
        
        united_entries = []
        for entries_sublist in split_entries.values():
            for entry in entries_sublist:
                if entry not in united_entries:
                    united_entries.append(entry)
        delete_entries = []
        for i, entry in enumerate(united_entries):
            for j, test_entry in enumerate(united_entries):
                if i != j and DataStorage.entry_extends(entry, test_entry):
                    delete_entries.append(i)
                    break
        united_entries = [
            entry
            for i, entry in enumerate(united_entries)
            if i not in delete_entries
        ]

        check_lengths = set(len(x) for x in united_entries)
        assert len(check_lengths) == 1, f"Inconsitencies in nonmerged key combinations:\n{repr(united_entries)}"
        return united_entries

    def clear_table(self, **request) -> None:
        df = self._request_table(**request)
        
        # Remove all rows from the table to clean it
        df.drop(df.index, inplace=True)

    def deallocate_directories(self, 
            name: str,
            key_restrictions: dict,
            restriction_id: int=None,
            **kwargs
        ) -> None:
        
        assert restriction_id is None, f"Cannot deallocate directories of restriced item '{name}'"
        
        diritem = self.get_containing_diritem(name=name)
        diritem_name = diritem.name
        
        if diritem_name != self._internal('directories'):
            diritem.cleanup()
    
    def remove_elements(self, elements_data, allow_multiple_rows: bool=False, **request) -> None:
        df = self._request_table(**request)

        remove_indices = []
        for element in elements_data:
            if 'index' in element and 'keys' in element:
                index = element['index']
                keys = element['keys']
                df_keys = df.loc[index].to_dict()
                assert df_keys == keys
                remove_indices.append(index)
            elif 'keys' in element:
                keys = element['keys']
                if len(keys) > 0:
                    restrictions = [
                        df[key] == value
                        for key, value in keys.items()
                    ]
                    total_restriction = restrictions[0]
                    for item in restrictions[1:]:
                        total_restriction = total_restriction & item
                    sub_df = df[total_restriction]
                else:
                    sub_df = df
                if not allow_multiple_rows:
                    assert len(sub_df) == 1
                    index = sub_df.index[0]
                    remove_indices.append(index)
                else:
                    remove_indices += sub_df.index.to_list()
            elif 'index' in element:
                remove_indices.append(index)
            else:
                raise RuntimeError
        df.drop(remove_indices, inplace=True)

    # TODO Implement file lookups

    @staticmethod
    def _internal_item(itemname: str) -> str:
        """To avoid conflicts between actual item names and
        internal item names using within DataStorage, we
        augment them with '_internalitem_' prefix.

        Args:
            itemname (str): meaningful name of internal item

        Returns:
            str: augmented name of internal item
        """
        return f'_internalitem_{itemname}'
    
    @staticmethod
    def _internal_key(keyname: str) -> str:
        """To avoid conflicts between actual key names and
        internal key names using within DataStorage, we
        augment them with '_internalkey_' prefix.

        Args:
            keyname (str): meaningful name of internal key

        Returns:
            str: augmented name of internal key
        """
        return f'_internalkey_{keyname}'

    def _internal(self, name: str) -> str:
        return self.INTERNALS_TOTAL[name]

    @staticmethod
    def _fstring_to_wildcard(fstring: str) -> str:
        subs = {
            t[1]: '*'
            for t in string.Formatter().parse(fstring)
            if t[1] is not None
        }
        return fstring.format(**subs)


DataStorage.INTERNALS = {
    'items': {
        'dirtemplate': DataStorage._internal_item('dirtemplate_{itemname}'),
        **{
            itemname: DataStorage._internal_item(itemname)
            for itemname in [
                # DirectoryItem: Index of all directories used to store FileItems and children, etc.
                'directories',
                'modtimes',
            ]
        }
    },
    'keys': {
        'path': PathItem.PATH_KEY,
        **{
            keyname: DataStorage._internal_key(keyname)
            for keyname in [
                # self-explanatory (for instance, 'directories' item stores wd's
                # of all items, thus, the need for 'itemname' key).
                # 'dirobject' is the DirectoryItem that handles self.wd of 'itemname'.
                'itemname',
                'dirobject',

                # For 'modtimes': 'itemname' again, and
                # 'element_index' - element of the item for which mod time is recorded
                # and 'modtime' itself
                'restriction_id',
                'element_index',
                'modtime',
            ]
        },
    },
}
DataStorage.INTERNALS_TOTAL = {
    key: value
    for internal_dict in DataStorage.INTERNALS.values()
    for key, value in internal_dict.items()
}


class ItemTableIterator:
    def __init__(self, base_instance, /, **request):
        df: pd.DataFrame = base_instance._request_table(**request)
        self.main_iter = df.iterrows()

    def __next__(self) -> dict:
        index, keys = next(self.main_iter)
        return {
            'index': index,
            'keys': keys.to_dict(),
        }


class StoredItemsIterator:
    def __init__(self, base_instance):
        self.main_iter = iter(base_instance.data.items())
        self.protected_items = [
            base_instance._fstring_to_wildcard(itename_mask)
            for itename_mask in base_instance.INTERNALS['items'].values()
        ]

    @staticmethod
    def contains_wildcard(value, mask_container):
        return any(
            fnmatch.fnmatch(value, current_mask)
            for current_mask in mask_container
        )

    def __next__(self) -> dict:
        item_name, keys = next(self.main_iter)
        while self.contains_wildcard(item_name, self.protected_items):
            item_name, keys = next(self.main_iter)
        return (item_name, keys['item'])
