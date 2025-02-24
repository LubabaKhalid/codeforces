t=int(input())
s=0
for _ in range(t):
    n,m=map(str,input().split())
    m=int(m)
    if n=="P":
        s=s+m
    elif n=="B":
        if s+1<=m:
            print("YES")
            s=0
        else:
            print("NO")
            s=s-m
            
            
        
        