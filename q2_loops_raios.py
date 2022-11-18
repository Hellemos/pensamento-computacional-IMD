d = int(input())
n = int(input())
count = 0
for i in range(int(n)):
    val = int(input())
    if(val <= d):
        count += 1
print(count)
