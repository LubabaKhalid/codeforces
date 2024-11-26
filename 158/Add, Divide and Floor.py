t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=min(a)
    M=max(a)
    c=0
    while m!=M:
        M=(M+m)//2
        c+=1
    print(c)
    if 0<c<=n:
        for i in range(c):
            print(m,end=" ")
        print()