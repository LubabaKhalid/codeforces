t=int(input())
for _ in range(t):
    n,a,b,c=map(int,input().split())
    
    m=a+b+c
    y=n%m
    x=n//m
    c=0
    if y==0:
        c=0
    elif y<=a:
        c=1
    elif y<=(a+b):
        c=2
    else:
        c=3
    print(x*3+c)
        