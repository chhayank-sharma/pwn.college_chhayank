# -*- coding: utf-8 -*-
# Recover full flag from CTFQ Feistel output

import itertools

# 1️⃣ Load output.txt lines
lines = [
"01011100010110010111101001100110011011110111100101001000011101010110111001110100",
"01001101011110010110011101010111011010010101110001011001011110100110011001101111",
"00100001010101010111001101110101010110010100110101111001011001110101011101101001",
"00000010011100110110011001001101010001010010000101010101011100110111010101011001",
"01001101010000100100101001001110011110110000001001110011011001100100110101000101",
"00100000010111100111001101101011010100010100110101000010010010100100111001111011",
"01011100011110000101000001001011011011010010000001011110011100110110101101010001",
"00100011011010010110110100010010010011000101110001111000010100000100101101101101",
"00011110011110000101001100000110010001110010001101101001011011010001001001001100",
"01001000001000100101001001110001011011110001111001111000010100110000011001000111",
"00001001001110000111100000101000010001110100100000100010010100100111000101101111",
"00110100011010000111010100011100011011110000100100111000011110000010100001000111",
"00001101001000110111000001011111010011010011010001101000011101010001110001101111"
]

# Convert binary string to bytes
def binstr_to_bytes(s):
    return bytes(int(s[i:i+8],2) for i in range(0,len(s),8))

states = [binstr_to_bytes(l) for l in lines]

# Split state into halves
def split_halves(b):
    hl = len(b)//2
    return b[:hl], b[hl:]

# 2️⃣ Recover keys 2..13 from consecutive states
recovered_keys = []
for i in range(len(states)-1):
    l0, r0 = split_halves(states[i])
    l1_next, _ = split_halves(states[i+1])
    # key_i+1 = l1_next ^ l0 ^ r0
    k = bytes(a ^ b ^ c for a,b,c in zip(l1_next, l0, r0))
    recovered_keys.append(k)

# 3️⃣ Feistel simulation function
def feistel_simulate(block, keys):
    l0 = block[:len(block)//2]
    r0 = block[len(block)//2:]
    outputs = []
    for k in keys:
        r1 = bytes(a ^ b ^ c for a,b,c in zip(l0, r0, k))
        l1 = r0
        r0, l0 = r1, l1
        outputs.append(r0 + l0)
    return outputs

# 4️⃣ Brute-force missing 5th byte of first key
known_prefix = b"ctf{"
middle = b''.join(recovered_keys)
final_tail = b"rnel"

found_flags = []

for x in range(32,127):
    k1 = known_prefix + bytes([x])
    r1, l1 = split_halves(states[0])
    # l0 = r1 ^ r0 ^ k1, r0 = l1
    r0 = l1
    l0 = bytes(a ^ b ^ c for a,b,c in zip(r1, r0, k1))
    S0 = l0 + r0
    keys_all = [k1] + recovered_keys
    outputs = feistel_simulate(S0, keys_all)
    if outputs == states:
        flag = k1 + middle + final_tail
        if all(32 <= b < 127 for b in flag):
            found_flags.append(flag.decode())

# 5️⃣ Print recovered flag(s)
for f in found_flags:
    print("Recovered flag:", f)
