#!/usr/bin/env python3
# prints all 256 URLs for pattern (s|c)(q|g)(x|y)(h|n)(x|v)(B|D)(h|n)(S|Z)

from itertools import product

BASE = "https://pastebin.com/"
choices = [
    ("s","c"),
    ("q","g"),
    ("x","y"),
    ("h","n"),
    ("x","v"),
    ("B","D"),
    ("h","n"),
    ("S","Z"),
]

for i, combo in enumerate(product(*choices), start=1):
    print(f"{BASE}{''.join(combo)}")
