t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=False
    s=0
    for i in range(n):
        s=abs(s-a[i])
    if s>1:
        print("YES")
    else:
        print("NO")