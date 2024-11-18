def fun(l,n):
    for j in range(1,n//2+2):
        if n%j==0:
            z=n//j
            if j in l and z in l:
                return j,z
    return -1,-1
t=int(input())
for i in range(t):
    k=int(input())
    l=list(map(int,input().split()))
    n=len(l)-2
    j,z=fun(l,n)
    print(j,z)
                