t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(input())
    x=set(s)
    if len(x)==1 or (k==0 and s>=s[::-1]):
        print("NO")
    else:
        print("YES")
    
        
        