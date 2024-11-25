import heapq
def fun():
    n,m,l=map(int,input().split())
    hurdle=[]
    power=[]
    heap=[]
    for j in range(0,n):
        hs,he=map(int,input().split())
        hurdle.append(hs,he)
    for j in range(m):
        s,p=map(int,input().split())
        power.append(s,p)
    j=0
    count=0
    k=1
    for i in range(n):
        s,e=hurdle[i]
        while j<m and power[j][0]<s:
            heapq.heappush(heap,-power[j][1])
            j+=1
        while k<(e-s+2) and heap:
            k=k-heapq.heappop(heap)
            count+=1
        if k<(e-s+2):
            print(-1)
            return 
    print(count)
            
        
        
    
t=int(input())
for i in range(t):
    fun()
            
        
            
    
    
    