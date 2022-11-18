l1 = []
l2 = []
l3 = 0

for i in range(5):
    v1 = int(input())
    l1.append(v1)
   
for i in range(5):
    v2 = int(input())
    l2.append(v2)
 
for i in range(len(l1)):
    for x in range(len(l2)):
        l3 = l1+l2
        l3[::2] = l1
        l3[1::2] = l2
        l3.sort()
print(' '.join(map(str,l3)))

    
    
