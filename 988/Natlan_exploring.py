import math
m=998244353
n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[0]=1
for i in range(n):
    for j in range(i+1,n):
        
        if math.gcd(a[i],a[j])!=1:
            dp[j]=(dp[i]+dp[j])%m
print(dp[n-1])