# 1. Создать список и заполнить его элементами различных типов данных. 
# Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

a = 12
b = 12,35
c = "Hello"
d =  ('a', 'b', '13')
e = ['a', 'c', 'e']
f = {'name': 'Daiana', 'lastname': 'Dudina'}

main_list = [a,b,c,d,e,f]
for el in main_list:
    print(f'{el} is {type(el)}')


# 2. Для списка реализовать обмен значений соседних элементов, т.е. 
# значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

list = list(input("Введите список >>>"))
list[::2], list[1::2] = list[1::2], list[::2]
print(list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input('Порядковый номер месяца >>>'))
if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])
    print(seasons_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
    print(seasons_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
    print(seasons_dict[3])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
    print(seasons_dict[4])
else:
    print('Введите число в диапазоне от 1 до 12 >>> ')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове.

sentences = (input('Введите слова>>>'))
a = sentences.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 4, 3, 3, 2]
rating = int(input("Введите число >>> "))
a = my_list.count(rating)
for element in my_list:
    if a > 0:
        i = my_list.index(rating)
        my_list.insert(i+a, rating)
        break
    else:
        if rating > element:
            b = my_list.index(element)
            my_list.insert(b, rating)
            break
        elif rating < my_list[len(my_list) - 1]:
            my_list.append(rating)
print(my_list) 


# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента 
# — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. 
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, 
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

goods = []
while input("Would you like add product? Enter yes/no: ") == 'yes':
    number = int(input("Enter product number: "))
    features = {}
    while input("Would you like add product parameters? Enter yes/no: ") == 'yes':
        feature_key = input("Enter feature product: ")
        feature_value = input("Enter feature value product: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
#goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)
