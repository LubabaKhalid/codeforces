t=int(input())
for _ in range(t):
    n,a,b,c=map(int,input().split())
    if a==1 and b==1 and c==1:
        print(n)
    else:
        m=a+b+c
        y=n%m
        x=n//m
        c=0
        if y==0:
            print(x*3)
        else:
            if y<=a:
                c=c+1
                y=y-a
            if y<=b and y!=0:
                c=c+1
                y=y-b
            if y<=c and y!=0:
                c=c+1
            print(c+(x*3))        