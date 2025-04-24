t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    x=set(s)
    if n==1:
        print("NO")
    elif len(x)==1:
        print("NO")
    elif k==0:
        if s[0]<s[-1]:
            print("YES")
        else:
            print("NO")
    elif len(x)>2 and k>0:
        print("YES")
    else:
        print("NO")
    
    
        
        