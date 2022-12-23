array = [float(i) for i in input('Введите элементы через пробел ').split()]
min = round(array[0] % 1, 8)
max = round(array[0] % 1, 8)
for i in range(1, len(array)):
    if round(array[i] % 1, 8) < min: min = round(array[i] % 1, 8)
    elif round(array[i] % 1, 8) > max: max = round(array[i] % 1, 8)
print(array)
print(max - min)