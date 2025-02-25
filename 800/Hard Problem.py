t=int(input())
for _ in range(t):
    m,a,b,c=map(int,input().split())
    s=0
    space1=0
    space2=0
    if m>=a:
        space1=m-a
        s=s+a
    elif m<a:
        s=s+m
        
    if m>=b:
        space2=m-b
        s=s+b
    elif m<b:
        s=s+m
    total=space1+space2
    if total!=0:
        if total>=c:
            s=s+c
        else:
            s=s+total
    print(s)
    