num=list(map(int,input().split()))
i=0
j=1
while i<len(num)-1:
    if num[i]==0:
        while j<len(num):
            if num[j]!=0:
                num[i],num[j]=num[j],num[i]
                break
            j=j+1
    i=i+1
print(num)