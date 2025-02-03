t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    flag=False
    a=0
    b=0
    c=0
    for i in range(n-1):
        if l[i]==l[i+1]:
            c=2*l[i]
            for j in range(i+1,n-1):
                a=l[j]
                b=l[j+1]
                if c>abs(b-a):
                    flag=True
                    break
            if flag:
                break
    if flag:
        print(c//2,c//2,a,b)
    else:
        print(-1)
        