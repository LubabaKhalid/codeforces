def solve():
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read the inputs for each test case
        n, m, k = map(int, input().split())  # Number of enemies, max damage, enemies to defeat
        health = list(map(int, input().split()))  # Health of each enemy
        positions = list(map(int, input().split()))  # Positions of each enemy

        # Helper function to check if we can defeat at least `k` enemies in `attacks` attacks
        def can_defeat_with_x_attacks(x):
            damage = [0] * n  # List to store the damage each enemy receives
            # Compute the damage for each enemy when Xilonen stands at each position
            for i in range(n):
                for j in range(n):
                    dist = abs(positions[i] - positions[j])  # Calculate the distance between enemies
                    if dist < m:
                        damage[j] += max(0, m - dist) * x  # Add damage based on distance
            # Count how many enemies can be defeated
            defeated = sum(1 for i in range(n) if damage[i] >= health[i])
            return defeated >= k  # Return if we can defeat at least k enemies

        # Binary search for the minimum number of attacks
        low, high = 1, 10**9  # Lower and upper bounds for number of attacks
        result = -1

        while low <= high:
            mid = (low + high) // 2  # Middle point, representing the number of attacks
            if can_defeat_with_x_attacks(mid):
                result = mid
                high = mid - 1  # Try to find fewer attacks
            else:
                low = mid + 1  # Try more attacks
        
        # Output the result for this test case
        print(result)

solve()