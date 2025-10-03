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
    a = rl()
    res = inf
    def fun(sm1, sm2, i):
        nonlocal res
        if i >= n:
            res = min(res, abs(sm1 - sm2))
            return
        #take
        fun(sm1 + a[i], sm2, i + 1)
        #not
        fun(sm1, sm2 + a[i], i + 1)
    fun(0, 0, 0)
    print(res)
    
def run():
    cases = 1
    for _ in range(cases):
        solve()
 
if __name__ == "__main__":
    run()