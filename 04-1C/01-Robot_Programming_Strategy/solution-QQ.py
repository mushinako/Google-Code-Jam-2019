#!/usr/bin/env python3
# from math import gcd
# from functools import reduce


# def lcm(a, b):
#     return int(a * b / gcd(a, b))


# def lcm_arr(arr):
#     return reduce(lcm, arr)


def main():
    t = int(input())
    for i in range(1, t + 1):
        a = int(input())
        c = {input().strip() for _ in range(a)}
        lens = {len(x) for x in c}
        # prog_len = lcm_arr(lens)
        prog_len = max(lens)
        # print(lens, prog_len)
        prog = ''
        for j in range(prog_len):
            if not len(c):
                break
            chars = {ci[j % len(ci)] for ci in c}
            if 'R' in chars:
                if 'S' in chars:
                    if 'P' in chars:
                        prog = 'IMPOSSIBLE'
                        break
                    else:
                        p = 'R'
                else:
                    p = 'P'
            elif 'P' in chars:
                p = 'S'
            else:
                p = 'R'
            prog += p
            c = {ci for ci in c if ci[j % len(ci)] == p}
        if len(c):
            prog = 'IMPOSSIBLE'
        print('Case #{0}: {1}'.format(i, prog))


if __name__ == "__main__":
    result = main()
