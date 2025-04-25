import sys
from iCompress.compress import Compress
from iCompress.decompress import Decompress
from iCompress.services.file_service.file_write import FileWrite

class TextCompression:
    def __init__(self, file_path, binary_file_path):
        self.file_path = file_path
        self.binary_file_path = binary_file_path

    def compress(self):
        binary_string = Compress(self.file_path).compress()
        FileWrite(self.binary_file_path, binary_string).convert_to_bytes_and_write()
        print(f"File compressed successfully: {self.binary_file_path}")

    def decompress(self):
        binary_string = FileWrite(self.binary_file_path).convert_to_binary_string_from_bytes()
        text_file_content = Decompress(binary_string).decompress()
        FileWrite(self.file_path, text_file_content).write_text_data_to_file()
        print(f"File decompressed successfully: {self.file_path}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <compress|decompress> <input_file_path> <output_file_path>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    text_compression = TextCompression(input_file_path, output_file_path)

    if operation == "compress":
        text_compression.compress()
    elif operation == "decompress":
        text_compression.decompress()
    else:
        print("Invalid operation. Use 'compress' or 'decompress'.")
        sys.exit(1)

if __name__ == "__main__":
    main()