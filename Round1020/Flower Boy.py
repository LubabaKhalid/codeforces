def can_collect(a, b, k=None):
    flowers = a[:]
    if k is not None:
        flowers.append(k)
    flowers.sort()
    b.sort()
    i=0  
    j=0  
    while i<len(flowers) and j<len(b):
        if flowers[i]>=b[j]:
            j+=1
        i+=1
    return j==len(b)
t = int(input())
for _ in range(t):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    if a==b[::-1]:
        print(-1)
    else:
        if can_collect(a, b):
            print(0)
            continue
        left=1
        right=int(1e9)
        ans=-1

        while left<=right:
            mid=(left + right)//2
            if can_collect(a,b,mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1

        print(ans)
