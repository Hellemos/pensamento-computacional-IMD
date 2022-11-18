def verificaSeq(n):
    seq1 = []
    seq2 = []

    for i in range(int(n)):
        v1 = int(input())
        seq1.append(v1)

    m = int(input())
    for i in range(int(m)):
        v2 = int(input())
        seq2.append(v2)

    for i in range(len(seq2) - len(seq1)+1):
        for j in range(len(seq1)):
            if (seq2[i + j] != seq1[j]):
                return print ('N')
            else:
                return print('N')
        return print('S')
    return print('N')



n = int(input())
verificaSeq(n)





       
