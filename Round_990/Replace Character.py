t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    z=set(s)
    if z==1:
        print(s)
    else:
        s=list(s)
        for j in range(n-1):
            if s[j]!=s[j+1]:
                s[j+1]=s[j]
                break
        print(''.join(s))