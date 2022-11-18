jog1 = input()
jog2 = input()

if(jog1 == 'pedra' and jog2 == 'papel'):
    print('Jogador 2 venceu')
elif (jog1 == 'papel' and jog2 == 'pedra'):
    print('Jogador 1 venceu')
elif(jog1 == 'tesoura' and jog2 == 'papel'):
    print('Jogador 1 venceu')
elif(jog1 == 'papel' and jog2 == 'tesoura'):
    print('Jogador 2 venceu')
elif(jog1 == 'pedra' and jog2 == 'tesoura'):
    print('Jogador 1 venceu')
elif(jog1 == 'tesoura' and jog2 == 'pedra'):
    print('Jogador 2 venceu')
else:
    print('empate')
