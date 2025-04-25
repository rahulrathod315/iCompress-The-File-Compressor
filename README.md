# iCompress - The File Compressor

iCompress is a Python package for efficient file compression and decompression using Huffman coding. It is designed to reduce file sizes while maintaining data integrity, making it ideal for storage optimization and file transfer.

---

## Features

- **Custom Compression Algorithms**: Implements Huffman coding for efficient text compression.
- **Decompression Support**: Restores compressed files to their original state.
- **Command-Line Interface**: Easy-to-use CLI for compression and decompression tasks.
- **Cross-Platform**: Works on all major operating systems with Python 3.6+.

---

## Installation

iCompress is available on PyPI and can be installed using `pip`:

```bash
pip install iCompress
```

---

## Usage

### Command-Line Interface

#### Compress a File
To compress a file, use the following command:
```bash
python3 -m iCompress compress <input_file> <output_file>
```
Example:
```bash
python3 -m iCompress compress example.txt output.bin
```

#### Decompress a File
To decompress a file, use the following command:
```bash
python3 -m iCompress decompress <output_file> <decompressed_file>
```
Example:
```bash
python3 -m iCompress decompress output.bin uncompressed.txt
```

---

## How to Use This Repository

If you want to explore or contribute to the source code, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/rahulrathod315/iCompress-The-File-Compressor.git
   cd iCompress-The-File-Compressor
   ```

2. Install the package in editable mode for development:
   ```bash
   pip install -e .
   ```

3. Run the compression and decompression commands as described above.

4. To test the package, you can use the provided `example.txt` file or any other text file.

---

## Project Structure

```
iCompress/
    __init__.py
    compress.py          # Main compression logic
    decompress.py        # Main decompression logic
    services/
        compression_core/
            encoding_and_decoding.py  # Encoding and decoding logic
            frequency_tree.py         # Huffman tree implementation
            frequency.py              # Frequency analysis for compression
            padding.py                # Padding utilities for bit alignment
            prepare_dictionary.py     # Dictionary preparation for encoding
        file_service/
            file_metadata.py          # Handles file metadata during compression
            file_write.py             # Writes compressed data to files
setup.py               # Package setup configuration
README.md              # Project documentation
LICENSE                # License information
example.txt            # Sample input file for testing
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please contact the project maintainer at `rahul.rathod@gmail.com`.
