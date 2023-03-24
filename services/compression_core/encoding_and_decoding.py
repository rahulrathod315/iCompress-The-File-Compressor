import logging

logger = logging.getLogger(__name__)


class EncodeDecode:
    def __init__(self, file_content, dictionary):
        self.file_content = file_content
        self.dictionary = dictionary

    def encode(self):
        encoded_text = ""
        try:
            for alphabet in self.file_content:
                encoded_text += self.dictionary[alphabet]
        except Exception as e:
            logger.error(f"ERROR | ENCODE | ERROR_WHILE_ENCODING_FILE | EXCEPTION : {e}")
        return encoded_text

    def encode_dictionary(self):
        encoded_dictionary = ""
        dictionary_string = str(self.dictionary).strip()
        for alphabet in dictionary_string:
            encoded_dictionary += format(ord(alphabet), '08b')
        return encoded_dictionary
    
    def decode(self):
        decoded_data = ""
        current_alphabet = ""
        inverted_dictionary = self.invert_dictionary()

        for bit in self.file_content:
            current_alphabet += bit
            if current_alphabet in inverted_dictionary:
                decoded_data += inverted_dictionary[current_alphabet]
                current_alphabet = ""

        if current_alphabet:
            raise Exception("File is not decoded successfully.")
        return decoded_data

    def invert_dictionary(self):
        return {value: key for key, value in self.dictionary.items()}

    def decode_dictionary(self):
        dictionary = ""
        for index in range(0, len(self.dictionary), 8):
            byte = self.dictionary[index:index+8]
            dictionary += chr(int(byte, 2))
        return eval(dictionary)