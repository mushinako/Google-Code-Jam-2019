#!/usr/bin/env python3
def main():
    # `t`: Number of test cases
    t = int(input())
    for i in range(1, t+1):
        # `n`: The 4-prone number
        n = input()
        a = n.replace('4', '3')
        print('Case #{0}: {1} {2}'.format(i, a, int(n)-int(a)))


if __name__ == '__main__':
    main()
