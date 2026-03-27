# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group_1, group_2, arg=','):
    list1 = group_1.split(arg)
    list2 = group_2.split(arg)

    common = list(set(list1) & set(list2))
    common.sort()
    return common
group_1 = "Иванов,Петров,Сидоров"
group_2 = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(group_1, group_2)
print("Общие участники:", result)

