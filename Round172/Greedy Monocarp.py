t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    ans=0
    coins=0
    flag=False
    for i in range(n):
        if a[i]==k:
            flag=True
            break
        elif a[i]==k-1:
            flag=True
            ans=1
            break
    if flag:
        print(ans)
    else:
        for i in range(n):
            ans+=a[i]
            if ans==k:
                break
            elif ans>k:
                ans-=a[i]
        if ans<k:
            coins=k-ans
        print(coins)