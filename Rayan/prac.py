t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())  # number of columns
    a = list(map(int, input().split()))  # the initial array of inscriptions
    
    moves = []  # List to store the moves
    # Try to sort the array by making valid moves
    for i in range(n - 1):
        while a[i] > a[i + 1]:
            # Swap inscriptions between column i and i+1
            a[i], a[i + 1] = a[i + 1], a[i]
            moves.append((i + 1, i + 2))  # Store the 1-based indices of the move
    
    print(len(moves))  # Output the number of moves
    for move in moves:
        print(*move)  # Output each move (1-based indices)
