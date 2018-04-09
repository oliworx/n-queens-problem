N = 9
queens = bytearray([0]*N)
row    = bytearray([1]*N)
diag1  = bytearray([1]*(2*N-1))
diag2  = bytearray([1]*(2*N-1))

def setzedame(n):
    solutions = 0
    pos = 0
    while pos < N:
        d1=n+pos
        d2=pos-n+3
        if row[pos] and diag1[d1] and diag2[d2] :
            queens[n] = pos
            if n == N-1 :
                solutions += 1
            else:
                row[pos]  = 0
                diag1[d1] = 0
                diag2[d2] = 0
                solutions += setzedame(n+1)
                row[pos]  = 1
                diag1[d1] = 1
                diag2[d2] = 1

        pos += 1
    return solutions
    
print(setzedame(0))
