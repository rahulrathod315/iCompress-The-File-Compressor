import logging

from .services.compression_core.frequency import AlphabetFrequency
from .services.compression_core.frequency_tree import FrequencyTree
from .services.compression_core.prepare_dictionary import PrepareDictionary
from .services.compression_core.encoding_and_decoding import EncodeDecode
from .services.compression_core.padding import Padding

logger = logging.getLogger(__name__)

def get_file_content(file):
    try:
        return open(file, 'r').read().strip()
    except Exception as e:
        logger.error(f"ERROR | FREQUENCY | ERROR_WHILE_OPENING_FILE | EXCEPTION : {e}")

class Compress:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = get_file_content(self.file_path)

    def compress(self):
        frequency = AlphabetFrequency(self.file_content).get_alphabet_frequency_in_file()
        frequency_tree = FrequencyTree(frequency).build_tree()
        dictionary = PrepareDictionary(frequency_tree).get_dictionary()
        encoded_data = EncodeDecode(self.file_content, dictionary).encode()
        padded_data = Padding(encoded_data).add_padding()
        encoded_dictionary = EncodeDecode(self.file_content, dictionary).encode_dictionary()
        bits = padded_data + encoded_dictionary
        return bits