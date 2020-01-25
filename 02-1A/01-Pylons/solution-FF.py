#!/usr/bin/env python3
def main():
    t = int(input())
    sol_35 = [(3, 2), (1, 1), (2, 3),
              (3, 5), (1, 4), (2, 1),
              (3, 3), (1, 2), (2, 4),
              (3, 1), (1, 5), (2, 2),
              (3, 4), (1, 3), (2, 5), ]
    for i in range(1, t+1):
        r, c = [int(x) for x in input().split()]
        # If both sides are less than 5, IMPOSSIBLE
        if r < 5 and c < 5:
            print('Case #{}: IMPOSSIBLE'.format(i))
            continue
        print('Case #{}: POSSIBLE'.format(i))
        # Debug use
        print(r, c)
        # If either size is even, chop into 2×n blocks
        # Row even
        if not r % 2:
            print_even_row(r, c)
            continue
        # Column even
        if not c % 2:
            print_even_col(r, c)
            continue
        if c > 4:
            # Both odd, chop into 3×5, 3×(c-5), (r-3)×c
            #                            even   even
            # 3×5, any, can be brute-forced
            for x, y in sol_35:
                print(x, y)
            # 3×(c-5)
            print_even_col(3, c, col_start=6)
            # (r-3)×c
            print_even_row(r, c, row_start=4)
        # Insufficient col, chop into 5×3 and (r-5)×3
        for y, x in sol_35:
            print(x, y)
        print_even_row(r, c, row_start=6)


def print_even_row(r, c, row_start=1, col_start=1):
    assert not (r - row_start + 1) % 2
    for j in range(row_start, r+1, 2):
        for k in range(col_start, c+1):
            print(j, k)
            print(j+1, k+3)


def print_even_col(r, c, row_start=1, col_start=1):
    assert not (c - col_start + 1) % 2
    for k in range(col_start, c+1, 2):
        for j in range(row_start, r+1):
            print(j, k)
            print(j+3, k+1)


if __name__ == '__main__':
    main()
