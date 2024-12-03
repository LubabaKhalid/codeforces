from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=Counter(s)
    print(count)