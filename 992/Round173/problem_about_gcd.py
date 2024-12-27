def solve_case(l, r, G):
    # Calculate the smallest multiple of G >= l
    A = G * ((l + G - 1) // G)
    
    # Calculate the largest multiple of G <= r
    B = G * (r // G)
    
    # Check if A is within the range [l, r] and B is also within the range [l, r]
    if A > r or B < l:
        return "-1 -1"  # No valid A, B in the range

    # Return the result as a string formatted properly
    return f"{A} {B}"

# Read number of test cases
t = int(input())
results = []

# Process each test case
for _ in range(t):
    l, r, G = map(int, input().split())
    results.append(solve_case(l, r, G))

# Print all results, one per line
print("\n".join(results))
