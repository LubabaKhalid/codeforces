def fun(x,y,s):
    for i in range(x+1):
        for j in range(y+1):
            if ((i*6)+(j*2)+s)%9==0:
                return "YES"
    return "NO"
def main():
    t=int(input())  
    for _ in range(t):
        n=input()
        x=n.count("2")
        y=n.count("3")
        l=[int(d) for d in n]
        s=sum(l)
        print(fun(x,y,s))
main()