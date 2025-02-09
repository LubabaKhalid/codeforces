t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    ans=4*m
    c=0
    input()
    for i in range(n-1):
        a,b=map(int,input().split())
        c=c+a+b
    print(ans+c*2)