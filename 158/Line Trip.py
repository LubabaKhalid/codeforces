t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split())) #length n
    a=[0]+a+[x]
    maxi=0
    for i in range(1,len(a)):
        maxi=max(maxi,a[i]-a[i-1])
    z=(x-a[-2])*2
    if maxi>z:
        print(maxi)
    else:
        print(z)