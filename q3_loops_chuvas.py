dias = int(input())
count_casa_A = 0
count_casa_B = 0

#Casa A
for i in range(int(dias)):
    val = int(input())
    count_casa_A += val

#Casa B
for i in range(int(dias)):
    val = int(input())
    count_casa_B += val

if(count_casa_A > count_casa_B):
    print('CASA A')
elif(count_casa_A < count_casa_B):
    print('CASA B')
else:
    print('IGUAL')


