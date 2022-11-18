n = int(input())
media = 0
soma_pont = 0
pont = []
for i in range(int(n)):
    val = int(input())
    pont.append(val)
for i in pont:
    soma_pont += i
    media = soma_pont // n
for i in range(len(pont)):
    if(pont[i] > media):
        print(pont[i])
    elif(pont[i] == media):
        print('-')
        break
  
