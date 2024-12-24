def solve_case(l, r, G):
    # Calculate the range for x
    x_start = (l + G - 1) // G  # This is ceil(l / G)
    x_end = r // G              # This is floor(r / G)

    if x_start > x_end:
        return "-1 -1"  # No valid x in the range

    # We want to maximize |A - B|, so we take the smallest x and largest y
    x = x_start
    y = x_end

    A = G * x
    B = G * y

    return f"{A} {B}"

# Read number of test cases
t = int(input())
results = []
for _ in range(t):
    l, r, G = map(int, input().split())
    results.append(solve_case(l, r, G))

# Print all results
print("\n".join(results))