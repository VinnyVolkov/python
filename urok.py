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

# a = 5
# b = 1
# max_value = a if a > b else b
# print(max_value)

# num = int(input("Число "))
# sum = 0

# while num >= 1:
#       sum += num
#       num -= 1
# print(sum)

# list = [1,5,3,4,6,7]
# sum=0
# for i in list:
#     print(i)
#     sum+=i
# print(sum)


# length = int(20)
# width = int(15)
# area = length * width
# area = int(area)
# print(area)


# celsius = float(input("Введіть температуру в градусах Цельсія: "))
# fahrenheit = (celsius * 9/5) + 32

# print(f"{celsius} градусів Цельсія дорівнює {fahrenheit:.2f} градусам Фаренгейта.")

# val = str(input("Ведіть слово "))
# k= len(val)
# print(f" Кількість символів в даному рядкустановить {k} ")

# is_palindrome = input(" Ведіть ваше слово ")
# reverse = is_palindrome
# if reverse == is_palindrome [::-1]:
#     print("Слово є палідромом")
# else:
#     print(" Нажаль слово не є палідромом!")
