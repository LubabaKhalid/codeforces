t=int(input())
m=998244353
n=1000000
for _ in range(t):
    n=int(input())
    d=[0]*(n+1)
    s=[0]*(n+1)
    for i in range(3,n+1):
        y=i*(i-1)//2-1+d[i-1]  
        s[i]=(s[i-1]+y)%m
        d[i]=(d[i-1]+y*(i+1))%m
    print((n - 1 + s[n-1]) % m)