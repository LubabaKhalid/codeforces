global ans
def fun(r,cnt,i,l,b,ans):
    for k in range(r,i,-1):
        if l[i]-l[k]==1:
            ans+=1
            cnt+=1
            arr.append([i,k])
            l[i],l[k]=l[k],l[i]
            if l[r]==b[r]:
                r-=1
            break
    return ans
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
            j=0
            while j<d:
                ans=fun(r,cnt,i,l,b,ans)
                j+=1
        print(ans)
        for x,y in arr:
            print(x+1,y+1)
    
  
                
                