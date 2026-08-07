import heapq
from collections import Counter
import time
import sys

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

        print(f"Merging nodes: {left.char} ({left.freq}) and {right.char} ({right.freq})")
        time.sleep(0.5)

    return heap[0]


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix
            print(f"Assigning code to '{node.char}' : {prefix}")
            time.sleep(0.3)

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(data):
    frequencies = Counter(data)

    print("\nCharacter Frequencies")
    print(frequencies)

    root = build_huffman_tree(frequencies)

    codebook = generate_codes(root)

    encoded_data = "".join(codebook[ch] for ch in data)

    print("\nEncoded Data:")
    print(encoded_data)

    return encoded_data, codebook


def huffman_decoding(encoded_data, codebook):
    reverse = {v: k for k, v in codebook.items()}

    decoded = ""
    code = ""

    for bit in encoded_data:
        code += bit

        if code in reverse:
            print(f"Decoding {code} -> {reverse[code]}")
            decoded += reverse[code]
            code = ""
            time.sleep(0.2)

    return decoded


def animate(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.03)
    print()


if __name__ == "__main__":

    animate("===== Huffman Coding Application =====")

    text = input("Enter the text to encode: ")

    print("\nStarting Encoding...\n")

    encoded, codebook = huffman_encoding(text)

    print("\nCodebook")
    print(codebook)

    print("\nStarting Decoding...\n")

    decoded = huffman_decoding(encoded, codebook)

    print("\nOriginal Text :", text)
    print("Encoded Text  :", encoded)
    print("Decoded Text  :", decoded)

    if text == decoded:
        print("\nSUCCESS: Encoding and Decoding Successful.")
    else:
        print("\nERROR!")
