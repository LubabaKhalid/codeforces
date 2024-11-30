t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    arr=[]
    left=0
    right=n-1
    s=sorted(l)
    if s==l:
        print(0)
        continue
    else:
        for i in range(n):
            if s[i]!=l[i]:
                j=s.index(s[i])
                l[i],l[j]=l[j],l[i]
                arr.append([i,j])
                c=c+1
        
        print(c)
        for x,y in arr:
            print(x+1,y+1)
    
  
                
                