t=int(input())
for _ in range(t):
    n=int(input())
    a=set(list(map(int,input().split())))
    b=set(list(map(int,input().split())))
    if len(a)+len(b)>3:
        print("YES")
    else:
        print("NO")