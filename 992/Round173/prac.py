from itertools import combinations

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Size of the list (not really used directly)
    a = list(map(int, input().split()))  # List of integers
    b=a
    # Generate combinations for all possible sizes (1 to n)
    for r in range(1, n + 1):
        for comb in combinations(a, r):
            b.append(sum(comb))
    print(sorted(set(b)))
