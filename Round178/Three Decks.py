t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    s=c-b
    x=b-a
    y=s-x
    z=y//3
    if (c-b)==(b-a):
        print("YES")
    elif y>0 and z*3==y:
        print("YES")
    else:
        print("NO")