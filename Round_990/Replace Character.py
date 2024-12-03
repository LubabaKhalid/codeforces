from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    count=Counter(s)
    mn=min(count.items(), key=lambda x:x[1])
    mx=max(count.items(), key=lambda x:x[1])
    if mn[0]!=mx[0]:
        for j in range(n):
            if mn[0]==s[j]:
                s[j]=mx[0]
                break
    elif n>1:
        for j in range(n-1):
            if s[j]!=s[j+1]:
                s[j+1]=s[j]
                break
        
    print(''.join(s))