1856B - Good Arrays
def sol(num):
    if len(num)==1:
        return 'NO'
    one_c=0
    sum=0
    for n in num:
        if n==1:
            one_c+=1
        else:
            sum+=n
    if sum>=len(num):
        return "YES"
    return "NO"
        
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=sol(a)
    print(x)
