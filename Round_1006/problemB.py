t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    c=0
    C=0
    for i in range(n):
        if s[i]=='-':
            c=c+1
        elif s[i]=="_":
            C=C+1
    m=c//2
    if m*2==c:
        print(m*m*C)
    else:
        print((m+1)*m*C)