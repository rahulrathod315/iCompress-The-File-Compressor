class Padding:
    def __init__(self, file_content):
        self.file_content = file_content

    def add_padding(self):    # add 64 bit padding at the start and return
        total_bits_in_file = len(self.file_content)
        length_of_total_bits_in_binary = "{0:b}".format(total_bits_in_file)
        zero_prefix = "0" * (64 - len(length_of_total_bits_in_binary))
        final_padding = '1' + zero_prefix + length_of_total_bits_in_binary
        return final_padding + self.file_content

    def remove_padding(self):   # remove 64-bit padding from start and return
        if len(self.file_content) < 65:
            raise ValueError("Binary string is too short to contain valid padding.")
        
        padding = self.file_content[1:65]
        if not padding.isdigit():
            raise ValueError("Invalid padding detected in the binary string.")
        
        file_content_length = int(padding, 2)
        if len(self.file_content) < file_content_length + 65:
            raise ValueError("Binary string is truncated or corrupted.")
        
        return self.file_content[65:file_content_length+65], self.file_content[file_content_length+65:]  # return file_content, tail_content