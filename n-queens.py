N = 4
dame = [0]*N
zeile = [0]*N
diag1 = [0]*(2*N-1)
diag2 = [0]*(2*N-1)

def setzedame(n):
    pos = 0
    while pos < N:
        d1=n+pos
        d2=pos-n+3
        if zeile[pos] == 0 and  diag1[d1] == 0 and diag2[d2] == 0 :
            dame[n] = pos
            if n == N-1 :
                print('solution:')
                print(dame)
            else:
                zeile[pos]=1
                diag1[d1] = 1
                diag2[d2]=1
                setzedame(n+1)
                zeile[pos]=0
                diag1[d1] = 0
                diag2[d2]=0

        pos = pos + 1

setzedame(0)
