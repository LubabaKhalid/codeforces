def solve():
    t=int(input())  
    for _ in range(t):
        n=int(input())  
        cnt=[0]*(n+1)          
        a_list=list(map(int,input().split()))
        
        for a in a_list:
            cnt[a]+=1
        
        c=0  
        ans=0  
        
        for i in range(1,n+1):
            if cnt[i]==0:
                continue
            if cnt[i]==1:
                c+=1
            else:
                ans+=1
        
        ans+=(c+1)//2*2  
        print(ans)
solve()
