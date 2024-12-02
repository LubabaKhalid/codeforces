t=int(input())
for i in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    m=set(c)
    if len(m)==1:
        print(1)
    elif len(m)==len(c):
        print(4)
    else:
        print(len(m)+1)