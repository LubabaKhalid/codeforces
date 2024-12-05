t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=sum(a)
    if ans%n==0:
        print("YES")
    else:
        print("NO")