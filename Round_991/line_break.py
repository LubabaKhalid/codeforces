def solve():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # Read the number of words and the max length of the first strip
        words = [input().strip() for _ in range(n)]  # Read the words
        current_length = 0
        x = 0
        
        # Try to add words to the first strip until the length exceeds m
        for word in words:
            current_length += len(word)  # Add the length of the current word
            if current_length > m:  # If the length exceeds the capacity of the strip
                break
            x += 1  # Increment x, meaning the word fits on the first strip
        
        print(x)  # Output the result for this test case

# Run the solution
solve()
