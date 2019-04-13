#!/usr/bin/env python3
import sys
import re


def main():
    # `t`: Number of test cases, no need to check for `-1`
    t = int(input())
    for _ in range(t):
        # Do wan singol tes
        dat_tes()


# Error printing, for debug only, not used
# def eprint(*args, **kwargs):
#     print(*args, **kwargs, flush=True, file=sys.stderr)


# Flush printing
def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# Generate full search parameters, i.e., add non-interesting groups to query
def gen_full(block_param, blocks, n):
    # Everything not bad blocks are 0
    # Starting 0's
    ret = '0' * blocks[0][0]
    # Middle mess
    for i in range(len(blocks)-1):
        ret += block_param
        ret += '0' * (blocks[i+1][0]-blocks[i][1])
    # Ending
    return (ret + block_param[:blocks[-1][1]-blocks[-1][0]]
            + '0' * (n-blocks[-1][1]))


# Remove clunks, i.e., non-interesting groups, from judge response
def clean_input(inp, blocks):
    ret = []
    # Remove starting 0's
    inp = inp[blocks[0][0]:]
    # Middle mess
    for i in range(len(blocks)-1):
        lim = 16 - blocks[i][2]
        ret.append(inp[:lim])
        inp = inp[lim+blocks[i+1][0]-blocks[i][1]:]
    # Ending
    ret.append(inp[:16-blocks[-1][2]])
    return ret


# Exit when judge returns -1
def parse_input():
    x = input()
    if x == '-1':
        sys.exit(99)
    return x


# Testor
def dat_tes():
    n, b, f = [int(x) for x in parse_input().split()]
    # 1st try
    # Chop into 16-sized blocks and make each one all 0 or all 1, alternating
    q = n // 32
    r1 = n % 32 // 16
    r2 = n % 16
    ret = ('0' * 16 + '1' * 16) * q
    if r1:
        ret += '0' * 16 + '1' * r2
    else:
        ret += '0' * r2
    fprint(ret)
    res = parse_input()
    # Figure out which block contains bad machines
    bad_blocks = []
    se1 = re.compile('0(1|$)')
    se2 = re.compile('1(0|$)')
    # Check full-32 blocks
    for i in range(q):
        x = se1.search(res).span()[0] + 1
        y = se2.search(res).span()[0] + 1
        res = res[y:]
        if x != 16:
            bad_blocks.append([i*32, i*32+16, 16-x])
        if y - x != 16:
            bad_blocks.append([i*32+16, i*32+32, 16+x-y])
    # Check 16-block, if exists
    if r1:
        x = se1.search(res).span()[0] + 1
        res = res[x:]
        if x != 16:
            bad_blocks.append([q*32, q*32+16, 16-x])
    # Check remaining
    if r2 and len(res) != r2:
        bad_blocks.append([n-r2, n, r2-len(res)])
    # We have at most 15 blocks of 16 in `bad_blocks`
    # Each element in each block can be id-ed as 0 to 15, 4-bit binary
    # Set up search parameters for each block
    sp = [
        '0' * 8 + '1' * 8,
        ('0' * 4 + '1' * 4) * 2,
        ('0' * 2 + '1' * 2) * 4,
        '01' * 8,
        ]
    # Generate Full Search Parameters
    fp = [gen_full(x, bad_blocks, n) for x in sp]
    res_l = []
    # 2nd to 5th try
    for i in range(4):
        fprint(fp[i])
        res = parse_input()
        res_l.append(clean_input(res, bad_blocks))
    # `res_l` has 4 lists, each has at most 15 strings of length of at most 15
    # `zip()` to have at most 15 blocks of lists of 4 strings
    res_z = list(zip(*res_l))
    # For each block, figure out the missing ones
    missing = []
    # For full-16 blocks
    for i in range(len(res_z)-1):
        # Each block has 4 strings; `zip()` to get numbers in base 2
        pres = [int(''.join(x), 2) for x in zip(*res_z[i])]
        missing += [str(bad_blocks[i][0]+j) for j in range(16)
                    if j not in pres]
    # For the remainder
    pres = [int(''.join(x), 2) for x in zip(*res_z[-1])]
    missing += [str(bad_blocks[-1][0]+j)
                for j in range(bad_blocks[-1][1]-bad_blocks[-1][0])
                if j not in pres]
    # Send result
    fprint(' '.join(missing))
    # Check judge response
    if parse_input() == '1':
        return
    sys.exit(99)


if __name__ == '__main__':
    main()
