#!/usr/bin/env python3
def main():
    # `t`: Number of test cases
    t = int(input())
    for i in range(1, t+1):
        # `n`: The 4-prone number
        n = input()
        a = b = ''
        for x in n:
            if x == '4':
                a += '1'
                b += '3'
            else:
                a += '0'
                b += x
        # `a` converted back to `int` to eliminate preceding 0's
        print('Case #{0}: {1} {2}'.format(i, int(a), b))


if __name__ == '__main__':
    main()
