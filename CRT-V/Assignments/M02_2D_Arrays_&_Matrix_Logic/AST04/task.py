def diagonalSort(mat):
    m=len(mat)
    n=len(mat[0])

    for c in range(n):
        d=[]
        i=0
        j=c
        while i<m and j<n:
            d.append(mat[i][j])
            i+=1
            j+=1
        d.sort()
        i=0
        j=c
        k=0
        while i<m and j<n:
            mat[i][j]=d[k]
            i+=1
            j+=1
            k+=1

    for r in range(1,m):
        d=[]
        i=r
        j=0
        while i<m and j<n:
            d.append(mat[i][j])
            i+=1
            j+=1
        d.sort()
        i=r
        j=0
        k=0
        while i<m and j<n:
            mat[i][j]=d[k]
            i+=1
            j+=1
            k+=1

    return mat


if __name__=='__main__':
    m,n=map(int,input().split())
    mat=[]
    for i in range(m):
        mat.append(list(map(int,input().split())))
    print(diagonalSort(mat))