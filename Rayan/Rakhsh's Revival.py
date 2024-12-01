t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    s=input()
    c=0
    i=0
    a=0
    while i <len(s):
        if s[i]!='0':
            c=0
        else:
            c+=1
        if c==m:
            c=0
            a+=1
            i=i+k-1
        i+=1   
    print(a)
        
        