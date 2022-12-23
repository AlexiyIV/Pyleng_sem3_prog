array = [int(i) for i in input('Введите элементы через пробел ').split()]
sum = 0
for i in range(len(array)):
    if i % 2 !=0:
        sum += array[i]
print(array)
print('Сумма элементов с нечётными индексами =', sum)