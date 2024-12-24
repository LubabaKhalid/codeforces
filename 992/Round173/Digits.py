def find_divisors(d):
    divisors = []
    for odd_digit in [1, 3, 5, 7, 9]:
        if d % odd_digit == 0:
            divisors.append(odd_digit)
    return divisors

# Reading number of test cases
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    divisors = find_divisors(d)
    print(" ".join(map(str, divisors)))
