t=int(input())
for _ in range(t):
    s=input()
    one=s.count('1')
    n=len(s)
    zero=n-one
    for i in s:
        if i=='0' and one>0:
            one-=1
        elif i=='1' and zero>0:
            zero-=1
        else:
            break
    print(zero+one)