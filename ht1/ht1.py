# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

def sort_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

numbers = [2, 7, 4, 5, 0, 500]

print('Задача №1 императивный стиль:')
sort_imperative(numbers)
print(numbers)
 
print('Задача №2 декларативный стиль:')
sort_declarative(numbers)
print(numbers)
