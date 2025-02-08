t=int(input())
for _ in range(t):
    s=input()
    c=0
    for i in range(len(s)):
        if s[i]=='1':
            c=c+1
    print(c)