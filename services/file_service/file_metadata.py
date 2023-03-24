import os
from datetime import datetime, timezone
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class FileMetaData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = None
        self.file_extension = None
        self.file_created_at = None
        self.file_last_modified_at = None
        self.file_size = None
        self.file_metadata = {}

    def get_file_name(self):
        return Path(self.file_path).stem

    def get_file_extension(self):
        return os.path.splitext(self.file_path)[1]

    def get_file_creation_time(self):
        timestamp_of_file_creation = os.stat(self.file_path).st_birthtime
        return datetime.fromtimestamp(timestamp_of_file_creation, tz=timezone.utc)

    def get_file_last_modification_time(self):
        timestamp_of_last_modification = os.path.getmtime(self.file_path)
        return datetime.fromtimestamp(timestamp_of_last_modification, tz=timezone.utc)

    def get_file_size(self):
        return os.path.getsize(self.file_path)

    def set_file_metadata(self):
        try:
            self.file_name = self.get_file_name()
            self.file_extension = self.get_file_extension()
            self.file_created_at = self.get_file_creation_time()
            self.file_last_modified_at = self.get_file_last_modification_time()
            self.file_size = self.get_file_size()
        except Exception as e:
            logger.error(f"ERROR | FILE_METADATA | ERROR_WHILE_GETTING_FILE_METADATA | EXCEPTION : {e}")

    def get_file_matadata(self):
        self.set_file_metadata()
        self.file_metadata["file_path"] = self.file_path
        self.file_metadata["file_name"] = self.file_name
        self.file_metadata["file_size"] = self.file_size
        self.file_metadata["file_extension"] = self.file_extension
        self.file_metadata["file_created_at"] = self.file_created_at.strftime("%d %B %Y %H:%M:%S")
        self.file_metadata["file_last_modified_at"] = self.file_last_modified_at.strftime("%d %B %Y %H:%M:%S")