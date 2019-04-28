#!/usr/bin/env python3


def getmaxcoord(man, q):
    most = max(map(max, man))
    for j in range(q):
        for i in range(q):
            if man[i][j] == most:
                return (j, i)


def main():
    t = int(input())
    for k in range(1, t+1):
        p, q = [int(x) for x in input().split()]
        q += 1
        # ppls = []
        man = [[0] * q for _ in range(q)]
        # xl = yl = 0
        # xu = yu = q
        for _ in range(p):
            xcoord, ycoord, dire = input().split()
            x = int(xcoord)
            y = int(ycoord)
            if dire == 'N':
                for i in range(y+1, q):
                    for j in range(q):
                        man[i][j] += 1
            elif dire == 'S':
                for i in range(y):
                    for j in range(q):
                        man[i][j] += 1
            elif dire == 'E':
                for i in range(q):
                    for j in range(x+1, q):
                        man[i][j] += 1
            else:
                for i in range(q):
                    for j in range(x):
                        man[i][j] += 1
        x, y = getmaxcoord(man, q)
        print('Case #{0}: {1} {2}'.format(k, x, y))


if __name__ == '__main__':
    main()
