media = 0
soma = 0

n = int(input('##### Digite a quantidade de notas ##### \n'))

print('## Entre com as notas ##')
for i in range(0, n):
    v1 = int(input())
    soma += v1
    media = soma / n

print(f'Resultado da media: {media}')

