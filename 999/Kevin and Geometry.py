'''t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    if n>=4 and l[n-1]==l[n-2]:
        print(l[n-1],l[n-2],l[n-3],l[n-4])
    else:
        flag=False
        a=0
        b=0
        c=0
        for i in range(n-1):
            if l[i]==l[i+1]:
                c=l[i]
                for j in range(i+2,n-1):
                    a=l[j]
                    b=l[j+1]
                    if (2*c)>abs(b-a):
                        flag=True
                        break
                if flag:
                    break
        if flag:
            print(c,c,a,b)
        else:
            print(-1)'''
            

            
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split))
    l=sorted(l)
    c=0
    a=0
    b=0
    for i in range(n-1,0,-1):
        if l[i]==l[i-1]:
            c=2*l[i]
            del l[i]
            del l[i-1]
            break
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1])<c:
            print(c//2,c//2,l[i],l[i+1])
            break
    else:
        print(-1)
        