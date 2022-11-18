import datetime

ano = int(input())
date = datetime.date.today()
year = date.strftime("%Y")

idade = int(year) - ano

if(idade >= 16 and idade >= 18):
    print(idade, 'anos')
    print('Pode votar e dirigir')
elif(idade >= 16 and idade < 18):
    print(idade)
    print('Pode votar e não pode dirigir')
else:
    print(idade)
    print('Não pode votar e não pode dirigir')

