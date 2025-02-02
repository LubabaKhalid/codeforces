import math
t=int(input())
for _ in range(t):
    s=[]
    c=0
    l,r,g=map(int,input().split())
    for i in range(l,r+1):
        if i%g==0:
            s.append(i)
            c=c+1
            if c==2:
                break
            
    if c==2:
        m=math.gcd(s[0],s[1])
        if m==g:
            print(s[0],s[1])
        else:
            print(-1,-1)
    elif c==1:
        if s[0]==g:
            print(s[0],s[0])
        else:
            print(-1,-1)
    else:
        print(-1,-1)
    
            
