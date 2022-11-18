n = int(input())
maior = 0
temp = []
result = 0
for i in range(int(n)):
    val = int(input())
    temp.append(val)
for i in range(len(temp)):
    maior = max(temp)
    result = maior - temp[i]
    print(result)

