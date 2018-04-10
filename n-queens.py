N = 10
queens = bytearray([0]*N)
row    = bytearray([1]*N)
diag1  = bytearray([1]*(2*N-1))
diag2  = bytearray([1]*(2*N-1))

def next_queen(n, pos, d1, d2):
    row[pos]  = 0
    diag1[d1] = 0
    diag2[d2] = 0
    solutions = move_queen(n+1)
    row[pos]  = 1
    diag1[d1] = 1
    diag2[d2] = 1

    return solutions
                
def move_queen(n):
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
                solutions += next_queen(n, pos, d1, d2)

        pos += 1
    return solutions


solutions = 0
pos = 0
while pos < N/2:
    queens[0] = pos
    solutions += next_queen(0, pos, pos, pos+3)
    pos += 1

print(solutions*2)
