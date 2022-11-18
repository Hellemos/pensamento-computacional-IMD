votos = []
so = {'1':'Windows', '2':'Unix', '3':'Linux', '4':'Netware', '5':'Mac OS', '6':'Outro'}
v = -1
count_w = 0
count_u = 0
count_l = 0
count_n = 0
count_m = 0
count_o = 0

while v != 0:
    v = int(input())
    votos.append(v)

for i in range(len(votos)):
    if(votos[i] == 1):
        count_w += 1
    elif(votos[i] == 2):
        count_u += 1
    elif(votos[i] == 3):
        count_l += 1
    elif(votos[i] == 4):
        count_n += 1
    elif(votos[i] == 5):
        count_m += 1
    elif(votos[i] == 6):
        count_o += 1
print('Windows',count_w)
print('Unix',count_u) 
print('Linux',count_l) 
print('Netware',count_n) 
print('Mac OS',count_m)
print('Outro',count_o)
print('Total:',len(votos),'votos')
        
