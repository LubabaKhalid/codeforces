m=int(input())
for _ in range(m):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    t=-1
    for i in range(n):
        s=1
        for j in range(n):
            if i!=j and abs(a[i]-a[j])%k==0:
                s=0
        if s==1:
            t=i+1
    if t==-1:
        print("NO")
    else:
        print("YES")
        print(t)