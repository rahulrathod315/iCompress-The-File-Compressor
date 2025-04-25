# iCompress-The-Text-File-Compressor

iCompress is a Python-based file compression tool that uses the Huffman coding algorithm to compress and decompress files. This project is designed to reduce the size of text files by encoding their contents into a more compact binary format. It also provides the capability to decompress the compressed files back to their original form.

---

## Features:
1. **File Compression**: Compresses text files using the Huffman coding algorithm.
2. **File Decompression**: Decompresses previously compressed files to restore the original content.
3. **Efficient Encoding**: Uses a frequency-based Huffman tree to generate optimal binary encodings for file contents.
4. **Cross-Platform**: Written in Python, making it compatible with any system that supports Python 3.

---

## Requirements:
To use this tool, you need to have the following installed on your system:
- **Python 3**: Ensure Python 3 is installed. You can download it from [python.org](https://www.python.org/).

---

## Project Structure:
The project is organized as follows:
```
iCompress/
    __init__.py
    compress.py          # Main script for compressing files
    decompress.py        # Main script for decompressing files
    services/
        compression_core/
            encoding_and_decoding.py  # Handles encoding and decoding logic
            frequency_tree.py         # Constructs the Huffman tree
            frequency.py              # Calculates frequency of bytes
            padding.py                # Handles padding for binary strings
            prepare_dictionary.py     # Prepares the Huffman dictionary
        file_service/
            file_metadata.py          # Manages file metadata
            file_write.py             # Handles writing to files
```

---

## How It Works:

### Compression:
1. The `compress.py` script reads the input file and calculates the frequency of each byte in the file.
2. A Huffman tree is constructed based on the frequency of each byte. Bytes with higher frequencies are assigned shorter binary codes.
3. Using the Huffman tree, each byte in the input file is encoded into a binary string of variable length.
4. The encoded binary strings, along with the Huffman tree, are written to the output file. The tree is necessary for decompression.

### Decompression:
1. The `decompress.py` script reads the compressed file and reconstructs the Huffman tree from the stored metadata.
2. Using the reconstructed tree, the binary strings in the compressed file are decoded back into their original bytes.
3. The original bytes are written to the output file, restoring the original content.

---

## Usage:

### Compressing a File:
To compress a file, navigate to the project directory in your terminal and run the following command:
```bash
python compress.py <input_file_path> <binary_file_path>
```
- `<input_file_path>`: Path to the file you want to compress.
- `<binary_file_path>`: Path where the compressed binary file will be saved.

**Example:**
```bash
python compress.py example.txt output.bin
```
This will compress `example.txt` and save the compressed output as `output.bin`.

---

### Decompressing a File:
To decompress a file, run the following command:
```bash
python decompress.py <output_file_path> <binary_file_path>
```
- `<output_file_path>`: Path where the decompressed file will be saved.
- `<binary_file_path>`: Path to the compressed binary file.

**Example:**
```bash
python decompress.py decompressed_example.txt output.bin
```
This will decompress `output.bin` and save the decompressed content as `decompressed_example.txt`.

---

## Example Workflow:
1. **Compress a File**:
   - Input: `example.txt`
   - Command: `python compress.py example.txt output.bin`
   - Output: `output.bin`

2. **Decompress the File**:
   - Input: `output.bin`
   - Command: `python decompress.py decompressed_example.txt output.bin`
   - Output: `decompressed_example.txt`

---

## Limitations:
- This tool is designed for text files. Compressing binary files may not yield significant size reductions.
- The compressed file includes metadata (Huffman tree), which may slightly increase the file size for very small inputs.

---

## Future Enhancements:
- Add support for compressing binary files.
- Implement multi-threading for faster compression and decompression.
- Provide a graphical user interface (GUI) for ease of use.

---

## License:
This project is distributed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgments:
This project uses the Huffman coding algorithm, a widely used method for lossless data compression. Special thanks to the Python community for providing excellent libraries and resources.

---

## Contact:
For any questions or feedback, please contact the project maintainer at [rahulrathod315@example.com].
