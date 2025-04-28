t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    for i in range(n-1,-1,-1):
        s[n-i]=s[n-i-1]+a[i]
    
    res=[0]*n

    for k in range(1, n + 1):
        max_sum = 0
        for i in range(n):
            
            if k <= n:
               
                temp = a[:i]+a[i+1:]+[a[i]]
                sum_k = sum(temp[-k:])
                max_sum = max(max_sum, sum_k)
        res[k-1]=max_sum

    print(*res)
