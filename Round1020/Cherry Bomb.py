t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    known_x=set()
    possible=True
    for i in range(n):
        if b[i]!=-1:
            known_x.add(a[i]+b[i])
    
    if len(known_x)>1:
        print(0)
        continue
    
    if len(known_x)==1:
        x=known_x.pop()
        valid=True
        for i in range(n):
            if b[i]==-1:
                y=x-a[i]
                if y<0 or y>k:
                    valid=False
                    break
        print(1 if valid else 0)
    else:
        low=max(a[i] for i in range(n) if a[i] <= k) 
        high=min(a[i] + k for i in range(n))         
        if high<low:
            print(0)
        else:
            print(high-low + 1)
