t=int(input())
for _ in range(t):
    n=int(input())
    x=[]
    for i in range(n):
        r=list(map(int,input().split()))
        x.append(r)
    
    ans=[]
    for i in range(n):
        for j in range(n):
            if x[i][j] not in ans:
                ans.append(x[i][j])
    y=n*2
    for i in range(1,y+1):
        if i not in ans:
            print(i,end=' ')
            break
    for i in range(n*2-1):
        print(ans[i],end=' ')
    print()
             
        
            