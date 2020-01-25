#!/usr/bin/env python3
def main():
    t = int(input())
    for prob_num in range(1, t + 1):
        p, q = [int(x) for x in input().split()]
        q += 1
        # Consider x- and y-directions independently
        xcoord = set()
        ycoord = set()
        xaxis = [None] * q
        yaxis = [None] * q
        # ncnt = scnt = ecnt = wcnt = 0
        # Parse data into {coord: [num_facing_one_dire, num_faction_other_dire]}
        for _ in range(p):
            x, y, dire = input().split()
            x, y = int(x), int(y)
            if dire == 'N':
                # ncnt += 1
                if y in ycoord:
                    yaxis[y][1] += 1
                else:
                    ycoord.add(y)
                    yaxis[y] = [0, 1]
            elif dire == 'S':
                # scnt += 1
                if y in ycoord:
                    yaxis[y][0] += 1
                else:
                    ycoord.add(y)
                    yaxis[y] = [1, 0]
            elif dire == 'E':
                # ecnt += 1
                if x in xcoord:
                    xaxis[x][1] += 1
                else:
                    xcoord.add(x)
                    xaxis[x] = [0, 1]
            else:
                # wcnt += 1
                if x in xcoord:
                    xaxis[x][0] += 1
                else:
                    xcoord.add(x)
                    xaxis[x] = [1, 0]
        # Calc for each point (x)
        res_x = 0
        res_x_cnt = 0
        pot_x = {0} | set([x + 1 for x in xcoord])
        for x in sorted(pot_x):
            x_cnt = 0
            for px in range(len(xaxis)):
                if xaxis[px] is None:
                    continue
                if px == x:
                    continue
                if px < x:
                    x_cnt += xaxis[px][1]
                else:
                    x_cnt += xaxis[px][0]
            if x_cnt > res_x_cnt:
                res_x = x
                res_x_cnt = x_cnt
        # Calc for each point (y)
        res_y = 0
        res_y_cnt = 0
        pot_y = {0} | set([y + 1 for y in ycoord])
        for y in sorted(pot_y):
            y_cnt = 0
            for py in range(len(yaxis)):
                if yaxis[py] is None:
                    continue
                if py == y:
                    continue
                if py < y:
                    y_cnt += yaxis[py][1]
                else:
                    y_cnt += yaxis[py][0]
            if y_cnt > res_y_cnt:
                res_y = y
                res_y_cnt = y_cnt
        # Print
        print('Case #{0}: {1} {2}'.format(prob_num, res_x, res_y))


if __name__ == '__main__':
    main()
