t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    arr=[0]*n
    c=0
    for i in range(n-1,-1,-1):
        arr[i]=c
        if s[i]=='1':
            c+=1
        else:
            c-=1
    arr.sort()
    start=0
    res=-1
    
    for i in range(n-1,-1,-1):
        start+=arr[i]
        if start>=k:
            res=n-i+1
            break
    print(res)