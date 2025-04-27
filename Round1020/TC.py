t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    if '0' in s:
        print(n+s.count('1'))
    elif n==1 and s[0]=='1':
            print(0)
    else:
        print((n-1)*n)
        