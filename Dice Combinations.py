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
    '''
    no of coins
    '''
    MOD = 10 ** 9 + 7
    prev = [0] * 7   
    prev[0] = 1      
    
    for i in range(1, n + 1):
        val = 0
        for j in range(1, 7):
            if i - j >= 0:
                val = (val + prev[(i - j) % 7]) % MOD
        prev[i % 7] = val
    
    print(prev[n % 7])
    
def run():
    cases = 1
    for _ in range(cases):
        solve()
 
if __name__ == "__main__":
