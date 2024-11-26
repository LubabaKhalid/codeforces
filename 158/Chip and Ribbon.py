t=int(input())
for _ in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    teleports=0
    for i in range(1,n):
        if c[i]>c[i-1]:
            teleports+=(c[i]-c[i-1])
    print(teleports+c[0]-1)
    