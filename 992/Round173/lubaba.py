import math

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    divisors = []
    
    if n == 9:
        m = (math.factorial(n) // 4096)
        d = str(d)
        d = int(d) * m
        for odd_digit in [1, 3, 5, 7, 9]:
            if d % odd_digit == 0:
                divisors.append(odd_digit)
     
    elif n > 7:
        m = math.factorial(n)
        d = int(d) * (m // 128)
        for odd_digit in [1, 3, 5, 7, 9]:
            if d % odd_digit == 0:
                divisors.append(odd_digit)
       
    elif n<=7 and n>5:
        m=math.factorial(n)
        d=str(d)
        d=d*(m//8)
        e=int(d)
        for odd_digit in [1, 3, 5, 7, 9]:
            if e%odd_digit==0:
                divisors.append(odd_digit)
                
    else:
        m = math.factorial(n)
        d = int(d)
        for odd_digit in [1, 3, 5, 7, 9]:
            if d % odd_digit == 0:
                divisors.append(odd_digit)
    for j in divisors:
        print(j,end=' ')
    print()