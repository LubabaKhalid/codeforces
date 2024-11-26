t = int(input())  # Number of test cases
for _ in range(t):
    s = input()  # The binary string
    one = s.count('1')  # Count of '1's in the string
    n = len(s)  # Length of the string
    zero = n - one  # Count of '0's in the string
    
    # Iterate through the string to find the point where excess '1's or '0's need to be deleted
    for i in range(n):
        if s[i] == '0':
            zero -= 1  # Reduce the count of '0's as we encounter them
        else:
            one -= 1  # Reduce the count of '1's as we encounter them
        
        # If either '1's or '0's count becomes negative, it means we have to delete the remaining characters
        if zero < 0 or one < 0:
            print(n - i)  # The cost will be the remaining characters after index 'i'
            break
    else:
        print(0)  # If the loop completes without breaking, it means the string is already good
