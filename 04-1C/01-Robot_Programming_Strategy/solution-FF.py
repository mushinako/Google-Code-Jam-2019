#!/usr/bin/env python3
def main():
    t = int(input())
    for i in range(1, t+1):
        a = int(input())
        c = [input() for _ in range(a)]
        j = 0
        resolved = False
        res = ''
        for _ in range(500):
            first = set()
            if not c:
                resolved = True
                break
            for x in c:
                first.add(x[j % len(x)])
            if 'P' in first:
                if 'R' in first:
                    if 'S' in first:
                        break
                    else:
                        sol = 'P'
                else:
                    sol = 'S'
            else:
                sol = 'R'
            res += sol
            c = [x for x in c if x[j % len(x)] == sol]
            j += 1
        if resolved:
            print('Case {0}: {1}'.format(i, res))
        else:
            print('Case {}: IMPOSSIBLE'.format(i))


if __name__ == '__main__':
    main()
