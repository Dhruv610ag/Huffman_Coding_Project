# Huffman-Coding-Code

## 📌 Overview  
This project implements *Huffman Coding* in Python to efficiently *compress and decompress* text files. The algorithm assigns *shorter binary codes* to frequently occurring characters, reducing storage space while maintaining lossless compression.  

## 🚀 Features  
•⁠  ⁠*Efficient compression* of text files using Huffman Encoding.  
•⁠  ⁠*Decompression support* to restore the original file.  
•⁠  ⁠*Uses priority queues & binary trees* for encoding.  
•⁠  ⁠*Automatic padding & byte conversion* for binary storage.  

## 🔧 How It Works  
1.⁠ ⁠*Compression:*  
   - Reads the input text file.  
   - Constructs a *frequency dictionary* for characters.  
   - Builds a *min-heap* and a *Huffman tree*.  
   - Generates *Huffman codes* and encodes the text.  
   - Writes the compressed binary file (⁠ .bin ⁠).  

2.⁠ ⁠*Decompression:*  
   - Reads the compressed ⁠ .bin ⁠ file.  
   - Reconstructs the *Huffman tree*.  
   - Decodes the binary data back into text.  
   - Outputs the original text file.  

## 📂 File Structure  
•⁠  ⁠*huffman_coding.py* → Implementation of Huffman Compression & Decompression  
•⁠  ⁠*sample.txt* → Input text file  
•⁠  ⁠*sample.bin* → Compressed binary output  
•⁠  ⁠*sample_decompress.txt* → Decompressed output file  

## 📈 Applications  
•⁠  ⁠*File Compression* (reducing text file size).  
•⁠  ⁠*Data Transmission* (efficient encoding).  
•⁠  ⁠*Text-based Encoding* (for secure storage).  

## 🏆 Key Learnings  
•⁠  ⁠Implementing *priority queues* & *binary trees* in Python.  
•⁠  ⁠*Optimizing storage space* using Huffman Encoding.  
•⁠  ⁠Handling *bitwise operations* & file I/O efficiently.
