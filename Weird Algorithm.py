# src: Hi, I'm Avinash Rajavarapu

import sys
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from math import gcd, sqrt, ceil, floor, inf
from functools import lru_cache

def ri(): return int(input())
def rl(): return list(map(int, input().split()))
def rs(): return input().strip()
def rm(): return map(int, input().split())

def solve():
    n = ri()
    res = []
    res.append(n)
    while n != 1:
        if n % 2:
            n *= 3
            n += 1
        else:
            n //= 2
        res.append(n)
    print(*res)
            

def run():
    cases = 1
    for _ in range(cases):
        solve()

if __name__ == "__main__":
    run()
