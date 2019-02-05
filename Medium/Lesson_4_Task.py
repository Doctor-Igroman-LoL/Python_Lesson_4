# Эти задачи необходимо решить используя регулярные выражения!
import re
# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

print('-' * 5, 'Решение первой задачи', '-' * 5)

pattern_name_and_surname = '^[A-ZА-Я.][a-zа-я]+$'
pattern_email = '^[a-z_0-9]+[@.][a-z0-9]+[\.](ru|org|com)$'
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
email = input('Введите свою электроную почту: ')

print_list = []
print_list.append(name) if re.search(pattern_name_and_surname, name) else print('Неправильно введено имя')
print_list.append(surname) if re.search(pattern_name_and_surname, surname) else print('неправильно введена фамилия')
print_list.append(email) if re.search(pattern_email, email) else print('неправильно введена электронная почта')
print('{} {} - {}'.format(print_list[0], print_list[1], print_list[2]))

# Задача - 2:
# Вам дан текст:
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

print('-' * 5, 'Решение второй задачи', '-' * 5)

pattern = '[.]{2,}'
print('В тексте найдено более одной точки') if re.search(pattern, some_str) else print('В тексте не найдено более одной точки')
