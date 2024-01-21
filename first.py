# print("hello")
# print("hello")
# print("Hello", end=" next")

# a = input("Рядок запрошення: ")

#  На екрані ви побачите: Рядок запрошення: #

# Власник Юра 
# a = input("Хто ти: ")
# if a=="Yura":
#  print('Привіт Власник')
# else:
#  6print(f"Привіт, {a}!")

# P квадрата
# a= int(input("Ведіть сторону квадрата "))
# P= a*4
# print(f"Периметир квадрата:{P}")

# Coffee
# Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# # Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# # Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant+ \
#              num_glasses * price_per_glass+ \
#              num_coffee_packs * price_per_coffee_pack

# # Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# # Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")

# my_list = [1, 2, 3, 4, 2, 2, 5, 2, 4]
# count_2 = my_list.count(4)
# print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

# nums = [3, 1, 4, 1, 5, 9, 2]
# nums.sort()
# print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(b.difference(a))  # {1, 2}
# print(a - b)  # {1, 2}

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# union = a | b  # Об'єднання множин
# intersection = a & b  # Перетин множин
# difference = a - b  # Різниця множин
# symmetric_difference = a ^ b  # Симетрична різниця

# print(union)  # frozenset({1, 2, 3, 4, 5})
# print(intersection)  # frozenset({3})
# print(difference)  # frozenset({1, 2})
# print(symmetric_difference)  # frozenset({1, 2, 4, 5})

# #.format
# # Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# # Чи більше число 10
# num = int(input("Ведіть число "))
# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")

    # # Задача 1.
# # Составить программу решения линейного уравнения а*х + b = 0 (а≠0). (a и b вводятся пользователем)

# a = float(input("Ведіть числа a: " ))
# b = float(input("Ведіть числа b: "  ))
# print(f"Ваші числа a={a} та b={b}")
# print(f"Ваше рівнння = x= {-b}/{a}={-b/a}")

# a = float(input("Ведіть першу сторону катета " ))
# b = float(input("Ведіть другу сторону катета " ))
# c=(a**2+b**2)*0.5
# print(f"Ви ввели такі сторони a={a} та b={b}, то гіпотинуза буде дорівнювати {c}")

# number = 1000

# while number >= 0:
#     print(number)
#     number -= 7
# print(number)


# # парне не парне
# x = int(input('Введіть число: '))

# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")

# a = input('Введіть число')
# a = int(a)

# if a == 1:
#     print('Число дорівнює 1')
# elif a > 0:
#     print('Число додатне')
# else:
#     print("a <= 0")

# тип bool
# money = 4
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

# #іS
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True
# print(a is c)  # False

#Наприклад, нам треба визначити, чи введене користувачем число є парним двозначним числом:

# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")

# Умовні оператори вкладені один в одного, що означає, що перевірка умов відбувається поетапно, і якщо перша умова x >= 0 виконується, то програма переходить до внутрішнього блоку і перевіряє умову y >= 0. 
# Якщо ця умова також виконується, то точка знаходиться в першій чверті. Якщо умова y >= 0 не виконується, то точка знаходиться в четвертій чверті.

# Якщо умова x >= 0 не виконується, то програма переходить до наступного внутрішнього блоку, але вже для оператора else, де виконується перевірка умови y >= 0. Якщо ця умова виконується, то точка знаходиться в другій чверті, якщо ні - у третій чверті.

# Отже, в результаті виконання даного коду буде виведена назва чверті, в якій знаходиться точка з координатами (x, y).

# x = -1
# y = 2
# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

# #тернарні операторои
# a = 5
# b = 8
# max_value = a if a > b else b
# print(max_value)


# # оператор match
# fruit = "apple"
# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")


# # розширена match
# point = (1, 0)

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")

# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")



# pets = ["dog", "fish", "cat"]

# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")

# some_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(some_list):
#     print(index, value)

# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for number, letter in zip(list1, list2):
#     print(number, letter)

# sum = 0
# list = [1,2,3,4,5,6]
# for num in list:
#     sum += num
# print(sum)

# # items
# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }
# # print(numbers)
# for k, v in numbers.items():
#     print(k, v)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0


# while num >= 0:
#     sum=+num
# print(sum)

# num = int(input("Введіть ціле число від 0 до 100: "))
# sum_result = 0

# while num >= 1:
#     sum_result += num
#     num -= 1

# print("Сума всіх чисел від 1 до введеного числа:", sum_result)

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == "r":
#      result += 1
#      print(result)

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#    chunk = pool / quantity
# except: ZeroDivisionError
# print('Divide by zero completed!')

# # summ
# list = [1,5,3,4,6,7]
# sum=0
# for i in list:
#     print(i)
#     sum+=i
# print(sum)


# # Функція
# def say_hello():
# 		# тіло функції
#     print('Привіт, Світ!')

# # Кінець функції say_hello()

# # виклик функції
# say_hello()

# # ще один виклик функції
# say_hello()

# # Аргумент 
# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів
    
# # Функція з int
# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# # return
# def add_sum (num1:int, num2:int):
#     sum = num1 + num2
#     return sum
# x = int(input("Ведіть 1 число "))
# y = int(input("Ведіть 2 число "))
# result = add_sum (x,y)
# print( f"сума чисел {result}")

