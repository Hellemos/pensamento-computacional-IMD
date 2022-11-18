minimo = int(input())
maximo = int(input())
n = int(input())
result = []
for i in range(int(n)):
    val = int(input())
    if(val >= minimo and val <= maximo):
        result.append(val)
for i in result:
    print(i)

