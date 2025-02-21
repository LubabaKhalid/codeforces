t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    i=1
    j=n
    l=[]
    for x in range(n):
        if(x+1)%k==0:
            l.append(i)
            i=i+1
        else:
            l.append(j)
            j=j-1
    print(*l)