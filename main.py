import heapq
from collections import defaultdict

def huffman_encode(input_string):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in input_string:
        frequency[char] += 1

    # Build the priority queue (min-heap) based on frequencies
    heap = [[freq, [char, ""]] for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Building the Huffman tree
    while len(heap) > 1:
        low1 = heapq.heappop(heap)  # Smallest frequency
        low2 = heapq.heappop(heap)  # Second smallest frequency
        for pair in low1[1:]:
            pair[1] = '0' + pair[1]  # Assign binary code for left branch
        for pair in low2[1:]:
            pair[1] = '1' + pair[1]  # Assign binary code for right branch
        heapq.heappush(heap, [low1[0] + low2[0]] + low1[1:] + low2[1:])

    huffman_codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    huffman_dict = {char: code for char, code in huffman_codes}
    encoded_string = ''.join(huffman_dict[char] for char in input_string)
    
    return encoded_string
