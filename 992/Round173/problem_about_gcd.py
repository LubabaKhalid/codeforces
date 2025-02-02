import math
t=int(input())
for _ in range(t):
    flag=False
    l,r,g=map(int,input().split())
    a=l
    b=r
    while a%g!=0:
        a+=1
    while b%g!=0:
        b-=1
    while b!=a:
        if (math.gcd(a,b))==g:
            flag=True
            print(a,b)
            break
        b-=g
    if flag is False:
        if l<=g<=r:
            print(g,g)
        else:
            print(-1,-1)
    
    