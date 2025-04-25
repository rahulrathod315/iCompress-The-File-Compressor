import logging

logger = logging.getLogger(__name__)


class FileWrite:
    def __init__(self, file_path, content=None):
        self.file_content = content
        self.file_path = file_path

    def open_binary_file_in_write_mode(self):
        try:
            self.file = open(self.file_path, "wb")
        except Exception as e:
            logger.error(f"ERROR | FILE_WRITE | ERROR_WHILE_OPENING_FILE_IN_BINARY_WRITE_MODE | FILE : {self.file_path}")
            raise Exception("Sorry, Can't open File.")

    def open_binary_file_in_read_mode(self):
        try:
            self.file = open(self.file_path, "rb")
        except Exception as e:
            logger.error(f"ERROR | FILE_WRITE | ERROR_WHILE_OPENING_FILE_IN_BINARY_READ_MODE | FILE : {self.file_path}")
            raise Exception("Sorry, Can't open File.")

    def open_text_file_in_write_mode(self):
        try:
            self.file = open(self.file_path, "w")
        except Exception as e:
            logger.error(f"ERROR | FILE_WRITE | ERROR_WHILE_OPENING_FILE_IN_WRITE_MODE | FILE : {self.file_path}")
            raise Exception("Sorry, Can't open File.")

    def convert_binary_string_to_bytes(self):
        return int(self.file_content, 2).to_bytes((len(self.file_content) + 7) // 8, byteorder='big')

    def write_to_file(self, data):
        try:
            self.file.write(data)
        except Exception as e:
            logger.error(f"ERROR | FILE_WRITE | ERROR_WHILE_WRITING_FILE | FILE : {self.file_path}")
            raise Exception("Error while writing to file")
    
    def convert_to_bytes_and_write(self):
        self.open_binary_file_in_write_mode()
        bytes_data = self.convert_binary_string_to_bytes()
        self.write_to_file(bytes_data)

    def convert_to_binary_string_from_bytes(self):
        self.open_binary_file_in_read_mode()
        self.file_content = self.file.read()
        return bin(int.from_bytes(self.file_content, byteorder='big'))[2:]

    def write_text_data_to_file(self):
        self.open_text_file_in_write_mode()
        self.write_to_file(self.file_content)
        