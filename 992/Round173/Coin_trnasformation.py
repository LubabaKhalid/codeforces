def maxcoins(n):
    if n<=3:
        return 1
    count=0
    while n>3:
        n//=4
        count+=1
    return 2**count
t = int(input())
for _ in range(t):
    n=int(input())
    print(maxcoins(n))

