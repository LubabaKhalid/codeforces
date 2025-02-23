t=int(input())
for _ in range(t):
    s=input()
    a=int(s[0])
    b=int(s[2])
    op=s[1]
    if op=="<" and a<b:
        print(s)
    elif op==">" and a>b:
        print(s)
    elif op=="=" and a==b:
        print(s)
    elif op=="<" and a>b:
        s=s[0]+'>'+s[2]
        print(s)
    elif op==">" and a<b:
        s=s[0]+'<'+s[2]
        print(s)
    elif op=="=" and a!=b:
        s=s[2]+s[1]+s[2]
        print(s)
    elif (op=="<" or op==">") and a==b:
        s=s[0]+'='+s[2]
        print(s)
    
        