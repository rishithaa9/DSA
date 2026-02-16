#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

MOD = 10**9 + 7

def solve(s):
    from collections import Counter

    freq = Counter(s)

    # Half counts
    half_counts = [v // 2 for v in freq.values()]
    half_len = sum(half_counts)

    # Precompute factorials and inverse factorials
    fact = [1] * (half_len + 1)
    inv_fact = [1] * (half_len + 1)

    for i in range(1, half_len + 1):
        fact[i] = fact[i - 1] * i % MOD

    # Fermat's little theorem for inverse factorial
    inv_fact[half_len] = pow(fact[half_len], MOD - 2, MOD)
    for i in range(half_len, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    # Calculate result
    result = fact[half_len]
    for c in half_counts:
        result = result * inv_fact[c] % MOD

    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(str(result) + '\n')

    fptr.close()
