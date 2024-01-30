import os

from .decorators import register_dataitem
from .abstract_path import PathItem

from chemscripts.utils import str_to_type


@register_dataitem('dirs')
class DirectoryItem(PathItem):
    def __init__(self,
            directories: list = None,
            key_requests: dict = {},
            skip_autoindexing: bool = False,
            **kwargs
        ):
        """

        Args:
            mask (str): filename mask of the form like '{keyA}_{keyB}.ext'.
            wd (str): directory where all FileItem files are stored.
            files (List[str], optional): restrictions to load only specific files
            key_requests (dict, optional): key restrictions for files loading.
            Cannot be provided together with `files` kwarg.
        """
        super().__init__(**kwargs)

        # Will be used to finish initialization in the `checkin` method
        self.checkin_kwargs = {
            'directories': directories,
            'key_requests': key_requests,
            'skip_autoindexing': skip_autoindexing,
        }

    def checkin(self) -> None:
        """Since this part of initialization requires interaction with `self.storage`
        it is executed a bit after the __init__ call
        """
        super().checkin()
        
        if not self.checkin_kwargs['skip_autoindexing']:
            self._index_elements(
                key_requests=self.checkin_kwargs['key_requests'],
                required_elements=self.checkin_kwargs['directories'],
            )

    def ensure_directory(self, **keys):
        # This will perform some basic checks of **keys
        self.get_path(**keys)

        # Create directory if it doesn't exist already
        self.storage.verify_directory(diritem=self, **self._restriction_request(key_restrictions=keys))
        
    def cleanup(self) -> None:
        for dirname, keys in self:
            assert os.path.isdir(dirname), f'{dirname} not a directory'
            if len(os.listdir(dirname)) == 0:
                os.rmdir(dirname)
        
        # This will remove the table elements corresponding to non-existing paths
        super().cleanup()
    
    def deallocate_directory(self, dirname):
        assert dirname in self
    
    def validate_path(self, path: str) -> bool:
        return os.path.isdir(path)

