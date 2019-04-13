#!/usr/bin/env python3
import sys


BLADES = [2**4, 3**2, 5, 7, 11, 13, 17]
PROD = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17


def main():
    # No need of `n` and `m`
    t, _, __ = [int(x) for x in input().split()]
    for _ in range(t):
        golf_gophers()


def golf_gophers():
    # Collect judge response for all coprime numbers
    judge_res = []
    for p in BLADES:
        fprint(' '.join([str(p)]*18))
        judge_res.append(sum(
            [int(x) for x in judge_input().split()]))
    # eprint(judge_res)
    # Calculate using Chinese remainder theorem
    fprint(crt(BLADES, judge_res))
    if judge_input() == '1':
        return
    sys.exit(99)


# Chinese remainder theorem
def crt(mods, rems):
    sum = 0
    for m, r in zip(mods, rems):
        p = PROD // m
        # eprint(m, r, p)
        sum += r * p * mul_inv(p, m)
    return sum % PROD


# Multiplicative inverse of a (mod b)
def mul_inv(a, b):
    if b == 1:
        return 1
    tmp = b
    x = 0
    y = 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x, y = y - q * x, x
    if y < 0:
        y += tmp
    return y


# Flush printing
def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# Error printing, for debug only
# def eprint(*args, **kwargs):
#     print(*args, **kwargs, flush=True, file=sys.stderr)


# Make sense of judge output
def judge_input():
    x = input()
    # eprint(x)
    if x == '-1':
        sys.exit(99)
    return x


if __name__ == '__main__':
    main()
