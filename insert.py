a={2,4,9,20,23,28}
x=19
i=len(a)-1
while i>-1:
    if a[i]>x and i>0:
        a[i+1]=a[i]
a[i+1]=x
print(a)