t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    h=list(map(int,input().split())) #n is length
    x=list(map(int,input().split())) #n is length
    damage=[]
    for j in range(n):
        totaldamage=0
        for k in range(n):
            dist=abs(x[j]-x[k])
            if dist<m:
                d=max(0,m - dist)
                totaldamage=totaldamage+d
        
    if totaldamage>=h[i]:
        damage.append(h[i])
    print(damage)