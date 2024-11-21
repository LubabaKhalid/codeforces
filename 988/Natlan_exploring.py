import math
n= int(input())
l=list(map(int,input().split()))
m=998244353
dp=[0]*n
dp[0]=1
for i in range(n):
    for j in range(n):
        if i<j and math.gcd(l[i],l[j])!=1:
            dp[j]=(dp[i]+dp[j])%m
print(dp[n-1])