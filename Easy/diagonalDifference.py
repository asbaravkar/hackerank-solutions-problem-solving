def diagonalDifference(mat):
    n=len(mat)
    s1,s2=0,0
    for i in range(len(mat)):
        # [ [1 3 4],
        #   [1 2 3],
        #   [3 4 5] ]
        s1+=mat[i][i]
        s2+=mat[n-1-i][i]
    if s2>s1:
        return s2-s1
    else:
        return s1-s2

n=int(input())
mat=[]
for i in range(n):
    temp=[int(i) for i in input().split()]
    mat.append(temp)
print(diagonalDifference(mat))
