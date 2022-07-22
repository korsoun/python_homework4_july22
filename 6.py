# Дополнительная задача.
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
                # Иванов 23543.12
                # Петров 13749.32

def get_salary_dict (file_name):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        dict_salaries = dict()
        for line in file.readlines():
            # Прочитать строку, разделить надвое по знаку пробела, добавить в список
            current_line = line.split()
            # Внести данные в словарь. Ключ - первый элемент словаря, значение - второй элемент
            dict_salaries[current_line[0]] = float(current_line[1])
    return dict_salaries

def get_low_salary_list (dict_salary):
    low_salary_list = []
    for key in dict_salary:
        if dict_salary[key] < 20000:
            low_salary_list.append(key)
    return low_salary_list

def get_avg_salary (dict_salary):
    count = 0
    sum = 0
    for key in dict_salary:
        sum += dict_salary[key]
        count += 1
    avg_sal = sum / count
    return avg_sal
    



file_name = 'salaries.txt'
print(f' Список сотрудников с заработной платой ниже 20.000: {get_low_salary_list(get_salary_dict(file_name))}')
print(f' Средняя заработная плата составляет {round(get_avg_salary(get_salary_dict(file_name)), 2)}')


