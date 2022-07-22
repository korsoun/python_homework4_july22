# Дополнительная задача.
# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

def get_num_list (file):
    with open (file, 'r') as find_file:
        broken_list = find_file.read().split()
        for i in range(len(broken_list)):
            broken_list[i] = int(broken_list[i])
    return broken_list

def find_number (broken_list):
    broken = None
    for i in range(len(broken_list)-1):
        if broken_list[i] != broken_list[i+1] - 1:
            broken = broken_list[i] + 1
    return broken
            

file = 'find_file.txt'
if find_number(get_num_list(file)):
    print(f'Не хватает числа {find_number(get_num_list(file))}')
else:
    print('Числовая последовательность корректна.')