t=int(input())
for _ in range(t):
    n=input()
    s=len(n)
    while(n[-1]=='0'):
        n=n[:-1]
    print(s-1-n.count('0'))
    
    