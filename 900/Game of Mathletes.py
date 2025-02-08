t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    a=sorted(a)
    l=0
    r=len(a)-1
    while l<r:
        x=a[l]+a[r]
        if x==k:
            c=c+1
            l=l+1
            r=r-1
        elif x<k:
            l=l+1
        else:
            r=r-1
    print(c)