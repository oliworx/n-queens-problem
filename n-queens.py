dame = [0,0,0,0]
zeile = [0,0,0,0]
diag1 = [0,0,0,0,0,0,0]
diag2 = [0,0,0,0,0,0,0]

def setzedame(n, dame, zeile, diag1, diag2):
    pos = 0
    while pos < 4:
        d1=n+pos
        d2=pos-n+3
        if zeile[pos] == 0 and  diag1[d1] == 0 and diag2[d2] == 0 :
            dame[n] = pos
            if n < 3 :
                zeile[pos]=1
                diag1[d1] = 1
                diag2[d2]=1
                setzedame(n+1, dame[:], zeile[:], diag1[:], diag2[:])
                zeile[pos]=0
                diag1[d1] = 0
                diag2[d2]=0
            else:
                print(dame)
        pos = pos + 1

setzedame(0, dame, zeile, diag1, diag2)
