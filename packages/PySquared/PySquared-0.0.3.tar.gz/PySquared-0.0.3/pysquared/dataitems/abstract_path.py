import string
import glob
import os
import re
from pathlib import Path

from .decorators import register_dataitem
from .abstract_data import DataItem, ColumnType
from .keynames_layers import GroundKeynamingLayer, KeynamingLayer

from chemscripts.utils import str_to_type


@register_dataitem('path')
class PathItem(DataItem):
    PATH_KEY = '_pathitem_Path'
    def __init__(self,
            mask: str,
            wd: str = None,
            **kwargs
        ):
        """

        Args:
            mask (str): path mask of the form like '{keyA}_{keyB}.ext'.
            wd (str): directory where all FileItem files are stored.
            files (List[str], optional): restrictions to load only specific files
            key_requests (dict, optional): key restrictions for files loading.
            Cannot be provided together with `files` kwarg.
        """
        if 'additional_keys' not in kwargs:
            kwargs['additional_keys'] = {}
        kwargs['additional_keys'][self.PATH_KEY] = ColumnType.CONSTANT
        super().__init__(index_expectation=ColumnType.VARIABLE, **kwargs)

        self.mask, self.wd = self._obtain_paths(
            mask=mask,
            wd=wd,
        )

        self.modtime_control = {'column': self.PATH_KEY}

        self._key_mapping = GroundKeynamingLayer(keys=[key for key in self._keys_iter()])

    def _obtain_paths(self, mask=None, wd=None) -> tuple:
        assert mask is not None
        fixed_mask, mask_wd = self.storage.preprocess_mask(mask)

        if wd is not None:
            provided_wd = self.storage.preprocess_wd(wd)
        
        if wd is not None and mask_wd is not None:
            assert provided_wd == mask_wd, \
                "Mismatch of working directories extracted from mask and wd-kwarg: " \
                f"'{provided_wd}' vs. '{mask_wd}'"

        if mask_wd is not None:
            fixed_wd = mask_wd
        elif wd is not None: # Then, provided_wd is the preprocessed path
            fixed_wd = provided_wd
        else:
            fixed_wd = self.storage.propose_storage_directory(self.name)
        
        if fixed_mask != '.':
            fixed_mask = self.storage.preprocess_wd(os.path.join(fixed_wd, fixed_mask))
        return fixed_mask, fixed_wd

    def checkin(self) -> None:
        """Since this part of initialization requires interaction with `self.storage`
        it is executed a bit after the __init__ call
        """
        if self.wd != '.' or self.mask != '.': # if it is not '_internalitem_directories'
            create_diritem = self.wd != '.'

            self.storage._request_base_directory(
                self.wd,
                create_diritem=create_diritem,
                **self.storage_request
            )

    def _index_elements(self,
            required_elements: list = None,
            key_requests: dict = {}
        ):
        """Load existing files whose names are consistent with
        filename pattern (f-string `self.mask`).
        Record key values for each file.
        
        Args:
            files (List[str], optional): `files` kwarg can be passed to constrain
            parsing to specific files.
            key_requests (dict, optional): kwargs can be passed to constrain parsing
            to some specific key values.

        Raises:
            RuntimeError: on ambiguous/inappropriate filename patterns
        """
        # TODO Record modification time
        
        assert not (required_elements is not None and len(key_requests) > 0), \
            f"Cannot initialize FileItem '{self.name}' with both keys AND filenames specified: " \
            f"keys={repr(key_requests)}, paths={repr(required_elements)}"
            
        # Either include my filename mask or include all specified files
        if required_elements is None:
            # Use filename mask
            search_mask = self._get_wildcard_expression(**key_requests)
            include_elements = list(glob.glob(search_mask))
        else:
            include_elements = required_elements

            # Assert that all requested files exist
            all_files_exist = True
            for file in include_elements:
                if os.path.isfile(file):
                    all_files_exist = False
                    break
            if not all_files_exist:
                raise RuntimeError('Some of the requested files are missing:' + \
                    repr([file for file in include_elements if not os.path.isfile(file)]))

        for file in include_elements:
            try:
                keys = self._get_keyvalues(file)
            except IncompatiblePathError:
                continue

            super().include_element(
                keys={
                    self.PATH_KEY: file,
                    **keys
                }
            )
    
    def validate_path(self, path: str) -> bool:
        return os.path.isfile(path) or os.path.isdir(path)

    def _get_keyvalues(self, filename: str, assert_underscores=True) -> dict:
        """Obtain values of keys from provided filename
        by parsing using self.mask

        Args:
            filename (str): filename to be processed

        Raises:
            IncompatiblePathError: if some parsed key value contains '_' symbol
            usually this indicates that some file of different dataitem '{a}_{b}.ext'
            was parsed as '{c}.ext' which is incorrect

        Returns:
            dict: key-value pairs of a given filename
        """

        if len(list(self._keys_iter())) == 0:
            return {}

        filename = self.storage.preprocess_wd(filename)
        assert self.validate_path(self._postprocess_path(filename)), \
            f"Processed path '{filename}' is invalid for the item '{self.name}'. Make sure that path exists and check your masks"
        
        self.log.debug(f"Parsing key values from '{filename}'")

        # Regex for removing self.wd from name
        # wd_mask = os.path.join(self.wd, '*')
        # wd_regex = re.escape(wd_mask).replace(r"\*", "(.*)")

        # Regex for extracting keys
        pattern = self._get_wildcard_expression(absolute=False)
        regex = re.escape(pattern).replace(r"\*", "(.*)")

        # wd_matches = re.findall(wd_regex, filename)
        # assert len(wd_matches) != 0 and not(len(wd_matches) > 1), \
        #     f"Unable to extract working directory from '{filename}'"
        # pure_name = wd_matches[0]
        pure_name = filename

        assert '*' not in pure_name, "Found * symbol in the name of '{pure_name}'. Don't use it"
        matches = re.findall(regex, pure_name) # TODO Doesn't generate ALL possible matches :((
        assert len(matches) != 0, f"{pure_name} doesn't match the pattern '{pattern}'"
        assert not(len(matches) > 1), f"Several matches found for {pure_name} (has to be only 1). Pattern = '{pattern}'"
        match = matches[0]
        if isinstance(match, str):
            match = (match,)
        
        # Need to check that '_' isn't present in matched parts
        if assert_underscores:
            skip_file = False
            for value in match:
                if '_' in value:
                    self.log.info(f"File '{pure_name}' doesn't match the pattern for "
                            f"{self.name} (key contains '_')")
                    skip_file = True
            if skip_file:
                raise IncompatiblePathError(filename, pattern)
        
        key_value_pairs = {
            key: str_to_type(value)
            for key, value in zip(self._keys_iter(), match)
        }
        
        return key_value_pairs

    def access_element(self, **keys) -> str:
        """Access filename by its full set of keys

        Returns:
            Any: the retrieved filename

        Raises:
            AssertionError: on incomplete set of provided keys or multiple filenames matched
        """
        
        for key in keys.keys():
            assert key in self.public_keys, f"Key '{key}' is not present"
        keys = self._key_mapping.map_to_internal(keys)

        absolute_path = self._get_keys(**keys)[self.PATH_KEY]
        return self._postprocess_path(absolute_path, absolute=True)
        return relative_path

    def include_element(self, filename: str, assert_underscores=True, **keys_provided) -> None:
        """Index a new filename as an element of current FileItem

        Args:
            filename (str): name of the file to be included
        """

        for key in keys_provided.keys():
            assert key in self.public_keys, f"{key} not in {self.public_keys}"
        keys_provided = self._key_mapping.map_to_internal(keys_provided)

        if not self._conforms_keys_control(keys_provided):
            return

        filename = self.storage.preprocess_wd(filename)
        keys_determined = self._get_keyvalues(filename, assert_underscores=assert_underscores)

        if len(keys_provided) > 0:
            assert set(keys_provided.keys()) == set(keys_determined.keys()), \
                "Problem with provided keys: not all (or unexpected) keys were specified. " \
                f"Passed={list(keys_provided.keys())}, Expected={self._key_names}"
            
            assert keys_provided == keys_determined, \
                f"Problem with provided keys: mismatch between filename and provided keys " \
                f"Passed={repr(keys_provided)}, Expected={repr(keys_determined)}"
        
        super().include_element(
            keys={self.PATH_KEY: self._postprocess_path(filename), **keys_determined}
        )

    def get_restricted(self, keys: dict, **kwargs):
        """Get the restricted (filtered) version of the fileitem.
        It's very important to pass only the necessary files into transforms.
        Restricted version can be updated from inside transforms and
        then manually merged into the main fileitem.

        Args:
            keys (Dict[str, Any]): key values used for restriction

        Returns:
            FileItem: restricted version (detached from the `self` fileitem)
        """

        return super().get_restricted(keys,
            constructor_kwargs={
                'mask': self._get_mask(**keys),
                **kwargs
            }
        )

    def __iadd__(self, other):
        """Merge with another FileItem

        Args:
            other (FileItem): Usually, restricted version of FileItem
            produced by transform is merged into the main FileItem

        Returns:
            FileItem: updated main FileItem
        """
        
        # This only performs a few assertions
        super().__iadd__(other)

        for filename, keys in other:
            self.include_element(filename=filename, **keys, **other.restrictions)
        return self

    def _process_iteration(self, index, keys):
        return self._postprocess_path(keys[PathItem.PATH_KEY]), \
            {
                key: value
                for key, value in keys.items()
                if key != PathItem.PATH_KEY
            }

    def __iter__(self):
        pub_keys = self.public_keys
        return self._base_iter(
            call=lambda index, keys: (
                keys[PathItem.PATH_KEY],
                {
                    key: value
                    for key, value in self._key_mapping.map_to_external({
                        key: value
                        for key, value in keys.items()
                        if key != PathItem.PATH_KEY
                    }).items()
                    if key in pub_keys
                }
            )
        )
    
    def private_iterator(self):
        return self._base_iter()
        # return self._base_iter(
        #     call=lambda index, keys: self._process_iteration(index, keys)
        # )

    def get_path(self, **keys):
        assert set(self.public_keys) == set(keys.keys()), \
            "Mismatch between provided and expected keys: " \
            f"Provided={repr(list(keys.keys()))}, Expected={repr(self.public_keys)}"
        
        keys = self._key_mapping.map_to_internal(keys)

        if self.mask != '.':
            self.storage.verify_parent_directory(**self._restriction_request(key_restrictions=keys))

        return self._postprocess_path(self.mask.format(**keys))

    def _get_mask(self, **kwargs):
        """Get the mask of filename with some keys set to specified values.
        Pass kwargs to set some of the keys to specific values.

        Returns:
            str: the resulting filename mask
        """

        # General substitution of all keys to '*'
        subs = {
            key: '{%s}' % key
            for key in self._keys_iter()
        }
        
        # Replace some '*' with specified values
        for key, value in kwargs.items():
            subs[key] = value
        
        return self.mask.format(**subs)

    def _get_wildcard_expression(self, absolute=True, **kwargs):
        """Get the wildcard expression of filename by replacing all keys with '*' symbol.
        Pass kwargs to set some of the keys to specific values.

        Returns:
            str: the resulting filename mask
        """

        # General substitution of all keys to '*'
        subs = {
            key: '*'
            for key in self._keys_iter()
        }
        
        # Replace some '*' with specified values
        for key, value in kwargs.items():
            subs[key] = value

        if absolute:        
            return self._postprocess_path(self.mask.format(**subs))
        else:
            return self.mask.format(**subs)

    
    def _postprocess_path(self, filename: str, absolute: bool=False) -> str:
        # TODO This doesn't work when self.wd has '{stuff}'
        # assert Path(filename).is_relative_to(Path(self.wd))
        return self.storage.postprocess_path(filename, absolute=absolute)

    def containing_dir(self):
        return self.storage.get_containing_diritem(**self.storage_request)

    def cleanup(self) -> None:
        if self.restriction_id is None:
            self.storage.deallocate_directories(**self.storage_request)

        remove_elements = []
        for index, keys in self._base_iter():
            path = keys[PathItem.PATH_KEY]
            if not (os.path.isdir(path) or os.path.isfile(path)):
                remove_elements.append({'index': index, 'keys': keys})
        self.storage.remove_elements(remove_elements, **self.storage_request)

    @staticmethod
    def _keys_as_list(mask) -> list:
        return [
            t[1]
            for t in string.Formatter().parse(mask)
            if t[1] is not None
        ]

    def _keys_iter(self) -> str:
        """Lazy iterator over keys of the filename mask

        Yields:
            str: formatting elements of self.mask
        """

        for t in string.Formatter().parse(self.mask):
            if t[1] is not None:
                yield t[1]
    
    @property
    def _key_names(self) -> list:
        """Create a list of all keys of the current FileItem

        Returns:
            List[str]: resulting list
        """
        return [ key for key in self._keys_iter() ] + super()._key_names


class IncompatiblePathError(Exception):
    def __init__(self, path, mask):
        self.message = f"Path '{path}' does not match the mask '{mask}'"
        super().__init__(self.message)
