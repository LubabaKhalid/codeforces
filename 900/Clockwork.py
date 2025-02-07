t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if a[i]>(2*max(i,(n-1)-i)):
            c=c+1
        else:
            c=0
    if c==n:
        print("YES")
    else:
        print("NO")