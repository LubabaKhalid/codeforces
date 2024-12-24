import math
t=int(input())
for i in range(t):
    n=int(input())
    if n>3:
        print(math.ceil(n/4))
    else:
        print(n)