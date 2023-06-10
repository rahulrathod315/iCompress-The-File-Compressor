# iCompress-The-Text-File-Compressor

iCompress is a Python-based file compression tool that uses the Huffman coding algorithm to compress files. It takes a file input, compresses it using Huffman coding, and generates a compressed output file. It also has the capability to decompress the compressed file and retrieve the original file.

# Requirements:
To use this tool, you need to have Python 3 installed on your system. You also need to have the following Python libraries installed:
  1. argparse
  2. heapq
  
# Usage:
To compress a file, navigate to the project directory in your terminal and run the following command:
  ```
  python compress.py <input_file_path> <output_file_path>
  ```
where <input_file_path> is the path to the file you want to compress and <output_file_path> is the path to the compressed output file.

To decompress a compressed file, run the following command:
  ```
  python decompress.py <compressed_file_path> <output_file_path>
  ```
where <compressed_file_path> is the path to the compressed file and <output_file_path> is the path to the decompressed output file.

# How it works:
When you run the compress.py file, it first reads in the input file and calculates the frequency of each byte in the file. It then constructs a Huffman tree based on the frequency of each byte, with the most frequently occurring bytes having the shortest codes. Using this Huffman tree, it encodes each byte of the input file into a binary string of variable length. The binary strings are then written to the output file along with the Huffman tree, which is necessary for decompression.

When you run the decompress.py file, it reads in the compressed file and reconstructs the Huffman tree. It then uses this tree to decode the binary strings and write the original bytes to the output file.
