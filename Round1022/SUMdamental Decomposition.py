t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    if n==1:
        if x==0:
            print(-1)
        else:
            print(x)
    elif n==2:
        if x==1:
            print(5)
        elif x==0:
            print(2)
        else:
            print(x)
    
    else:
        print(x+n-1)      