numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_of_none = numbers.index(None)
count_of_numbers = len(numbers)
sum_of_numbers = sum(numbers[:index_of_none]) + sum(numbers[index_of_none+1:])
average_of_number = sum_of_numbers/count_of_numbers
numbers[index_of_none] = average_of_number
print("Измененный список:", numbers)