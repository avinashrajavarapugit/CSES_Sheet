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
    # n, x = rm()
    # a = rl()
    
    '''
    no of coins
    '''
    # a = set(a)
    # dp = [float('inf')] * (x + 1)
    # dp[0] = 0
    # for j in a:
    #     for i in range(j, x + 1):
    #         dp[i] = min(dp[i], dp[i - j] + 1)
    
    # print(dp[x] if dp[x] != float('inf') else -1)
    n, x = rm()
    coins = list(set(rl()))
    visited = [False] * (x + 1)
    q = deque([(0, 0)])
    visited[0] = True
    
    while q:
        cur, steps = q.popleft()
        if cur == x:
            print(steps)
            return
        for c in coins:
            nxt = cur + c
            if nxt <= x and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, steps + 1))
    print(-1)
    
def run():
    cases = 1
    for _ in range(cases):
        solve()
 
if __name__ == "__main__":
    run()
