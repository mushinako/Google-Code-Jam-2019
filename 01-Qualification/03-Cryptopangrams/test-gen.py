#!/usr/bin/env python3
# Usage:
#   python3 test-gen.py number
#       number: an integer, number of test cases

import sys
import random
import string
from datetime import datetime


def main():
    # Use current time as `random` seed for greater variation
    random.seed(datetime.now())
    # Read primes
    with open('primes.txt', 'r') as f:
        all_primes = f.read().split()
    # `t`: Number of test cases
    t = int(sys.argv[1])
    with open('test.in', 'w') as f:
        with open('sol.txt', 'w') as g:
            f.write(str(t)+'\n')
            g.write(str(t)+'\n')
            for _ in range(t):
                f.write('\n')
                # `primes_s`: 26 primes, `set` to avoid duplicates
                primes_s = set()
                while len(primes_s) < 26:
                    x = random.choice(all_primes)
                    primes_s.add(x)
                # `primes_l`: 26 primes, sorted
                primes_l = sorted(list(primes_s), key=int)
                # Write chosen primes to 'sol.txt'
                g.write(', '.join(primes_l)+'\n')
                message = []
                letters_left = list(range(0, 26))
                # While `letters_left` is not empty, randomly choose a letter
                # All 'letters' are mere indices of letters now, 0-based
                while letters_left:
                    letter = random.randint(0, 25)
                    if letter in letters_left:
                        letters_left.remove(letter)
                    message.append(letter)
                # Write the message to 'sol.txt'
                g.write(''.join([string.ascii_uppercase[i] for i in message])
                        + '\n')
                # Calculate secret message
                secret = []
                for i in range(len(message)-1):
                    prod = (int(primes_l[message[i]])
                            * int(primes_l[message[i+1]]))
                    secret.append(str(prod))
                # Write secret message to 'test.in'
                f.write(' '.join(secret)+'\n')


if __name__ == '__main__':
    main()
