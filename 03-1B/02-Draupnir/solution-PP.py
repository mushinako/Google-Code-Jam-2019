#!/usr/bin/env python3
import sys


# My choice of days to be sent
DAYS = (56, 170)


def main():
    t, _ = [int(x) for x in input().split()]
    for _ in range(t):
        draupnir()


def draupnir():
    # eprint()
    judge_res = []
    # Get both judge responses
    for d in DAYS:
        fprint(d)
        judge_res.append(int(judge_input()))
    # eprint(judge_res)
    fprint(*calc(*judge_res))
    if judge_input() == '1':
        # eprint('Success!')
        return
    sys.exit(99)


def calc(d56, d170):
    # Notice there're at most 100 < 128 = 2**7 rings, thus a factor difference
    #   of 2**7 is sufficient to separate variables
    # Day 56
    assert not d56 % 2 ** 9
    d56 //= 2 ** 9    # d56 = 2**47*r1 + 2**19*r2 + 512*r3 + 32*r4 + 4*r5 + r6
    r1 = d56 // 2 ** 47
    r2 = d56 % 2 ** 47 // 2 ** 19
    d56res = d56 % 2 ** 19          # d56res = 512*r3 + 32*r4 + 4*r5 + r6
    # Day 170
    assert not d170 % 2 ** 28
    d170 //= 2 ** 28  # d170 = 2**28*r3 + 2**14*r4 + 64*r5 + r6
    r3 = d170 // 2 ** 28
    r4 = d170 % 2 ** 28 // 2 ** 14
    d170res = d170 % 2 ** 14        # d170res = 64*r5 + r6
    # Put r3, r4 back into `d56res`
    d56res -= 512 * r3 + 32 * r4    # d56res = 4*r5 + r6
    # Solve for r5, r6
    diff = d170res - d56res
    assert not diff % 60
    r5 = diff // 60
    r6 = d56res - 4 * r5
    # eprint(r1, r2, r3, r4, r5, r6)
    return (r1, r2, r3, r4, r5, r6)


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
