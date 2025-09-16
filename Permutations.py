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
    5 3 1 4 2
    '''
    if n == 1:
        print(1)
    
    elif n > 3:
        odd = []
        ev = []
        for i in range(n, 0, -1):
            if i % 2:
                odd.append(i)
            else:
                ev.append(i)
            
        res = odd + ev
        print(*res)
    else:
        print('NO SOLUTION')
        
            
            

def run():
    cases = 1
    for _ in range(cases):
        solve()

if __name__ == "__main__":
    run()
