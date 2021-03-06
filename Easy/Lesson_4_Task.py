# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
print('-' * 5, 'Решение первой задачи', '-' * 5)

random_list = [x**2 for x in range(1, random.randint(2, 20))]
print(random_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print('-' * 5, 'Решение второй задачи', '-' * 5)

list_first = ['Бананы', 'Апельсиный', 'Яблоки', 'Груши']
list_second = ['Мандарины', 'Авокадо', 'Инжир', 'Инопланетные фрукты']

common_list = [list_first.append(fruit) for fruit in list_second]
print(list_first)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('-' * 5, 'Решение третий задачи', '-' * 5)

random_list_second = [i for i in range(-10, random.randint(0, 30)) if i % 3 == 0 and i > 0 and i % 4 != 0]
print(random_list_second)