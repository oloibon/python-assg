x = int(input('Enter no... '))
 
y3 = 0
y1 = 1
y2 = 1

if (x == 0 or x == 1):
    print('Ua number is a fibonacci number')
 
else:
    while y3 < x:
        y3 = f1 + f2
        y2 = f1
        y1 = f3
    if y3 == x:
        print('Ua number is a fibonacci number')
    else:
        print('Ua number is not a fibonacci number')
