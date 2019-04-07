#!/usr/bin/env python3
def main():
    # `t`: Number of test cases
    t = int(input())
    for i in range(1, t+1):
        # `n` is discarded as it's not necessary
        input()
        p = input()
        # Swap `E`'s and `S`'s
        res = p.replace('E', '0').replace('S', 'E').replace('0', 'S')
        print('Case #{0}: {1}'.format(i, res))


if __name__ == '__main__':
    main()
