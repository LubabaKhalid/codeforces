def maze(i,j,s,n):
    if j==0:
        if (j+1)<=(n-1) and mat[i][j+1]==1:
            s=s+"R"
            return s,False
        elif (i+1)<=(n-1) and mat[i+1][j]==1:
            s=s+"D"
            return s,False
        else:
            return [],True
    if j==(n-1):
        pass
        
mat= [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
n=len(mat)
s=""
if mat[0][0]==0:
    print("[]")
elif mat[n-1][n-1]==0:
    print("[]")
else:
    i=0
    flag=False
    while i<n:
        for j in range(n):
            s,flag=maze(i,j,s,n)
        i=i+1