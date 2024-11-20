def check(mid):
    l=[]
    r=[]
    for i,j in enumerate(h):
        req=(j+mid-1)//mid
        if req>m:
            continue
        interval=m-req
        l.append(x[i]-interval)
        r.append(x[i]+interval+1)
    l.sort()
    r.sort()
    i=0
    cnt=0
    for j in l:
        cur=j
        cnt+=1
        while i<len(r) and cur>=r[i]:
            cnt-=1
            i+=1
        if cnt>=k:
            return True
    return False
 
def solve():
    global n,m,k,h,x
    n,m,k=map(int,input().split())
    h=list(map(int,input().split()))
    x=list(map(int,input().split()))
    low=1
    high=10**9
    while high-low>1:
        mid=(low+high)//2
        if check(mid):
            high=mid
        else:
            low=mid+1
    if check(low):
        print(low)
    elif check(high):
        print(high)
    else:
        print(-1)
        
for _ in range(int(input())):
    solve()