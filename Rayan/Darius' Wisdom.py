t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    b=l[:]
    b.sort()
    arr=[]
    ans=0
    cnt=0
    r=n-1
    if b==l:
        print(0)
        continue
    else:
        for i in range(n):
            d=l[i]-b[i]
            for j in range(d):
                for k in range(r,i,-1):
                    if l[i]-l[k]==1:
                        ans+=1
                        cnt+=1
                        arr.append([i,k])
                        l[i],l[k]=l[k],l[i]
                        if l[r]==b[r]:
                            r-=1
                        break
        
        print(ans)
        for x,y in arr:
            print(x+1,y+1)
    
  
                
                