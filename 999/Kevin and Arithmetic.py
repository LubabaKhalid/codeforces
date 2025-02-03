t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(n):
        if l[i]%2==0:
            s=s+1
    if s==n:
        print(s-1)
    else:
        print(s+1)