t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if i==0 and a[i]!=0:
            c=c+1
        elif i!=0 and a[i-1]==0 and a[i]!=0:
            c=c+1
    print(min(c,2))