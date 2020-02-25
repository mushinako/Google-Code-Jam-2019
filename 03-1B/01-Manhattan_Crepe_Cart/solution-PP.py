#!/usr/bin/env python3
from bisect import bisect_left, bisect_right


def calc_axis(grid_len, ppl_d, ppl_u):
    ppl_d.sort()
    ppl_u.sort()
    # Candidates are 0 or ppl_u+1
    cand = sorted(set((0,)) | set(map(lambda x: x + 1, set(ppl_u))))
    cur = cur_ppl = 0
    for c in cand:
        c_ppl = bisect_left(ppl_u, c) - bisect_right(ppl_d, c) + len(ppl_d)
        if c_ppl > cur_ppl:
            cur = c
            cur_ppl = c_ppl
    return cur


def manhattan_crepe_cart(grid_len, ppl_w, ppl_e, ppl_s, ppl_n):
    # Consider only x-axis (W, E)
    xcoord = calc_axis(grid_len, ppl_w, ppl_e)
    # Consider only y-axis (S, N)
    ycoord = calc_axis(grid_len, ppl_s, ppl_n)
    return '{0} {1}'.format(xcoord, ycoord)


def main():
    t = int(input())
    for i in range(1, t + 1):
        p, q = [int(x) for x in input().split()]
        ppl_w = []
        ppl_e = []
        ppl_s = []
        ppl_n = []
        for _ in range(p):
            data = input().split()
            coords = (int(data[0]), int(data[1]))
            if data[2] == 'W':
                ppl_w.append(int(data[0]))
            elif data[2] == 'E':
                ppl_e.append(int(data[0]))
            elif data[2] == 'S':
                ppl_s.append(int(data[1]))
            else:
                ppl_n.append(int(data[1]))
        coord = manhattan_crepe_cart(q + 1, ppl_w, ppl_e, ppl_s, ppl_n)
        print('Case #{0}: {1}'.format(i, coord))


if __name__ == "__main__":
    res = main()
