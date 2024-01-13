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

# Ось пояснення:

# x = 1 і y = 2 - це координати точки на площині.

# Умова if x >= 0: перевіряє, чи x не менше 0. Якщо це вірно, виконується блок коду всередині цієї умови.

# Усередині першої умови, ще одна умова if y >= 0: перевіряє, чи y не менше 0. Якщо і це вірно, виводиться текст "Перша чверть", оскільки обидві координати x і y є не менше 0.

# Якщо перша умова if x >= 0: не виконується, тобто x менше 0, виконується блок коду всередині else:.

# Усередині блоку коду для else:, знову є умова if y >= 0:, що перевіряє, чи y не менше 0. Якщо це вірно, виводиться текст "Друга чверть", оскільки x менше 0 і y не менше 0.

# Якщо обидві умови if x >= 0: та if y >= 0: не виконуються, виконується блок коду всередині останньої умови else:, і виводиться текст "Третя чверть", оскільки x менше 0 і y менше 0.

# Отже, в залежності від знаків координат x та y визначається у якому квадранті знаходиться точка на площині, і відповідний текст виводиться на екран. В даному випадку, оскільки x = 1 (більше 0) і y = 2 (більше 0), виведеться "Перша чверть".

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