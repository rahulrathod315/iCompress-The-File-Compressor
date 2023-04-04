from compress import Compress
from decompress import Decompress
from services.file_service.file_write import FileWrite

class TextCompression:
    def __init__(self, file_path, binary_file_path):
        self.file_path = file_path
        self.binary_file_path = binary_file_path

    def compress(self):
        binary_string = Compress(self.file_path).compress()
        FileWrite(self.binary_file_path, binary_string).convert_to_bytes_and_write()

    def decompress(self):
        binary_string = FileWrite(self.binary_file_path).convert_to_binary_string_from_bytes()
        text_file_content = Decompress(binary_string).decompress()
        FileWrite(self.file_path, text_file_content).write_text_data_to_file()