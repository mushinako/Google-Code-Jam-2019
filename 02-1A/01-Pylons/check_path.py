#!/usr/bin/env python3
import sys
import re


def main():
    response = sys.stdin.read().split('\n')
    pos = re.compile('^Case #(\d+): (IMPOSSIBLE|POSSIBLE)$')
    i = 0
    while response[i]:
        if response[i][0] == 'C':
            p = pos.match(response[i])
            i += 1
            num = int(p.group(1))
            if p.group(2) == 'POSSIBLE':
                r, c = [int(x) for x in response[i].split()]
                i += 1
                path = []
                while response[i] and response[i][0] != 'C':
                    path.append([int(x) for x in response[i].split()])
                    i += 1
                    # print(i, repr(response[i]))
                board = [[0] * c for _ in range(r)]

                def go(r, c, spot, prev_spot=None):
                    # print(spot)
                    x, y = spot
                    if 1 <= x <= r and 1 <= y <= c:
                        if prev_spot:
                            u, v = prev_spot
                            if ((x == u) or (y == v) or (x - y == u - v)
                               or (x + y == u + v)):
                                return 'Same row col diag'
                        if board[x-1][y-1] == 1:
                            return 'Already filled'
                        board[x-1][y-1] = 1
                        return 0
                    return 'Out of range'

                # print(path)
                fail = go(r, c, path[0])
                if fail:
                    print('#{0} FAILED {1} {3} {4} at 0: {2}'.format(
                        num, fail, path[0], r, c))
                    continue
                success = 1
                for j in range(1, len(path)):
                    fail = go(r, c, path[j], path[j-1])
                    if fail:
                        print('#{0} FAILED {4} {5} {6} at {1}: {2}-{3}'.format(
                            num, j, path[j-1], path[j], fail, r, c))
                        success = 0
                        break
                if not success:
                    continue
                if board_filled(board):
                    print('#{} SUCCESSFUL'.format(num))
                    continue
                print('#{} FAILED Board not filled'.format(num))
            else:
                print('#{} SKIPPED'.format(num))


def board_filled(board):
    for row in board:
        for col in row:
            if not col:
                return 0
    return 1


if __name__ == '__main__':
    main()
