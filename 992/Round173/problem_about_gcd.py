import math
t=int(input())
for _ in range(t):
    s=[]
    c=0
    l,r,g=map(int,input().split())
    
    if l%g==0:
        a=l
    else:
        a=(l//g+1)*g
    b=(r//g)*g
    if a<=b and math.gcd(a,b)==g:
        print(a,b)
    else:
        print(-1,-1)