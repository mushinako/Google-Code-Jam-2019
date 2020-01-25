#!/usr/bin/env python3
def main():
    t = int(input())
    for i in range(1, t + 1):
        p, _ = [int(x) for x in input().split()]
        # Consider x- and y- directions independently
        # List of people going each directions
        xe = []
        xw = []
        yn = []
        ys = []
        # Parse each person
        for _ in range(p):
            x, y, dire = input().split()
            coord = (int(x), int(y))
            if dire == 'N':
                yn.append(coord)
                continue
            if dire == 'S':
                ys.append(coord)
                continue
            if dire == 'E':
                xe.append(coord)
                continue
            if dire == 'W':
                xw.append(coord)
                continue
        # Potential results
        xcoords = sorted(list(set([c[0]+1 for c in xe])))
        ycoords = sorted(list(set([c[1]+1 for c in yn])))
        # Check results (x)
        xmaxppl = 0
        xmaxcoord = 0
        for x in xcoords:
            xppl = len([1 for c in xe if c[0] < x]) + \
                len([1 for c in xw if c[0] > x]) + \
                len([1 for c in yn+ys if c[0] == x])
            if xppl > xmaxppl:
                xmaxppl = xppl
                xmaxcoord = x
        # Check results (y)
        ymaxppl = 0
        ymaxcoord = 0
        for y in ycoords:
            yppl = len([1 for c in yn if c[1] < y]) + \
                len([1 for c in ys if c[1] > y]) + \
                len([1 for c in xe+xw if c[1] == y])
            if yppl > ymaxppl:
                ymaxppl = yppl
                ymaxcoord = y
        # Print
        print('Case #{0}: {1} {2}'.format(i, xmaxcoord, ymaxcoord))


if __name__ == '__main__':
    main()
