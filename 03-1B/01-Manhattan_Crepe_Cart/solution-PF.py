#!/usr/bin/env python3
def main():
    t = int(input())
    for k in range(1, t+1):
        p, q = [int(x) for x in input().split()]
        q += 1
        # Consider x- and y- directions independently
        xcoord = set()
        ycoord = set()
        xaxis = {}
        yaxis = {}
        ncnt = scnt = ecnt = wcnt = 0
        # xman = [0] * q
        # yman = [0] * q
        # Parse data into {coord: [num_facing_down, num_facing_up]}
        for _ in range(p):
            x, y, dire = input().split()
            if dire == 'N':
                ncnt += 1
                if y in ycoord:
                    yaxis[y][1] += 1
                else:
                    ycoord.add(y)
                    yaxis[y] = [0, 1, ]
                # for i in range(int(y)+1, q):
                #     yman[i] += 1
            elif dire == 'S':
                scnt += 1
                if y in ycoord:
                    yaxis[y][0] += 1
                else:
                    ycoord.add(y)
                    yaxis[y] = [1, 0, ]
                # for i in range(int(y)):
                #     yman[i] += 1
            elif dire == 'E':
                ecnt += 1
                if x in xcoord:
                    xaxis[x][1] += 1
                else:
                    xcoord.add(x)
                    xaxis[x] = [0, 1, ]
                # for i in range(int(x)+1, q):
                #     xman[i] += 1
            else:
                wcnt += 1
                if x in xcoord:
                    xaxis[x][0] += 1
                else:
                    xcoord.add(x)
                    xaxis[x] = [1, 0, ]
                # for i in range(int(x)):
                #     xman[i] += 1
        for xcoord, xnums in sorted(xaxis.items()):
            num_x_d, num_x_u = xnums

        # x = xman.index(max(xman))
        # y = yman.index(max(yman))
        print('Case #{0}: {1} {2}'.format(k, x, y))


if __name__ == '__main__':
    main()
