def remove_duplicates(lst):
    # Видаляємо повторювані елементи
    a_list = []
    for item in lst:
        if item not in a_list:
            a_list.append(item)
    return a_list
def sort_list(lst):
    # Окремо сортуємо числа і рядки
    numbers = sorted([item for item in lst if isinstance(item, int)])
    # Рядки сортуємо у алфавітному порядку, ігноруючи регістр
    strings = sorted([item for item in lst if isinstance(item, str)], key=str.lower)
    # Об'єднуємо числа і рядки в один список
    return numbers + strings
my_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
a_list = remove_duplicates(my_list)
print("Список без повторень:", a_list)
sorted_list = sort_list(a_list)
print("Відсортований список:", sorted_list)
