import sys
from iCompress.compress import Compress
from iCompress.decompress import Decompress
from iCompress.services.file_service.file_write import FileWrite

class TextCompression:
    """
    A class to handle file compression and decompression operations.

    Attributes:
        file_path (str): Path to the input or output file.
        binary_file_path (str): Path to the binary file for compressed data.
    """

    def __init__(self, file_path: str, binary_file_path: str) -> None:
        """
        Initializes the TextCompression class with file paths.

        Args:
            file_path (str): Path to the input or output file.
            binary_file_path (str): Path to the binary file for compressed data.
        """
        self.file_path = file_path
        self.binary_file_path = binary_file_path

    def compress(self) -> None:
        """
        Compresses the input file and writes the compressed binary data to the binary file.
        """
        binary_string = Compress(self.file_path).compress()
        FileWrite(self.binary_file_path, binary_string).convert_to_bytes_and_write()
        print(f"File compressed successfully: {self.binary_file_path}")

    def decompress(self) -> None:
        """
        Decompresses the binary file and writes the decompressed content to the output file.
        """
        binary_string = FileWrite(self.binary_file_path).convert_to_binary_string_from_bytes()
        text_file_content = Decompress(binary_string).decompress()
        FileWrite(self.file_path, text_file_content).write_text_data_to_file()
        print(f"File decompressed successfully: {self.file_path}")

def main() -> None:
    """
    Entry point for the application. Handles command-line arguments for compression and decompression.
    """
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