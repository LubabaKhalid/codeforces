t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.insert(0,0)
    dif=[0]*(n+1)
    dif[0]=1
    for i in range(1,n+1):
        if l[i]==l[i-1]:
            dif[i]+=dif[i-1]
        if i>1 and l[i]==l[i-2]+1:
            dif[i]+=dif[i-2]
        dif[i]=dif[i]%998244353
    print((dif[-1]+dif[-2])%998244353)