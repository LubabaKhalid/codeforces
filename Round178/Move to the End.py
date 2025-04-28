t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a_sorted = sorted(a, reverse=True)
    prefix=[]
    total=0
    for val in a_sorted:
        total+=val
        prefix.append(total)
    
    print(*prefix)
