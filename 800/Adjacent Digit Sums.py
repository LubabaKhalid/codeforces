t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    d=x+1-y
    if d>=0 and d%9==0:
        print("YES")
    else:
        print("NO")