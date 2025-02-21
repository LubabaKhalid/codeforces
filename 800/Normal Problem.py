t=int(input())
for _ in range(t):
    a=input()[::-1]
    mapping={'p':'q','q':'p','w':'w'}
    s="".join(mapping[i] for i in a)
    print(s)