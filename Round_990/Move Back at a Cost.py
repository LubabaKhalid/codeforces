t=int(input())  
for _ in range(t):
    n=int(input())  
    a=list(map(int,input().split()))  
    result=[]
    for i in range(n):
        if i<n-1 and a[i]>a[i+1]:
            a[i]+=1
            result.append(a[i])
        else:
            result.append(a[i])
    result.sort()
    print(*result)