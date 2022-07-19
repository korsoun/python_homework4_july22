# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена.
# Записать в файл многочлен степени k.

import random

def get_coefficients (grade):

    '''Функция получает число, обозначающее степень многочлена, и выдает список коэффициентов.'''

    coefficient_list = []
    for i in range(grade + 1):
        if len(coefficient_list) == grade:
            coefficient_list.append(random.randint(1, 100))  # Последний элемент от 1 до 100, чтобы гарантированно получить многочлен заданной степени.
        else:
            coefficient_list.append(random.randint(0, 100))
    return coefficient_list

def get_polynom (k):

    '''Функция получает число, обозначающее степень многочлена, и выдает запись многочлена в виде строки'''

    coefficient_list = get_coefficients(k)
    polynom = ' = 0'
    for grade in range(len(coefficient_list)):
        if grade == 0:
            polynom = f' + {coefficient_list[grade]}' + polynom
        elif grade == 1:
            if coefficient_list[grade] == 1:
                polynom = f' + x' + polynom
            elif coefficient_list[grade] > 1:
                polynom = f' + {coefficient_list[grade]}x' + polynom
        else:
            if coefficient_list[grade] == 1:
                polynom = f' + x^{grade}' + polynom
            elif coefficient_list[grade] > 1:
                polynom = f' + {coefficient_list[grade]}x^{grade}' + polynom
    polynom = polynom[2:]
    return polynom    

k = int(input('Введите требуемую степень уравнения больше 0: '))
if k > 0:
    polynom = get_polynom(k)
    print(f'Сформировано уравнение: {polynom}')
    with open('polynom.txt', 'w', encoding = 'utf-8') as polynom_file:
        polynom_file.write(polynom)
    print(f'Уравнение записано в файл polynom.txt')
else:
    print('Недопустимая степень.')
