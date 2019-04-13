#!/usr/bin/env python3
from math import gcd


def main():
    # `t`: Number of test cases
    t = int(input())
    for i in range(1, t+1):
        # `n` and `l` are ignored
        input()
        # `nums`: List of numbers
        nums = [int(x) for x in input().split()]
        # Move any preceding duplicates to `nums_removed` for later
        nums_copy = nums[:]
        while nums[0] == nums[1]:
            nums = nums[1:]
        nums_removed = nums_copy[:len(nums_copy)-len(nums)][::-1]
        # Use `gcd(a, b)` on first and second of what's left
        a, b = nums[:2]
        p = gcd(a, b)
        q = a // p
        # Initiate factored
        factored = [q, p, b // p]
        p = b // p
        # Add following primes
        for x in nums[2:]:
            p = x // p
            factored.append(p)
        # Add preceding primes (from `nums_removed`)
        # `reverse-append-reverse` instead of `insert` due to time complexity
        factored.reverse()
        for x in nums_removed:
            q = x // q
            factored.append(q)
        factored.reverse()
        # Get sorted list of unique primes
        primes = sorted(list(set(factored)))
        # I have a sense how fast this should run, so this is a kinda cheating
        # way of knowing that I got an error here, as `assert` would just give
        # an 'RE', which can happen elsewhere as well
        if len(primes) != 26:
            while(True):
                print(1)
        # Decoding dictionary
        dic = {primes[i]: chr(i+65) for i in range(26)}
        # Decode
        result = ''.join([dic[x] for x in factored])
        print('Case #{0}: {1}'.format(i, result))


if __name__ == '__main__':
    main()
