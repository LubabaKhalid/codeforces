t=int(input())
for _ in range(t):
    s=input()
    c=0
    n=len(s)
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            n=1
    print(n)
