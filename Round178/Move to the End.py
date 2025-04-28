t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=len(set(a))
    if s==1:
        for i in range(1,n+1):
            print(a[0]*i,end=' ')
        print()
    elif s==2:
        if a[0]>a[1]:
            print(a[0],a[0]+a[1])
        else:
            print(a[1],a[1]+a[0])
    else:
        c=0
        x=0
        y=0
        if n%2!=0:
            y=n//2
            x=y+1
        else:
            y=n//2
            x=y
        r=sorted(a[x-1:n])
        l=sorted(a[0:y])
        a=l+r
        for i in range(n-1,-1,-1):
            c=c+a[i]
            print(c,end=' ')
            
            
            
                
            
        
            