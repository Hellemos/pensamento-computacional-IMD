import math

a = int(input())
b = int(input())
c = int(input())

if(math.fabs(b - c) < a and b + c > a):
    print('possível')
elif(math.fabs(a - c) < b and a + c > b):
    print('possível')
elif(math.fabs(a - b) < c and a + b > c):
    print('possível')
else:
    print('impossível')


