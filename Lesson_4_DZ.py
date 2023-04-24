import math

# Задача 1. Дано натуральное число N. Напишите метод,
# который вернёт список простых множителей числа N и количество этих множителей.

# 60 -> 2, 2, 3, 5

def Task1():
    n = int(input('Введите число: '))
    divs = []
    div = 2
    while n > 1:
        if n % div == 0:
            divs.append(div)
            n //= div
        else:
            div +=1
    print(divs)

# Задача 2. В первом списке находится информация об ассортименте мороженного,
# во втором списке - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.

# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

def vafelki():
    list1 = {'Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка'}
    list2 = {'Сливочное', 'Вафелька', 'Сладкоежка'}

    list3 = list1.difference(list2)
    print(f'Закончилась {list3}')


# Задача 3. Выведите число π с заданной точностью.
# Точность выводится в виде десятичной дроби.
# 3 -> 3.142

def Task3():
    n = int(input('Введите точность: '))
    print(round(math.pi, n))


# Задача 4*. Даны два файла, в каждом из которых находится
# запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8
def polinomi():
    data = open('file1.txt', encoding='utf-8')
    text = data.readlines()
    data.close()

    data = open('file2.txt', encoding='utf-8')
    text += data.readlines()
    data.close()

    poly_f = text[0]
    poly_s = text[1]    

    poly_s = poly_s.replace(' ', '')
    poly_s = poly_s.replace('-', '+-')
    if poly_s[0] == '+':
        poly_s = poly_s[1:]
    poly_s = poly_s.split('+')

    for i in range(len(poly_s)):
        if not 'x^' in poly_s[i]:
            if 'x' in poly_s[i]: poly_s[i] = poly_s[i].replace('x', 'x^1')
            else: poly_s[i] = poly_s[i] + 'x^0'
    
    poly_s = dict(i.split('x^') for i in poly_s)
    

    


    print(poly_f)
    print(poly_s)