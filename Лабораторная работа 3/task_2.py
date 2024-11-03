# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep = ","):
    set_people1 = set(group1.split(sep))
    set_people2 = set(group2.split(sep))
    list_common_participants = list(set_people1.intersection(set_people2))
    list_common_participants.sort()
    return list_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(f'Общие участники: {find_common_participants(participants_first_group, participants_second_group, "|")}')