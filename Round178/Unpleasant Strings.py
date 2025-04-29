n,k=map(int,input().split())
s=input()
q=int(input())
for _ in range(q):
    r=input()
    m=len(r)
    c=0
    j=0
    jc=0
    flag=False
    for i in range(n):
        if r==s[i:i+m]:
            c=c+1
        elif r[j]==s[i]:
            jc+=1
            j+=1
            if jc==m:
                print(1)
                flag=True
                break
    if not flag:
        print(c)
            
      