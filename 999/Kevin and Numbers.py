t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    ln=list(map(int,input().split()))
    lm=list(map(int,input().split()))
    ln=sorted(ln)
    lm=sorted(lm)
    if n<m:
        print("No")
    elif n==m:
        c=0
        for i in range(n):
            if lm[i]==ln[i]:
                c=c+1
        if c==m:
            
            print("Yes")
        else:
            print("No")
    elif m==1:
        i=1
        flag=False
        for i in range(1,n):
            if abs(ln[i-1]-ln[i])<=1:
                ln[i]+=ln[i-1]
                if ln[i]==lm[0]:
                    flag=True
                    break
            if flag:
                break
        if i==n-1 and flag:
            print("Yes")
    else: #n>m
        j=0
        for i in range(1,n):
            if abs(ln[i]-ln[i-1])<=1 and (ln[i]+ln[i-1])==lm[j]:
                
                
                
        
            