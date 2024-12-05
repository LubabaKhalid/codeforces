def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = input().strip()  # The number as a string
        
        # Calculate the sum of the digits
        digit_sum = sum(int(digit) for digit in n)
        
        # If the sum of digits is already divisible by 9, print "YES"
        if digit_sum % 9 == 0:
            print("YES")
        else:
            # Try squaring each digit and check if the new sum is divisible by 9
            flag = False
            for digit in n:
                digit = int(digit)
                
                # Only consider squaring digits 1, 2, 3 since they give valid results
                if digit in {1, 2, 3}:  
                    squared_digit = digit ** 2
                    if squared_digit < 10:  # Ensure the squared result is a single digit
                        new_sum = digit_sum - digit + squared_digit
                        if new_sum % 9 == 0:
                            flag = True
                            break
            
            # If any change was successful, print "YES", else print "NO"
            if flag:
                print("YES")
            else:
                print("NO")

# Call the main function to execute the logic
main()
