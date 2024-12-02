t=int(input())
inf=10**7
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    ans=inf
    s=0
    for i in range(n):
        s+=a[i]
        if s<=k:
             ans=min(ans,k-s)
    print(ans)
