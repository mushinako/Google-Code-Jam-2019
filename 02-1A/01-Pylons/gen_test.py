#!/usr/bin/env python3
import sys
import random
from datetime import datetime


def main():
    random.seed(datetime.now())
    t = int(sys.argv[1])
    choices = list(range(2, 21))
    s = set()
    while len(s) < t:
        s.add((random.choice(choices), random.choice(choices)))
    with open('test.in', 'w') as f:
        f.write('{}\n'.format(t))
        for x in s:
            f.write('{0} {1}\n'.format(*x))


if __name__ == '__main__':
    main()
