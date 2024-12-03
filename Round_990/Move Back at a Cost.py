t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    while i<(n-1):
        if a[i]>a[i+1] and i+1!=n-1:
            a[i]=a[i]+1
            temp=a[i]
            for j in range(i,n-1):
                a[j]=a[j+1]
            a[n-1]=temp
            i=0
        elif a[i]>a[i+1] and i+1==n-1:
            a[i],a[i+1]=a[i+1],a[i]
            
        i=i+1
    for i in range(n):
        print(a[i],end=' ')  
                