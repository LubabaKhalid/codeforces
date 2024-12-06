t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s1=s2=0
    for i in range(n):
        if i%2==0:
            s2+=a[i]
        else:
            s1+=a[i]
    if s1%(n//2) or s2%((n+1)//2):
        print("NO")
    elif s1*((n+1)//2)==s2*(n//2):
        print("YES")
    else:
        print("NO")