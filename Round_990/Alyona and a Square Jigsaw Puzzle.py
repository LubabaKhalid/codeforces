import math
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    c=0
    for j in a:
        s+=j
        if math.sqrt(s)%2==1:
            c=c+1
    print(c)