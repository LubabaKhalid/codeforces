t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans+=a[i]
        if ans==k:
            break
        elif ans>k:
            ans=ans-a[i]
    print(k-ans)