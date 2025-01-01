import math
t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    res=0
    if l%2!=0:
        res=res+math.ceil(l/2)
        left=res-1
        rigth=res+1
        while (left)>=r:
            left=math.ceil(left/2)
            res+=left
            left=left-1
        while (rigth+l)/2>=r:
            res=res+ math.ceil((rigth+l)/2)
            right=res+1
    print(res)