# # retirn
# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!

# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал


# # list
# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]

# # coppy
# def modify_list(lst: list) -> None:
#      lst = lst.copy()
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3] 
                            

# # задача на функц
# def string_to_codes(string: str):
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes
# result = string_to_codes("Hello world!")
# print(result)

# # факторіал
# def factorial(x: int):
#     result = 1
#     while x >= 1:
#         result *= x
#         x -= 1
#     return result

# # Введення числа з клавіатури
# input_number = int(input("Введіть число для обчислення факторіалу: "))

# # Виклик функції та виведення результату
# result_factorial = factorial(input_number)
# print(f"Факторіал числа {input_number} дорівнює {result_factorial}")

# # паліндром
# def is_palindrome(val: str):
#     
    
#     # Переведіть рядок в нижній регістр і видаліть пробіли
#     cleaned_val = val.lower().replace(" ", "")
    
#     # Використовуйте [::-1] для обертання рядка
#     reversed_val = cleaned_val[::-1]
    
#     # Порівнюйте вихідний рядок і його обернений варіант
#     if cleaned_val == reversed_val:
#         return True
#     else:
#         return False

# # Введення рядка з клавіатури
# input_string = input("Введіть рядок для перевірки на паліндром: ")

# # Виклик функції та виведення результату
# result = is_palindrome(input_string)
# print(f"Чи є рядок паліндромом? {result}")

# def is_palindrome(num: int):
#     clened_num = str(num)
#     reverse_num=clened_num[::-1]
#     if clened_num==reverse_num:
#         return True
#     else:
#         return False
    
# input_string = input("Введіть рядок для перевірки на паліндром: ")


# result = is_palindrome(input_string)
# print(f"Чи є число паліндромом? {result}")
    
# def factorial(x:int):
#     result = 1
#     while x >= 1:
#          result *= x
#          x-=1
#     return result

# input_num = int(input("Ведіть число "))
# finish = factorial(input_num)
# print(f"Ви вели число {input_num} його факторіал {finish}")

# #   Local
# x = 50
# def func():
#     x = 2 
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50

# #  Enclosing
# def outer_func():
#     enclosing_var = "Я змінна в функції, що охоплює"

#     def inner_func():
#         print("Всередині вкладеної функції:", enclosing_var)

#     inner_func()

# outer_func()


#  nonlocal
# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x

# result = func_outer()  # 5

# print(result)

# x= float(input("ведіть цифру "))
# y = float(input("Ведіть дісконт "))

# def discount_price(price, discount):
#    def apply_discount():
#         nonlocal price
#         price = price * (1-discount)
#         return price
#    return apply_discount()

# final = discount_price(x, y)
# print( final)

# # global
# x = 50

# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x)# Значення x складає 2


# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")

# # використовує значення за замовчуванням для message
# greet("Олексій")  

# # передача власного значення для message
# greet("Марія", message="Добрий день") 


# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)

# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)

# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)

# def say(message, times=1):
#     print(message * times)

# say('Привіт') 
# say('Світ', 5)


# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name 
#         return f"{first_name} {last_name}"
#     else:
#         return f"{first_name} {last_name} {middle_name}"
# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name == "":
#         return(f"{first_name} {last_name}")
#     else:
#         return(f"{first_name} {middle_name} {last_name}")

# first_name = "Yura"
# last_name = "Sergiyovich"
# middle_name = None

# fullname = get_fullname(first_name, last_name, middle_name)
# print(fullname)

# # dz_string
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         a = (length-len(string)) 
#         string = " " * a + string
#         return string

# formatted_result = format_string("Hello", 10)


# print(formatted_result)
# print(len(formatted_result))
    
#  Виклкик функцій
#  def first(size, *params):
#     return size + len(params)

# def second(size, **params):
#     return size + len(params)

# # Приклади викликів функцій
# print(first(5, "first", "second", "third"))  # Результат: 8
# print(first(1, "Alex", "Boris"))             # Результат: 3
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6
# print(second(10, comment_one="Alex", comment_two="Boris")) # Результат: 12

#  признеченя для кількості 
# def say(message, times=1):
#     print(message * times)

# say('Привіт') 
# say('Світ', 5)

# знижка
# def real_cost(base: int, discount: int = 0) -> int:
#     return base * (1 - discount)

# x = int(input("Ведіть ціну "))
# y = float(input("Ведіть дисконт "))


# *args
# def print_all_args(*args):
#     for arg in args:
#         print(arg)

# print_all_args(1, 'hello', True)

# примінення *args
# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))




# price_discount = real_cost(x, y)
# print(f'Ваша знижка {price_discount}')

# price_bread = 15
# price_butter = 50
# price_sugar = 60

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)

# print(current_price_bread, current_price_butter, current_price_sugar)

# # **kwargs
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=25)

# # * and **
# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)

# example_function(1, 2, 3, 4, name="Alice",  age=25)

# # Факторіал
# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# char = int(input('Ведіть число '))
# final = factorial(char)
# print(f"Факторіал {char} це буде {final}") # виведе 120


# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))


# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result
# print(factorial(7))


    