t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))  
    if l==sorted(l):
        print("YES")
        continue
    
    elif l>sorted(l) and k>=2:
        print("YES")
    else:
       print("NO")
             