t=int(input())
for i in range(t):
    n=int(input())
    count=0
    l=list(map(int,input().split()))
    if n==2:
        if l[0]>l[1]:
            print("1\nDR")
        else:
            print("0")
            continue
    print(n*2)
    for j in range(n*2):
        for k in range(2,n,2):
            x=(j+k-1)%n
            y=(j+k)%n
            if (l[x]<l[y]) ^ (x<y):
                print("DDRR",end='')
                l[x],l[y]=l[y],l[x]
            else:
                print("DRDR",end='')
        if n%2==0:
            print("DR",end='')
        print()