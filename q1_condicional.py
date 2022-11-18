# entrada 12, 3, 3, 6
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a == (b + c + d) and b == c and c == b and d == (b + c)):
    print('S')
else:
    print('N')
