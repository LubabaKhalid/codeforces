t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if n==1:
        print(a[0])
    else:
        s=0
        for i in range(n-1):
            if a[i]>b[i+1]:
                s=s+a[i]-b[i+1]
        s=s+a[n-1]
        print(s)
                
            
            