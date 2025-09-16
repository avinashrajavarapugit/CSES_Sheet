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
    y, x = rm()
    '''
    '''
    n = max(x, y)
    if n % 2 == 0:
        if y == n:
            print(n * n - x + 1)
        else:
            print((n - 1) * (n - 1) + y)
    else:
        if x == n:
            print(n * n - y + 1)
        else:
            print((n - 1) * (n - 1) + x)
        

def run():
    cases = ri()
    for _ in range(cases):
        solve()

if __name__ == "__main__":
    run()
