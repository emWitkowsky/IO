# Copyright by
# Michał Wojciech Witkowski

import random
import sys

def miller_rabin(n, k=20):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as (2^r)*d + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False  # n is definitely composite
    return True  # n is probably prime


def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def test_fermat(n, a):
    return power_mod(a, n - 1, n) == 1

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        if len(lines) > 1:
            a = int(lines[1])
            return n, a
        else:
            return n, None

def main():

    input_filename = "wejscie.txt"
    output_filename = "wyjscie.txt"
    fermat_only = False

    if len(sys.argv) > 1 and sys.argv[1] == "-f":
        fermat_only = True

    n, a = read_input(input_filename)

    if fermat_only:
        if test_fermat(n, a):
            result = "prawdopodobnie pierwsza"
        else:
            result = "na pewno złożona"
    else:
        if miller_rabin(n):
            result = "prawdopodobnie pierwsza"
        else:
            result = "na pewno złożona"

    with open(output_filename, 'w') as file:
        file.write(result)


if __name__ == "__main__":
    main()