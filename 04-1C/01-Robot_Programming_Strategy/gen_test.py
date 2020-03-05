#!/usr/bin/env python3
import random


def main():
    MAX_K = 3
    MAX_CHAR_LEN = 50

    # MOVES = ['R', 'P', 'S']
    MOVES = ['R', 'P']
    OUT_FILE = 'test.in'
    # As = [2 ** x - 1 for x in range(1, MAX_K + 1)]
    As = [3, 7]
    CHAR_LENs = list(range(1, MAX_CHAR_LEN + 1))
    t = int(input('Number of cases: '))
    with open(OUT_FILE, 'w') as f:
        print(t, file=f)
        for _ in range(t):
            a = random.choice(As)
            print(a, file=f)
            for __ in range(a):
                char_len = random.choice(CHAR_LENs)
                chars = ''.join(random.choice(MOVES)
                                for ___ in range(char_len))
                print(chars, file=f)


if __name__ == "__main__":
    result = main()
