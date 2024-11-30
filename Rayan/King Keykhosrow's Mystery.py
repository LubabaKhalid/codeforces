import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    x=math.gcd(a,b)
    y=a//x
    z=b//x
    print(x*y*z)