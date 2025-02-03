t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    c=0
    for i in range(n):
        s=s+l[i]
        if s%2==0:
            c=c+1
            while (s//2)%2==0:
                c=c+1
                s=s//2
    s1=0
    c1=0
    for i in range(n-1,-1,-1):
        s1=s1+l[i]
        if s1%2==0:
            c1=c1+1
            while (s1//2)%2==0:
                c1=c1+1
                s1=s1//2
    print(max(c,c1))