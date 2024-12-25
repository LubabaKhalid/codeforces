mat= [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
n=len(mat)
print(n)
if mat[0][0]==0:
    print("[]")
elif mat[n-1][n-1]==0:
    print("[]")
else:
    print("OK")