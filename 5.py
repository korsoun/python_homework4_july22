# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import re

# str_first_polynom - строка, содержащая запись уравнения
# list_first_polynom - список, хранящий слагаемые 
# dict_first_polynom - словарь, ключи и значения которого - степени слагаемых и их коэффициенты
# list_grades_first_polynom - список, хранящий степени слагаемых
# Для второго многочлена аналогично
def get_coefs_grades (list_first_polynom):
    dict_first_polynom = {}
    list_grades_first_pol = []
    for element in list_first_polynom:
        coefficient = None
        grade = None
        index_coef = 0
        index_grade = len(element) - 1
        # Поиск коэффициента и степени для слагаемого вида 4x^3
        if not element.isdigit() and element[len(element)-1].isdigit() and element[0].isdigit():
            while element[index_coef].isdigit():
                index_coef += 1
            while element[index_grade].isdigit():
                index_grade -= 1
            coefficient = int(element[:index_coef])
            grade = int(element[index_grade + 1:])
            # if (str_first_polynom.find(element) - 2) == '-':    Честно, не знаю, почему этот кусок не работает. Ведь с тем же самым символом прошел re.split
            #     coefficient = -coefficient
        # Поиск коэффициента и степени для слагаемого вида x^3
        if not element[0].isdigit() and element[len(element)-1].isdigit():
            while element[index_grade].isdigit():
                index_grade -= 1
            coefficient = 1
            grade = int(element[index_grade + 1:])
        # Поиск коэффициента и степени для слагаемого вида 4x
        if not element.isdigit() and element[0].isdigit() and not element[len(element)-1].isdigit():
            while element[index_coef].isdigit():
                index_coef += 1
            coefficient = int(element[:index_coef])
            grade = 1
        # Поиск коэффициента и степени для слагаемого вида x
        if len(element) == 1 and not element.isdigit():
            coefficient = 1
            grade = 1
        # Поиск коэффициента и степени для слагаемого вида 8
        if element.isdigit():
            coefficient = int(element)
            grade = 0

        dict_first_polynom[f'grade {grade}'] = coefficient
        list_grades_first_pol.append(grade)
    return dict_first_polynom, list_grades_first_pol

def get_new_polynom (first_dict, second_dict, biggest_grade):
    dict_res_polynom = {}
    for grade in range(biggest_grade + 1):
        # Дополняем словари нулевыми значениями для отсутствующих степеней, чтобы не схватить ошибку
        if first_dict.get(f'grade {grade}') == None:
            first_dict[f'grade {grade}'] = 0
        if second_dict.get(f'grade {grade}') == None:
            second_dict[f'grade {grade}'] = 0
        # Сложение коэффициентов при одинаковых степенях
        dict_res_polynom[f'grade {grade}'] = first_dict[f'grade {grade}'] + second_dict[f'grade {grade}']
    str_res_polynom = ''
    while biggest_grade >= 0:
        # Сбор строки при слагаемом вида 4x^2
        if biggest_grade > 1 and dict_res_polynom[f'grade {biggest_grade}'] > 1:
            coef = dict_res_polynom[f'grade {biggest_grade}']
            str_res_polynom += f' + {coef}x^{biggest_grade}'
        # Сбор строки при слагаемом вида x^2
        if biggest_grade > 1 and dict_res_polynom[f'grade {biggest_grade}'] ==1:
            str_res_polynom += f' + x^{biggest_grade}'
        # Сбор строки при слагаемом вида 4x 
        if biggest_grade == 1 and dict_res_polynom[f'grade {biggest_grade}'] > 1:
            coef = dict_res_polynom[f'grade {biggest_grade}']
            str_res_polynom += f' + {coef}x'
        # Сбор строки при слагаемом вида 4
        if biggest_grade == 0:
            coef = dict_res_polynom[f'grade {biggest_grade}']
            str_res_polynom += f' + {coef}'
        # Сбор строки при слагаемом вида x
        if biggest_grade == 1 and dict_res_polynom[f'grade {biggest_grade}'] == 1:
            str_res_polynom += ' + x'
        biggest_grade -= 1
    str_res_polynom += " = 0"
    str_res_polynom = str_res_polynom[3:]
    return str_res_polynom

# Открытие первого файла
str_first_polynom = ''
with open('first_polynom.txt', 'r', encoding = 'utf-8') as first_file:
    str_first_polynom = first_file.read()
# Получение строки, отсев ненужной части и разделение на слагаемые
str_first_polynom = str_first_polynom[:len(str_first_polynom)-4]
list_first_polynom = re.split(' \+ | - ', str_first_polynom)
# То же самое для второго файла
str_second_polynom = ''
with open('second_polynom.txt', 'r', encoding = 'utf-8') as second_file:
    str_second_polynom = second_file.read()
str_second_polynom = str_second_polynom[:len(str_second_polynom)-4]
list_second_polynom = re.split(' \+ | - ', str_second_polynom)

# dict'ы хранят словари (степень - коэффициент при ней)
# list'ы хранят списки степеней
first_dict = get_coefs_grades(list_first_polynom)[0]    
first_list = (get_coefs_grades(list_first_polynom)[1])
second_dict = get_coefs_grades(list_second_polynom)[0]    
second_list = (get_coefs_grades(list_second_polynom)[1])
biggest_grade = max(first_list + second_list)
with open('result_polynom.txt', 'w') as res_file:
    res_file.write(get_new_polynom(first_dict, second_dict, biggest_grade))