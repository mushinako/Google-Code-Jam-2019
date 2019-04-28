#!/usr/bin/env python3
def main():
    t = int(input())
    for m in range(1, t+1):
        n, k = [int(x) for x in input().split()]
        c = [int(x) for x in input().split()]
        d = [int(x) for x in input().split()]
        res = 0
        for i in range(n):
            for j in range(i, n):
                x = max(c[i:j+1])
                y = max(d[i:j+1])
                if abs(x-y) <= k:
                    res += 1
        print('Case #{0}: {1}'.format(m, res))


if __name__ == '__main__':
    main()
