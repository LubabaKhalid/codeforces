t=int(input())
for _ in range(t):
    n=int(input())
    x=[]
    for i in range(n):
        r=list(map(int,input().split()))
        x.append(r)
    ans=x[0]
    for i in range(1,n):
        if x[i][-1] not in ans:
            ans.append(x[i][-1])
    y=n*2
    for i in range(1,y+1):
        if i not in ans:
            print(i,end=' ')
            break
    for i in range(n*2-1):
        print(ans[i],end=' ')
    print()
             
        
            