t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    if n==x:
        for i in range(n):
            print(i,end=' ')
        print()
    elif x!=0:
        for i in range(n):
            if i!=x:
                print(i,end=' ')
        print(x)
    elif x==0:
        for i in range(1,n):
            print(i,end=' ')
        print(x)
    