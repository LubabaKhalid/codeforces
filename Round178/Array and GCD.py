import sys
import threading
from collections import Counter
from math import gcd

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        cnt = Counter(a)
        max_val = max(a)
        freq = [0] * (max_val + 2)
        for num in a:
            freq[num] += 1

        dp = [0] * (max_val + 2)
        for i in range(max_val, 1, -1):
            total = 0
            for j in range(i, max_val + 1, i):
                total += freq[j]
            dp[i]=total
            for j in range(2 * i, max_val + 1, i):
                dp[i]-=dp[j]
        max_keep=max(dp[2:]) if n>1 else 0
        print(n-max_keep)

threading.Thread(target=main).start()
