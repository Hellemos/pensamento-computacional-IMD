nome = []
nota = []
soma = 0
media = 0
l3 = []

for i in range(5):
    n = input()
    nome.append(n)
    v = int(input())
    nota.append(v)

 
for i in range(len(nota)):
    soma += nota[i]
    media = soma / (len(nota))

dicio = dict(zip(nome, nota))

print('Média:',media)

for k, v in dicio.items():
    if(v >= media):
        l3.append(k)
        max_key = max(dicio, key = dicio.get)
        
print('Acima da média:',','.join(l3))
print('Maior nota:',max_key)
   
    
    


