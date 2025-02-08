t=int(input())
for _ in range(t):
    a,b,d,e=map(int,input().split())
    c=set([a+b,d-b,e-d])
    print(4-len(c))
    