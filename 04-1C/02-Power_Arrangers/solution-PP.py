#!/usr/bin/env python3
import sys
from collections import Counter


def main():
    t, _ = [int(x) for x in input().split()]
    for _ in range(t):
        power_arrangers()


def power_arrangers():
    res = ''
    can = ['A', 'B', 'C', 'D', 'E']
    # eprint()
    first = []
    # 119 requests
    for i in range(1, 596, 5):
        fprint(i)
        first.append(judge_input())
    # Find the missing first one
    cfirst = Counter(first)
    for x in can:
        if cfirst[x] != 24:
            res += x
            break
    can = [x for x in can if x != res]
    second_can = [5*i+2 for i in range(119) if first[i] == res]
    second = []
    # 23 requests
    for i in second_can:
        fprint(i)
        second.append(judge_input())
    # Find the missing second one
    csecond = Counter(second)
    for x in can:
        if csecond[x] != 6:
            res += x
            break
    can = [x for x in can if x != res[-1]]
    third_can = [second_can[i]+1 for i in range(23) if second[i] == res[-1]]
    third = []
    # 5 requests
    for i in third_can:
        fprint(i)
        third.append(judge_input())
    # Find the missing third one
    cthird = Counter(third)
    for x in can:
        if cthird[x] != 2:
            res += x
            break
    can = [x for x in can if x != res[-1]]
    # 1 request & Find the missing fourth one
    for i in range(5):
        if third[i] == res[-1]:
            fprint(third_can[i]+1)
            fourth = judge_input()
            break
    # Find the missing fifth one
    for x in can:
        if x != fourth:
            res += x + fourth
            break
    # Response
    fprint(res)
    # eprint(res)
    if judge_input() == 'Y':
        # eprint('Success!')
        return
    # eprint('Fail!')
    sys.exit(99)


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
    if x == 'N':
        sys.exit(99)
    return x


if __name__ == '__main__':
    main()
