t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=a
    b.append(0)
    for i in range(n):
        for j in range(i+1,n):
            b.append(sum(a[i:j+1]))
  
    b=sorted(set(b))
    print(len(b))
    for i in b:
        print(i,end=" ")
    print()