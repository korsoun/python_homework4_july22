# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def get_multipliers_list (num):
    """Рекурсивная функция, выводит список простых множителей в формате целых чисел.

    Аргумент num - целое число.
    При отсутствии простых множителей выведет список размера 0.
    
    """
    multipliers_list = []
    for i in range(2, num):
        if num % i == 0 and len(get_multipliers_list(i)) == 0: 
            multipliers_list.append(i)
    return multipliers_list

num = int(input('Введите число N: '))
if len(get_multipliers_list(num)) != 0:
    print(f'Список простых множителей числа {num}: {get_multipliers_list(num)}')
else:
    print(f'Простых множителей у числа {num} нет.')