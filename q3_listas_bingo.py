n = int(input())
seq1 = []
seq2 = []
result = []

for i in range(int(n)):
    v1 = int(input())
    seq1.append(v1)

m = int(input())  
for i in range(int(m)):
    v2 = int(input())
    seq2.append(v2)

for x in range(len(seq1)):
    for y in range(len(seq2)):
        if(seq1[x] == seq2[y]):
            result.append(seq2[y])
          
if(len(seq1) == len(result)):
    print('BINGO')
else:
    print('INCOMPLETO')




            
    
