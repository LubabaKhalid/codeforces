t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    a=sorted(a)
    flag=False
    for i in range(len(a)-1):
        alice=a[i]
        for j in range(i+1,len(a)):
            bob=a[j]
            if alice+bob==k:
                c=c+1
                del a[i]
                del a[j]
                flag=True
                break
        if not flag:
            del a[i]
            del a[i+1]
    print(c)