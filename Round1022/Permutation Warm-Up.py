t = int(input())
for _ in range(t):
    n = int(input())
    if n<15:
        print(n+(n//2-1)*(n//2-1))
    else:
        print(n + (n//2-1)*(n//2))
