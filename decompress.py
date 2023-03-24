from services.compression_core.encoding_and_decoding import EncodeDecode
from services.compression_core.padding import Padding

class Decompress:
    def __init__(self, file_content):
        self.file_content = file_content

    def decompress(self):
        file_content, encoded_dictionary = Padding(self.file_content).remove_padding()
        decoded_dictionary = EncodeDecode(file_content, encoded_dictionary).decode_dictionary()
        decoded_data = EncodeDecode(file_content, decoded_dictionary).decode()
        return decoded_data