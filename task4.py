#Напишите программу, которая будет преобразовывать десятичное число в двоичное.


a = int(input('Введите число '))
array = []
while a != 0:
    array.append(a % 2)
    a = int((a - a % 2) / 2)
for i in range(len(array)-1, -1, -1):
    print(array[i], sep='', end = '')
    
