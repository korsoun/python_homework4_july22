# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Допустим, что в списке элементы должны храниться строго в том же порядке.
def get_unique_list (general_list):
    non_unique_set = set()
    for i in range(1, len(general_list)):
        count = 1
        for j in range(i, len(general_list)):
            if general_list[j] == general_list[i-1]:
                count += 1
        if count != 1:
            non_unique_set.add(general_list[i-1])
    unique_list = []
    for elem in general_list:
        if elem not in non_unique_set:
            unique_list.append(elem)
    return unique_list

            
list = [1,1,2,3,4,4,5,6,7,8,8]
print(f'Задан список {list}')
print(f'Список его уникальных элементов: {get_unique_list(list)}')

