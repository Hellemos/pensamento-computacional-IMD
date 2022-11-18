a = int(input())
b = int(input())
c = int(input())
if (a < b and a > c or a > b and a < c):
    print('A')
elif (b < c and b > a or b > c and b < a):
    print('B')
elif (c < a and c > b or c > a and c < b):
    print('C')
else:
    print('N')
  
    


