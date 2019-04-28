#!/usr/bin/env python3
def main():
    t = int(input())
    for k in range(1, t+1):
        p, q = [int(x) for x in input().split()]
        q += 1
        # Consider x- and y- directions independently
        xman = [0] * q
        yman = [0] * q
        for _ in range(p):
            x, y, dire = input().split()
            if dire == 'N':
                for i in range(int(y)+1, q):
                    yman[i] += 1
            elif dire == 'S':
                for i in range(int(y)):
                    yman[i] += 1
            elif dire == 'E':
                for i in range(int(x)+1, q):
                    xman[i] += 1
            else:
                for i in range(int(x)):
                    xman[i] += 1
        x = xman.index(max(xman))
        y = yman.index(max(yman))
        print('Case #{0}: {1} {2}'.format(k, x, y))


if __name__ == '__main__':
    main()
