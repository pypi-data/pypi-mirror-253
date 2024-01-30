import string
import glob
import os
import re

from .decorators import register_dataitem
from .abstract_path import PathItem

from chemscripts.utils import str_to_type


@register_dataitem('file')
class FileItem(PathItem):
    def __init__(self,
            files: list = None,
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
            'files': files,
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
                required_elements=self.checkin_kwargs['files'],
            )

    def cleanup(self) -> None:
        if self.restriction_id is None:
            # If this is not a restricted version,
            # files will be deleted on cleanup call
            for filename, _ in self:
                self.log.info(f"Removing '{filename}'")
                os.remove(filename)

        # This will remove the table elements corresponding to non-existing paths
        super().cleanup()

    def validate_path(self, path: str) -> bool:
        return os.path.isfile(path)
