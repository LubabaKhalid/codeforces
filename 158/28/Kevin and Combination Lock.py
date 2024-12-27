t=int(input())
for i in range(t):
    x=int(input())
    x=x%33
    if x==0:
        print("YES")
    else:
        print("NO")