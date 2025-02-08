t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=n*m
    c=1
    n=0
    if n==1:
        print(m+1)
    else:
        for i in range(x):
            if c==m+1:
                n=i
                break
            c=c+1
        print(n+1)