t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    if n==1 and x==0:
        print(-1)
    else:
        a=bin(x)
        c=a.count('1')
        m=max(n-c,0)
        if (n-c)>0 and (n-c)%2==1:
            if x==0 or x==1:
                m+=3
            else:
                m+=1
        print(x+m)
            