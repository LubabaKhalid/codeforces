def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [[] for _ in range(m + 1)]
    MX = (1 << 31) - 1

    for mask in range(1, 1 << m):
        x = MX
        for i in range(m):
            if mask & (1 << i):
                x &= b[i]
        c[bin(mask).count('1')].append(x)

    rem = []
    for x in a:
        for j in range(1, m + 1):
            y = x
            for z in c[j]:
                y = min(y, x & z)
            rem.append(x - y)
            x = y

    # Sort in descending order and remove k largest reductions
    rem.sort(reverse=True)
    print(sum(a) - sum(rem[:k]))

# Read number of test cases
t = int(input())
for _ in range(t):
    solve()
