t=int(input())  
for _ in range(t):
    n,m= map(int,input().split())  
    words=[input().strip() for _ in range(n)]  
    current_length=0
    x=0
    for word in words:
        current_length+=len(word) 
        if current_length>m:  
            break
        x+=1  
        
    print(x) 


