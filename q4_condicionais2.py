cod = input()
p = int(input())
m = int(input())
g = int(input())

#camisas azuis
cpa = 10
cma = 7
cga = 5

#camisas verde
cpv = 12
cmv = 5
cgv = 4

if(cod == 'A'):
    result = cpa - p
    result1 = cma - m
    result2 = cga - g
    print('P(A):',result,'\nM(A):',result1,'\nG(A):',result2)
    print('P(V):',cpv,'\nM(V):',cmv,'\nG(V):',cgv)
elif(cod == 'V'):
    if(cmv < m):
        res = cpv - p
        res1 = cmv
        res2 = cgv - g
        print('P(A):',cpa,'\nM(A):',cma,'\nG(A):',cga)
        print('P(V):',res,'\nM(V):',cmv,'- \'''Quantidade não disponível.','\nG(V):',cgv)
    
        
    
