def main():
    t=int(input())  
    for _ in range(t):
        n,k=map(int,input().split()) 
        base = list(range(1,n+1)) 
        if k==1 and n>1:
            print("NO")
        elif k > n:
            print("NO")
        elif k==2:
            print("YES")
            print(" ".join(map(str, base))) 
            print(" ".join(map(str, base[::-1])))
        elif n==k:
            print("YES")
             
            for i in range(k):
                perm=base[i:]+base[:i]
                print(" ".join(map(str,perm)))
        else:
            print("NO")
main()
