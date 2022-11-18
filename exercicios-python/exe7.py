nome = 'FULANO'
novo_nome = ''
tam = len(nome)

i = tam
while i >= 0:
    print(nome)
    novo_nome = nome[:tam - 1]
    print(novo_nome)
    i -= 1
