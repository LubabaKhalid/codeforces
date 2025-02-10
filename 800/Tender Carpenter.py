t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n):
        if (min(a[i-1],a[i])*2)>max(a[i-1],a[i]):
            print("Yes")
            break
    else:
        print("No")