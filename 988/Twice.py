from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if n==1:
        print(0)
    else:
        freq = Counter(l)
        score = 0
        for count in freq.values():
            score += count // 2  
        print(score)