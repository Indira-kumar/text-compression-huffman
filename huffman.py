import heapq
import collections

def huffman_encoding(file_in, file_out):
    # Read the input file and count the frequency of each character
    freq = collections.Counter(file_in.read())

    # Build the Huffman tree
    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Generate the encoding for each character
    encoding = {}
    for pair in heapq.heappop(heap)[1:]:
        encoding[pair[0]] = pair[1]

    # Write the encoded output to the output file
    file_out.write("".join([encoding[ch] for ch in file_in.read()]))

# Example usage
with open("input.txt", "r") as file_in:
    with open("output.txt", "w") as file_out:
        huffman_encoding(file_in, file_out)
# First, we create a list of nodes, where each node is a list containing the frequency of the character and a list of the character and its code. For example, the node for the character "a" with frequency 3 would be [3, ["a", ""]].

# We then create a heap from this list of nodes using the heapify function from the heapq module. This function rearranges the list in-place to form a heap.

# We enter a loop that continues until the heap has only one node left (the root of the tree). Within the loop, we pop the two nodes with the lowest frequencies off the heap using the heappop function. These nodes will become the children of a new parent node.

# For each character in the left child (the node with the lower frequency), we prepend a "0" to its code. For each character in the right child (the node with the higher frequency), we prepend a "1" to its code.

# We then create a new parent node with the sum of the frequencies of the two children as its frequency, and the two children as its children.

# Finally, we push the new parent node back onto the heap using the heappush function.

# This process continues until the heap has only one node left, at which point the tree is complete. The codes for each character can then be extracted from the tree by traversing the tree and looking at the code for each character.
def huffman_decoding(file_in, file_out):
    # Read the Huffman encoding from the input file
    encoding = {}
    for line in file_in:
        ch, code = line.strip().split(":")
        encoding[code] = ch

    # Decode the encoded message
    decoded = ""
    current_code = ""
    for ch in file_in.read():
        current_code += ch
        if current_code in encoding:
            decoded += encoding[current_code]
            current_code = ""

    # Write the decoded message to the output file
    file_out.write(decoded)

# Example usage
with open("encoded.txt", "r") as file_in:
    with open("decoded.txt", "w") as file_out:
        huffman_decoding(file_in, file_out)

# The function huffman_decoding takes two file objects as arguments: file_in and file_out. The file_in object is used to read the Huffman encoding and the encoded message from the input file, and the file_out object is used to write the decoded message to the output file.

# The first step in the decoding process is to read the Huffman encoding from the input file. This is done by looping through each line in the file and splitting it on the colon character (":"). The left side of the colon is the character, and the right side is the code. These values are then added to the encoding dictionary, with the code as the key and the character as the value.

# The next step is to decode the encoded message. To do this, we initialize an empty string called decoded and a string called current_code that will be used to store the code that we are currently building up as we read the encoded message.

# We then loop through each character in the encoded message, adding it to the current_code string. If the current_code string is in the encoding dictionary, we append the corresponding character to the decoded string and reset the current_code string to be empty. If the current_code string is not in the encoding dictionary, we continue adding characters to it until we find a matching code.

# Finally, we write the decoded string to the output file using the file_out object. This completes the decoding process.

# To decode the encoded message, the decoder reads the encoding file and builds a dictionary that maps the codes to the corresponding characters. It then reads the encoded message one character at a time, adding the characters to a current code until it finds a matching code in the dictionary. When a matching code is found, the decoder adds the corresponding character to the decoded message and resets the current code to be empty. This process is repeated until the entire encoded message has been decoded.
