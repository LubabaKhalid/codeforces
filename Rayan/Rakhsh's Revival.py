t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    s=input()
    z='0'*m
    c=0
    i=0
    while i <=(n-m):
        if s[i:i+m]==z:
            c+=1
            i+=k
        else:
            i+=1
    print(c)
        
        