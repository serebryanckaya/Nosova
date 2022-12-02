l = []
def sum_digits(b):
    if (b == 0):
        return l
    dig = b % 10
    l.append(dig)
    sum_digits(b // 10)
n = int(input("Введите число: "))
sum_digits(n)
print(sum(l))
"""Функция sum() начинает суммирование элементов последовательности iterable с начального 
значения start, если оно указано, сложение происходит слева направо и в результате возвращает их сумму."""