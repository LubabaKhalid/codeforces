def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of buttons
        a = list(map(int, input().split()))  # Weights of the buttons

        # To track the number of clones needed
        clones = 1  # At least one clone is always needed
        max_weight = a[0]  # Start with the first button weight

        for i in range(1, n):
            if a[i] > max_weight:
                max_weight = a[i]
            else:
                clones += 1
                max_weight = a[i]

        print(clones)

# Input reading and function call
solve()
