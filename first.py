#print("hello")
#print("hello")
#print("Hello", end=" next")

#a = input("Рядок запрошення: ")
#
#  На екрані ви побачите: Рядок запрошення: #

# Власник Юра 
# a = input("Хто ти: ")
#if a=="Yura":
 #print('Привіт Власник')
#else:
 #6print(f"Привіт, {a}!")

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