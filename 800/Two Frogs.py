t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    if a<b and (b-a)==1 :
        if a-n>=0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")