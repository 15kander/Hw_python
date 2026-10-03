# N1:
# name = input('Введите свое имя: ')
# age = int(input('Введите свой возраст: '))
# print(f'Через 10 лет вам будет {age + 10} лет, {name}.')

# N2:
# sum = 0
# for i in range(1, 4):
#     num = int(input(f'Введите число {i}: '))
#     sum += num
# print(f'Сумма чисел: {sum}')

# N3:
# s = int(input('Введите количество секунд: '))
# print(f'Это {s // 3600} часов, {s % 3600 // 60} минут и {s % 60} секунд.')

# N4:
# tr_a = int(input('Введите длину стороны треугольника: '))
# tr_b = int(input('Введите длину второй стороны треугольника: '))
# tr_c = int(input('Введите длину третьей стороны треугольника: '))
# p = (tr_a + tr_b + tr_c) / 2
# print(f'Площадь треугольника: {((p) * (p - tr_a) * (p - tr_b) * (p - tr_c)) ** 0.5}')

# N5:
# avg = 0
# for i in range(1, 6):
#     num = int(input(f'Введите число {i}: '))
#     avg += num
# print(f'Среднее значение: {avg / 5}')

# N6:
# num = int(input('Введите число: '))
# if num > 0:
#     print('Число положительное.')
# elif num < 0:
#     print('Число отрицательное.')
# else:
#     print('Число равно нулю.')

# N7:
# num = int(input('Введите число: '))
# print('Число четное.' if num % 2 == 0 else 'Число нечетное.')

# N8:
# n1 = int(input('Введите число 1: '))
# n2 = int(input('Введите число 2: '))
# print('Число 1 больше числа 2.' if n1 > n2 else 'Число 2 больше числа 1.' if n2 > n1 else 'Числа равны.')

# N9:
# max_num = 0
# for i in range(1, 4):
#     num = int(input(f'Введите число {i}: '))
#     if num > max_num:
#         max_num = num
# print(f'Максимальное число: {max_num}')

# N10:
# year = int(input('Введите год: '))
# print('Год високосный.' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 'Год не високосный.')

# N11:
# tr_exist = False
# tr_a = int(input('Введите длину стороны треугольника: '))
# tr_b = int(input('Введите длину второй стороны треугольника: '))
# tr_c = int(input('Введите длину третьей стороны треугольника: '))
# if tr_a + tr_b > tr_c and tr_a + tr_c > tr_b and tr_b + tr_c > tr_a:
#     tr_exist = True
#     print('Треугольник существует.')
# else:
#     print('Треугольник не существует.')

# N12:
# tr_type = None
# tr_a = int(input('Введите длину стороны треугольника: '))
# tr_b = int(input('Введите длину второй стороны треугольника: '))
# tr_c = int(input('Введите длину третьей стороны треугольника: '))
# if tr_a + tr_b > tr_c and tr_a + tr_c > tr_b and tr_b + tr_c > tr_a:
#     if tr_a == tr_b == tr_c:
#         tr_type = 'равносторонний'
#     elif tr_a == tr_b or tr_a == tr_c or tr_b == tr_c:
#         tr_type = 'равнобедренный'
#     else:
#         tr_type = 'разносторонний'
#     print(f'Треугольник существует и он {tr_type}.')
# else:
#     print('Треугольник не существует.')

# N13:
# discount = 0
# purchase_amount = float(input('Введите сумму покупки: '))
# if purchase_amount >= 5000:
#     discount = 0.07
# elif purchase_amount >= 3000:
#     discount = 0.05
# elif purchase_amount >= 1000:
#     discount = 0.03
# final_amount = purchase_amount * (1 - discount)
# print(f'Сумма покупки: {purchase_amount:.2f} руб.')
# print(f'Скидка: {discount * 100:.0f}% или {purchase_amount * discount:.2f} руб.')

# N14:
# zodiac_sign = None
# birthday = int(input('Введите день рождения: '))
# month = int(input('Введите месяц рождения (1-12): '))
# if month < 1 or month > 12:
#     print('Некорректный месяц рождения.')
# else:
#     for m in range(1, 13):
#         if month == 1:
#             zodiac_sign = 'Козерог' if birthday <= 19 else 'Водолей'
#         elif month == 2:
#             zodiac_sign = 'Водолей' if birthday <= 18 else 'Рыбы'
#         elif month == 3:
#             zodiac_sign = 'Рыбы' if birthday <= 20 else 'Овен'
#         elif month == 4:
#             zodiac_sign = 'Овен' if birthday <= 19 else 'Телец'
#         elif month == 5:
#             zodiac_sign = 'Телец' if birthday <= 20 else 'Близнецы'
#         elif month == 6:
#             zodiac_sign = 'Близнецы' if birthday <= 20 else 'Рак'
#         elif month == 7:
#             zodiac_sign = 'Рак' if birthday <= 22 else 'Лев'
#         elif month == 8:
#             zodiac_sign = 'Лев' if birthday <= 22 else 'Дева'
#         elif month == 9:
#             zodiac_sign = 'Дева' if birthday <= 22 else 'Весы'
#         elif month == 10:
#             zodiac_sign = 'Весы' if birthday <= 22 else 'Скорпион'
#         elif month == 11:
#             zodiac_sign = 'Скорпион' if birthday <= 21 else 'Стрелец'
#         elif month == 12:
#             zodiac_sign = 'Стрелец' if birthday <= 21 else 'Козерог'
# print(f'Ваш знак зодиака: {zodiac_sign}.')

# N15:
# calc_type = input('Введите тип калькуляции (1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление): ')
# num1 = float(input('Введите первое число: '))
# num2 = float(input('Введите второе число: '))
# result = None

# if calc_type == '1':
#     result = num1 + num2
# elif calc_type == '2':
#     result = num1 - num2
# elif calc_type == '3':
#     result = num1 * num2
# elif calc_type == '4':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         print('Ошибка: деление на ноль!')

# if result is not None:
#     print(f'Результат: {result}')   

# N16:
# N = int(input('Введите число N: '))
# for i in range(1, N + 1):
#     print(i)

# N17:
# n = int(input('Введите число N: '))
# for i in range(n, 0, -1):
#     print(i)

# N18:
# sum = 0
# N = int(input('Введите число N: '))
# for i in range(1, N + 1):
#     sum += i
# print(f'Сумма чисел от 1 до {N}: {sum}')

# N19:
# product = 1
# N = int(input('Введите число N: '))
# for i in range(1, N + 1):
#     product *= i
# print(f'Произведение чисел от 1 до {N}: {product}')

# N20:
# N = int(input('Введите число N: '))
# for i in range(1, 11):
#     print(f'{i} * {N} = {i * N}')

# N21:
# sum_even = 0
# N = int(input('Введите число N: '))
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         sum_even += i
# print(f'Сумма четных чисел от 1 до {N}: {sum_even}')

# N22:
# digit_count = 0
# N = int(input('Введите число N: '))
# while N > 0:
#     digit_count += 1
#     N //= 10
# print(f'Количество цифр в числе: {digit_count}')

# N23:
# sum_digits = 0
# N = int(input('Введите число N: '))
# while N > 0:
#     sum_digits += N % 10
#     N //= 10
# print(f'Сумма цифр в числе: {sum_digits}')

# N24:
# reverse_num = 0
# N = int(input('Введите число N: '))
# while N > 0:
#     reverse_num = reverse_num * 10 + N % 10
#     N //= 10
# print(f'Обратное число: {reverse_num}')

# N25:
# is_palindrome = False
# N = int(input('Введите число N: '))
# original_N = N
# reverse_num = 0

# while N > 0:
#     reverse_num = reverse_num * 10 + N % 10
#     N //= 10

# if original_N == reverse_num:
#     is_palindrome = True

# print(f'Число {original_N} является палиндромом' if is_palindrome else f'Число {original_N} не является палиндромом.')

# N26:
# square_a = int(input('Введите длину стороны квадрата: '))
# square = ''
# for i in range(square_a):
#     for j in range(square_a):
#         square += '*'
#     square += '*' * square_a + '\n'
# print(square)

# N27:
# triangle_height = int(input('Введите высоту треугольника: '))
# square_triangle = ''
# for i in range(1, triangle_height + 1):
#     square_triangle += '*' * i + '\n'
# print(square_triangle)

# N28:
# triangle_height = int(input('Введите высоту треугольника: '))
# piramid_triangle = ''
# for i in range(1, triangle_height + 1):
#     spaces = ' ' * (triangle_height - i)
#     stars = '*' * (2 * i - 1)
#     piramid_triangle += spaces + stars + '\n'
# print(piramid_triangle)

# N29:
# checkmate_desk = ''
# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             checkmate_desk += ' ='
#         else:
#             checkmate_desk += ' +'
#     checkmate_desk += '\n'
# print(f'[=] : белые клетки\n[+] : черные клетки\n\n{checkmate_desk}')

# N30:
# product_couple = []
# number = int(input('Введите число: '))
# for i in range(1, number+1):
#     for j in range(i, number+1):
#         if i*j == number:
#             product_couple.append((i, j))
# print(f'Пары чисел, произведение которых равно {number}:\n {" ".join(map(str, product_couple))}')

# N31:
# str = input('Введите строку: ')
# print(f'кол-во символов в строке: {len(str)}')

# N32:
# string = input('Введите строку: ')
# vowel_letters_count = 0
# vowel_letters = 'aeiouAEIOU'
# for i in string:
#     if i in vowel_letters:
#         vowel_letters_count += 1
# print(f'Количество гласных букв в строке: {vowel_letters_count}')

# N32:
# String = input('Введите строку: ')
# word_count = 0
# for i in String:
#     if i == '.':
#         break
#     elif i == ' ':
#         word_count += 1
# print(f'Количество слов в предложении: {word_count + 1}')

# N34:
# stroka = input('Введите строку: ')
# if stroka == stroka[::-1]:
#     print('Строка является палиндромом')
# else:
#     print('Строка не является палиндромом')

# N35:
# st = input('Введите строку: ')
# new_st = ''
# for i in st:
#     if i == ' ':
#         new_st += '_'
#     else:
#         new_st += i
# print(f'Строка после замены пробелов на подчеркивания: {new_st}')

# N36:
# s = input('Введите строку: ')
# need_sign = input('Введите символ, кол-во которого нужно посчитать: ')
# count = s.count(need_sign)
# print(f'Количество символов "{need_sign}" в строке: {count}')

# N37:
# s = input('Введите строку: ')
# largest_word = ''
# for word in s.split():
#     if len(word) > len(largest_word):
#         largest_word = word
# print(f'Самое длинное слово в строке: {largest_word}')

# N38:
# s = input('Введите строку: ')
# reversed_s = s[::-1]
# print(f'Строка в обратном порядке: {reversed_s}')

# N39:
# st = input('Введите строку: ')
# new_st = ''
# for i in st:
#     if i.isdigit():
#         continue
#     elif i.isspace():
#         new_st += ' '
#     elif i.isalpha():
#         new_st += i
# print(f'Строка без цифр: {new_st}')

# N40:
# s_1 = input('Введите первую строку: ')
# s_2 = input('Введите вторую строку: ')
# isAnagram = sorted(s_1.replace(' ', '').lower()) == sorted(s_2.replace(' ', '').lower())
# print(f'Строки являются анаграммами.' if isAnagram else f'Строки не являются анаграммами.')

# N41:
# list_num = [2, 7, 5, 4, 13, 5, 7, 8, 11]
# sum = 0
# for i in list_num:
#     sum += i
# print(f'Сумма чисел в списке: {sum}')
# # N42:
# print(f'Максимальное число в списке: {max(list_num)}')
# # N43:
# print(f'Минимальное число в списке: {min(list_num)}')
# # N44:
# print(f'Второе по величине число в списке: {sorted(list_num)[-2]}')
# # N45:
# print(f'Список без дубликатов: {list(set(list_num))}')
# # N46:
# print(f'Список в обратном порядке: {list_num[::-1]}')
# # N47:
# not_even_count = 0
# for i in list_num:
#     if i % 2 != 0:
#         not_even_count += 1
# print(f'Количество нечетных чисел в списке: {not_even_count}')
# # N48:
# list_num_2 = [1, 5, 2, 7, 3, 8, 4]
# print(f'Объединенный список без дубликатов: {list(set(list_num + list_num_2))}')
# # N49:
# print(f'Список чисел, которые встречаются в обоих списках: {list(set(list_num) & set(list_num_2))}')
# # N50:
# k = int(input('Введите число на которое нужно сдвинуть элементы списка: '))
# print(f'Список до сдвига элементов: {list_num}')
# list_num = list_num[k:] + list_num[:k]
# print(f'Список после сдвига элементов: {list_num}')

# N51:
# elem = (1, 2, 3, 4, 5)
# print(f'Сумма элементов кортежа: {sum(elem)}')

# N52:
# list_num = [3,4,1,2,4,12,6,7,7,3,2]
# print(f'Уникальные элементы списка: {list(set(list_num))}')

# N53:
# first_set = {1, 2, 3, 4, 5}
# second_set = {4, 5, 6, 7, 8}
# print(f'Два множества равны: {first_set == second_set}')

# N54:
# f_set = {4,2,3,8,5}
# s_set = {1,2,3,4,5}
# print(f'Элементы, которые есть в обоих множествах: {f_set.intersection(s_set)}')

# N55:
# fr_set = {3, 5, 7, 9}
# sc_set = {1, 2, 3, 4, 5}
# print(f'Элементы, которые есть в первом множестве, но отсутствуют во втором: {fr_set.difference(sc_set)}')

# N56:
# def char_frequency(text):
#     freq = {}
#     for char in text:
#         freq[char] = freq.get(char, 0) + 1
#     return freq
# print(char_frequency("My name is Iskander and I am a Python developer"))

# N57:
# def word_frequency(text):
#     freq = {}
#     words = text.split()
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     return freq

# print(word_frequency("My name is Iskander and I am a Python developer. Thsis is a test"))

# N58:
# def telephone_directory(contacts):
#     directory = {}
#     for name, number in contacts:
#         directory[name] = number
#     return directory
# contacts = [("Alice", "123-456-7890"), ("Bob", "987-654-3210"), ("Charlie", "555-555-5555")]
# print(telephone_directory(contacts))

# N59:
# def max_key(dictionary):
#     if not dictionary:
#         return None
#     max_key = max(dictionary, key=dictionary.get)
#     return max_key
# print(max_key({"a": 5, "b": 10, "c": 3}))

# N60:
# def reversed_dict(dictionary):
#     reversed_dict = {}
#     for key, value in dictionary.items():
#         reversed_dict[value] = key
#     return reversed_dict
# dict = {"a": 1, "b": 2, "c": 3}
# print(reversed_dict(dict))

# N61:
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# N62:
# def prime_num(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(prime_num(int(input('Введите число: '))))

# N63:
# def find_NOD(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# print(find_NOD(int(input('Введите число 1: ')), int(input('Введите число 2: '))))

# N64:
# def power(base, exponent):
#     return base ** exponent
# print(power(int(input('Введите основание: ')), int(input('Введите показатель степени: '))))

# N65:
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))
# print(sum_of_digits(int(input('Введите число: '))))

# N66:
# def max_in_list(lst):
#     if not lst:
#         return None
#     max_num = lst[0]
#     for num in lst:
#         if num > max_num:
#             max_num = num
#     return max_num
# lst = [3, 5, 2, 8, 1]
# print(max_in_list(lst))

# N67:
# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     return s == s[::-1]
# print(is_palindrome(input('Введите строку: ')))

# N68:
# def sort_list(lst):
#     return sorted(lst)
# print(sort_list([3, 1, 4, 2, 5]))

# N69:
# def generate_squares(n):
#     return [i**2 for i in range(1, n + 1)]
# print(generate_squares(int(input('Введите число N: '))))

# N70:
# def count_words(n):
#     return len(n.split())
# print(count_words(input('Введите строку: ')))

# N71:
# def factorial(n):
#     if n<1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# num = int(input('введите число: '))
# print(factorial(num))

# N72:
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(int(input('Введите число N: '))))

# N73:
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n - 1)
# print(sum(int(input('Введите число N: ')))) 

# N74:
# def reverse_string(num):
#     if len(num) == 0:
#         return num
#     else:
#         return num[-1] + reverse_string(num[:-1])
# print(reverse_string(input('Введите число: ')))

# N75:
# def is_palindrome_recursive(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome_recursive(s[1:-1])
# print(is_palindrome_recursive(input('Введите строку: ')))


# N86:
# class Student:
#     def __init__(self, name:str, age:int, student_id:int):
#         self.name = name
#         self.age = age
#         self.student_id = student_id
#         self.grades: list[float] = []

#     @property
#     def age(self) -> int:
#         return self._age

#     @age.setter
#     def age(self, value:int):
#         if not isinstance(value, int) or value <= 0:
#             raise ValueError("Возраст должен быть положительным целым числом.")
#         self._age = value

#     def add_grade(self, grade: float):
#         if isinstance(grade, (int, float)) and 1 <= grade <= 5:
#             self.grades.append(float(grade))
#         else:
#             raise ValueError("Оценка должна быть числом от 1 до 5.")

#     def get_average_grade(self) -> float:
#         if not self.grades:
#             return 0.0
#         return round(sum(self.grades) / len(self.grades), 2)

#     def __str__(self) -> str:
#         avg = self.get_average_grade()
#         return f"Student: name={self.name}, age={self.age}, student_id={self.student_id}, average_grade={avg})"

# try:
#     student = Student("Alice", 20, 12345)
#     student.add_grade(4.5)
#     student.add_grade(3.7)

#     print(student)
#     print(f"all grades: {student.grades}")
# except ValueError as e:
#     print(f"Error: {e}")

# N87:
# class Rectangle:
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height

#     def get_area(self) -> float:
#         return self.width * self.height

# try:
#     rect = Rectangle(5.0, 3.0)
#     area = rect.get_area()
#     print(f"Area of the rectangle: {area}")
# except Exception as e:
#     print(f"An error occurred: {e}")

# N88:
# class BankAccount:
#     def __init__(self, acc_num: str, balance: float = 0.0):
#         self.acc_num = acc_num
#         self.balance = balance

#     def deposit(self, amount: float):
#         if amount > 0:
#             self.balance += amount
#         else:
#             raise ValueError("Сумма депозита должна быть положительной")

#     def withdraw(self, amount: float):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#         else:
#             raise ValueError("Недостаточно средств или неверная сумма снятия")

#     def get_balance(self) -> float:
#         return self.balance

# try:
#     account = BankAccount("123456789", 1000.0)
#     account.deposit(-500.0)
#     account.withdraw(200.0)
#     print(f"Current balance: {account.get_balance()}")
# except ValueError as e:
#     print(f"Error: {e}")

# N89:
# class Car:
#     def __init__(self, make: str, model: str, year: int):
#         self.make = make
#         self.model = model
#         self.year = year

#     def __str__(self) -> str:
#         return f"Car: {self.year} {self.make} {self.model}"

# try:
#     car = Car("Toyota", "Camry", 2020)
#     print(car)
# except Exception as e:
#     print(f"An error occurred: {e}")

# N90:
# class User:
#     def __init__(self, username: str, email: str, age: int, password: str):
#         self.username = username
#         self.email = email
#         self.age = age
#         self.__password_hash = self.__hash_password(password)

#     @property
#     def username(self) -> str:
#         return self._username

#     @username.setter
#     def username(self, value:str):
#         if not isinstance(value, str) or len(value.strip()) < 3:
#             raise ValueError("Username must be a string with at least 3 characters")
#         self._username = value.strip()

#     @property
#     def email(self) -> str:
#         return self._email

#     @email.setter
#     def email(self, value:str):
#         if not isinstance(value, str):
#             raise ValueError("Email must be a string")
#         value = value.lower().strip()

#         if "@" not in value or "." not in value:
#             raise ValueError("Email must contain '@' and '.'")
#         if value.count("@") != 1:
#             raise ValueError("Email must contain exactly one '@'")
#         username_part, domain_part = value.split("@")
#         if not username_part or not domain_part:
#             raise ValueError("Email must have a username and domain part")
#         if '.' not in domain_part:
#             raise ValueError("Domain part must contain a '.'")

#         self._email = value        

#     @property
#     def age(self) -> int:
#         return self._age

#     @age.setter
#     def age(self, value:int):
#         if not isinstance(value, int) or not (0 < value <= 120):
#             raise ValueError("Age must be a positive integer between 1 and 120")
#         self._age = value

#     def __hash_password(self, password: str) -> str:
#         if not isinstance(password, str) or len(password) < 6:
#             raise ValueError("Password must be a string with at least 6 characters")
#         return password[::-1]  + "_hashed"

#     def check_password(self, password: str) -> bool:
#         return self.__password_hash == self.__hash_password(password)

#     def change_password(self, old_password: str, new_password: str):
#         if not self.check_password(old_password):
#             raise PermissionError("Old password is incorrect")
#         self.__password_hash = self.__hash_password(new_password)
#         print("Password changed successfully")

#     def __str__(self) -> str:
#         return f"User( username = '{self.username}', email = '{self.email}', age = {self.age})"

# try:
#     user = User(username="john_doe", email="john_doe@example.com", age=30, password="password123")
#     print("User created successfully", user)

#     print(f"Email: {user.email}")
#     user.age = 31
#     print(f"Updated age: {user.age}")
#     # user.email = "invalid_email" # ValueError: Email must contain '@' and '.'
#     # print(user.__password_hash) # AttributeError: 'User' object has no attribute '__password_hash'
#     print("Password is correct -", user.check_password("password123"))
#     user.change_password("password123", "newpass456")

# except Exception as e:
#     print(f"An error occurred: {e}")

# N91:
# class Animal:
#     def __init__(self, name: str, species: str, age: int):
#         self.name = name
#         self.species = species
#         self.age = age

#     @property
#     def name(self) -> str:
#         return self._name   

#     @name.setter
#     def name(self, value: str):
#         if not isinstance(value, str) or not value.strip():
#             raise ValueError("Name must be a non-empty string")
#         self._name = value.strip()

#     @property
#     def species(self) -> str:
#         return self._species

#     @species.setter
#     def species(self, value: str):
#         if not isinstance(value, str) or not value.strip():
#             raise ValueError("Species must be a non-empty string")
#         self._species = value.strip()

#     @property
#     def age(self) -> int:
#         return self._age

#     @age.setter
#     def age(self, value: int):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("Age must be a positive integer")
#         self._age = value

#     def make_sound(self) -> str:
#         return "Unknown sound"
#     def __str__(self) -> str:
#         return f"Animal: name = '{self.name}', species = '{self.species}', age = {self.age}"

# class Dog(Animal):
#     def __init__(self, name:str, age:int, breed:str):
#         super().__init__(name, "Dog", age)
#         self.breed = breed

#     @property
#     def breed(self) -> str:
#         return self._breed

#     @breed.setter
#     def breed(self, value: str):
#         if not isinstance(value, str) or not value.strip():
#             raise ValueError("Breed must be a non-empty string")
#         self._breed = value.strip()

#     def make_sound(self) -> str:
#         return "Woof!"

#     def fetch(self, item: str) -> str:
#         return f"{self.name} is fetching the {item}!"

#     def __str__(self) -> str:
#         return f"Dog: name = '{self.name}', breed = '{self.breed}', age = {self.age}"

# try:
#     gen_animal = Animal("Generic", "Unknown", 5)
#     print(gen_animal)
#     print(f"{gen_animal.name} makes sound: {gen_animal.make_sound()}\n")

#     dog = Dog("Buddy", 3, "Golden Retriever")
#     print(dog)
#     print(f"Sound: {dog.make_sound()}")
#     print(dog.fetch("ball"))

# except Exception as e:
#     print(f"An error occurred: {e}")

# N92:
# class Vehicle:
#     def start_engine(self) -> str:
#         return "Engine started"

# class ElectricCar(Vehicle):
#     def start_engine(self) -> str:
#         parent_msg = super().start_engine()
#         return f"{parent_msg} and the electric battery is now active (silent start)"

# car = ElectricCar()
# print(car.start_engine())

# N93:
# import math

# class Shape:
#     def area(self) -> float:
#         raise NotImplementedError("Subclasses must implement the area method")

# class Rectangle(Shape):
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius

#     def area(self) -> float:
#         return math.pi * (self.radius ** 2)

# shapes: list[Shape] = [Rectangle(10,5), Circle(3), Rectangle(2,4)]
# for shape in shapes:
#     print(f"Area of {shape.__class__.__name__}: {shape.area():.2f}")

# N94:
# class Employee:
#     def __init__(self, name: str, position: str, employee_id: str):
#         self.name = name
#         self.position = position
#         self.employee_id = employee_id

#     def calculate_salary(self) -> float:
#         raise NotImplementedError("Subclasses must implement the calculate_salary method")

# class SalariedEmployee(Employee):
#     def __init__(self, name:str, position:str, employee_id:str, monthly_salary:float):
#         super().__init__(name, position, employee_id)
#         self.monthly_salary = monthly_salary

#     def calculate_salary(self) -> float:
#         return self.monthly_salary

# class HourlyEmployee(Employee):
#     def __init__(self, name:str, position:str, employee_id:str, hourly_rate:float, hours_worked:float):
#         super().__init__(name, position, employee_id)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_salary(self) -> float:
#         return self.hourly_rate * self.hours_worked

# employees: list[Employee] = [
#     SalariedEmployee("Alice", "Manager", "E001", 5000.0),
#     HourlyEmployee("Bob", "Developer", "E002", 20.0, 160),
#     SalariedEmployee("Charlie", "Designer", "E003", 4000.0),
#     HourlyEmployee("Diana", "Tester", "E004", 18.0, 150)
# ]
# for emp in employees:
#     print(f"{emp.name} ({emp.position}) - Salary: ${emp.calculate_salary():.2f}")   

# N95:
# class Book:
#     def __init__(self, title: str, author: str, publication_year: int, isbn: str):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.isbn = isbn
#         self.is_available = True

#     def get_info(self) -> str:
#         status = "Available" if self.is_available else "Checked out"
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Status: {status}"

# class Reader:
#     def __init__(self, name: str, reader_id: str):
#         self.name = name
#         self.reader_id = reader_id
#         self.borrowed_books: list[Book] = []

#     def borrow_book(self, book: Book) -> str:
#         if book.is_available:
#             book.is_available = False
#             self.borrowed_books.append(book)
#             return f"{self.name} borrowed '{book.title}'"
#         else:
#             return f"'{book.title}' is not available for borrowing"

#     def return_book(self, book: Book) -> str:
#         if book in self.borrowed_books:
#             book.is_available = True
#             self.borrowed_books.remove(book)
#             return f"{self.name} returned '{book.title}'"
#         else:
#             return f"{self.name} did not borrow '{book.title}'"

#     def __str__(self) -> str:
#         borrowed_titles = ', '.join(book.title for book in self.borrowed_books) if self.borrowed_books else "No books borrowed"
#         return f"Reader: {self.name}, ID: {self.reader_id}, Borrowed Books: {borrowed_titles}"

# class Library:
#     def __init__(self):
#         self.books: list[Book] = []
#         self.readers: list[Reader] = []

#     def add_book(self, book: Book):
#         self.books.append(book)

#     def add_reader(self, reader: Reader):
#         self.readers.append(reader)

#     def find_book(self, title: str) -> Book | None:
#         for book in self.books:
#             if book.title == title:
#                 return book
#         return None

#     def find_reader(self, reader_id: str) -> Reader | None:
#         for reader in self.readers:
#             if reader.reader_id == reader_id:
#                 return reader
#         return None

#     def issue_book(self, isbn: str, reader: Reader) -> bool:
#         for book in self.books:
#             if book.isbn == isbn:
#                 if not book.is_available:
#                     print(f"Book '{book.title}' is currently not available.")
#                     return False
#                 book.is_available = False
#                 reader.borrowed_books.append(book)
#                 print(f"Book '{book.title}' issued to {reader.name}.")
#                 return True
#         print(f"No book with ISBN '{isbn}' found in the library.")
#         return False

#     def return_book(self, isbn: str, reader: Reader) -> bool:
#         for book in reader.borrowed_books:
#             if book.isbn == isbn:
#                 book.is_available = True
#                 reader.borrowed_books.remove(book)
#                 print(f"Book '{book.title}' returned by {reader.name}.")
#                 return True
#         print(f"{reader.name} did not borrow a book with ISBN '{isbn}'.")
#         return False

# lib = Library()
# book1 = Book("1984", "George Orwell", 1949, "978-0-45-152493-5")
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "978-0-06-112008-4")
# lib.add_book(book1)
# lib.add_book(book2)

# reader_alice = Reader("Alice", "R001")
# lib.add_reader(reader_alice)

# lib.issue_book("978-0-45-152493-5", reader_alice)
# lib.issue_book("978-0-45-152493-5", reader_alice)
# print(reader_alice)
# lib.return_book("978-0-45-152493-5", reader_alice)

# N96:
# def main():
#     students = {}
#     print("=== The system for managing student grades ===")

#     while True:
#         try:
#             num_students = int(input("Enter the number of students to add (or 0 to finish): "))
#             if num_students >0:
#                 break
#             print("Please enter a positive integer")
#         except ValueError:
#             print("Invalid input. Please enter a valid integer")
#     for i in range(1, num_students + 1):
#         name = input(f"\nEnter the name of student №{i}: ").strip()
#         while not name:
#             print("Name cannot be empty. Please enter a valid name")
#             name = input(f"Enter the name of student №{i}: ").strip()
#         grades = []
#         print(f"Enter grades for {name} (enter 'stop' or push Enter to finish):")
#         while True:
#             raw_input = input("  Grade: ").strip()
#             if raw_input.lower() == 'stop' or raw_input == '':
#                 if not grades:
#                     print("  At least one grade is required. Please enter a grade")
#                     continue
#                 break
#             try:
#                 grade = float(raw_input)
#                 if 1 <= grade <= 5:
#                     grades.append(grade)
#                 else:
#                     print("  Grade must be between 1 and 5. Please try again")
#             except ValueError:
#                 print("  Invalid input. Please enter a numeric grade between 1 and 5 or 'stop' to finish") 

#         students[name] = grades

#     print("\n=== Student Grades Summary ===")
#     print("\n" + "="*40)
#     print("="*40)

#     best_student = None
#     max_average = 1.0

#     for name, grades in students.items():
#         avg_grade = sum(grades) / len(grades)
#         print(f"\nStudent: {name:<15} | Grades: {grades} | Average: {avg_grade:.2f}")
#         if avg_grade > max_average:
#             max_average = avg_grade
#             best_student = name

#     print("\n" + "="*40)
#     print("="*40)
#     print(f"\nThe student with the highest average grade is: {best_student} with an average of {max_average:.2f}")

# if __name__ == "__main__":
#     main()

# N97:
# def main():
#     print("=== Attendance Tracking System ===")
#     group_students = [
#         'Michael Olise',
#         'Joshua Kimmich',
#         'Jude Bellingham',
#         'Jamal Musiala',
#         'Harry Kane'
#     ]

#     attendance = {student: False for student in group_students}
#     print("\nEnter the names of students who are present:")
#     print("(Enter '1' - present, '0' - absent)\n")

#     for student in group_students:
#         while True:
#             status = input(f"{student}: ").strip()
#             if status == '1':
#                 attendance[student] = True
#                 break
#             elif status == '0':
#                 attendance[student] = False
#                 break
#             else:
#                 print("Invalid input. Please enter '1' for present or '0' for absent.")
#     present_students = [name for name, is_present in attendance.items() if is_present]
#     absent_students = [name for name, is_present in attendance.items() if not is_present]

#     print("\n" + "="*40)
#     print("\n=== Attendance Summary ===")
#     print("\n" + "="*40)

#     print(f"\nTotal students: {len(group_students)}")
#     print(f"Present: {len(present_students)}")
#     print(f"Absent: {len(absent_students)}")

#     print("\nList of present students:")
#     if present_students:
#         for name in present_students:
#             print(f" - {name}")
#     else:
#         print("  No students are present.")

#     print("\nList of absent students:")
#     if absent_students:
#         for name in absent_students:
#             print(f" - {name}")
#     else:
#         print("  all students are present.")

# if __name__ == "__main__":
#     main()

# N98:
# def print_menu_list(menu: dict):
#     print("\n" + "=" * 40)
#     print("          RESTAURANT MENU")
#     print("=" * 40)
    
#     if not menu:
#         print("   (The menu is currently empty)")
#     else:
#         print(f"{'#':<3} {'Dish Name':<25} {'Price ($)':>10}")
#         print("-" * 40)
#         for i, (dish, price) in enumerate(menu.items(), 1):
#             print(f"{i:<3} {dish:<25} {price:>10.2f}")
            
#     print("=" * 40)


# def get_positive_float(prompt: str) -> float:
#     while True:
#         try:
#             value = float(input(prompt).strip())
#             if value >= 0:
#                 return value
#             print("Price cannot be negative.")
#         except ValueError:
#             print("Error: Please enter a valid numerical value.")


# def main():
#     restaurant_menu = {
#         "Margherita Pizza": 12.50,
#         "Pasta Carbonara": 14.00,
#         "Caesar Salad": 9.50,
#         "Caffe Latte": 4.00
#     }

#     while True:
#         print("\n=== MENU MANAGEMENT ===")
#         print("1. View Menu")
#         print("2. Add a Dish")
#         print("3. Update Dish Price")
#         print("4. Delete a Dish")
#         print("0. Exit Program")

#         choice = input("\nSelect an option (0-4): ").strip()

#         if choice == "1":
#             print_menu_list(restaurant_menu)

#         elif choice == "2":
#             dish_name = input("\nEnter the name of the new dish: ").strip().title()
#             if not dish_name:
#                 print("Dish name cannot be empty.")
#                 continue

#             if dish_name in restaurant_menu:
#                 print(f"'{dish_name}' is already on the menu! Use option 3 to update its price.")
#             else:
#                 price = get_positive_float(f"Enter price for '{dish_name}': ")
#                 restaurant_menu[dish_name] = price
#                 print(f"'{dish_name}' added successfully for ${price:.2f}!")

#         elif choice == "3":
#             if not restaurant_menu:
#                 print("\nMenu is empty. Nothing to update.")
#                 continue

#             dish_name = input("\nEnter dish name to update price: ").strip().title()
#             if dish_name in restaurant_menu:
#                 current_price = restaurant_menu[dish_name]
#                 print(f"Current price for '{dish_name}': ${current_price:.2f}")
#                 new_price = get_positive_float("Enter new price: ")
#                 restaurant_menu[dish_name] = new_price
#                 print(f"Price for '{dish_name}' updated to ${new_price:.2f}.")
#             else:
#                 print(f"'{dish_name}' not found in the menu.")

#         elif choice == "4":
#             if not restaurant_menu:
#                 print("\nMenu is empty. Nothing to delete.")
#                 continue

#             dish_name = input("\nEnter dish name to remove: ").strip().title()
#             if dish_name in restaurant_menu:
#                 del restaurant_menu[dish_name]
#                 print(f"'{dish_name}' has been removed from the menu.")
#             else:
#                 print(f"'{dish_name}' not found in the menu.")

#         elif choice == "0":
#             print("\nExiting program. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a number from 0 to 4.")


# if __name__ == "__main__":
#     main()

# N99:
# def analyze_txt(text: str):
#     text = text.strip()
#     if not text:
#         print("No text provided")
#         return

#     char_without_spaces = len(
#         text.replace(" ", "").replace("\n","").replace("\t", "")
#     )

#     sentence_count = 0
#     in_punctuation_block = False
#     for ch in text:
#         if ch in ".!?":
#                 if not in_punctuation_block:
#                     sentence_count +=1
#                     in_punctuation_block = True
#                 else:
#                     in_punctuation_block = False

#     if sentence_count == 0 and len(text)>0:
#         sentence_count = 1
    
#     punctuation = '.,!?:;-"\'()[]{}<>_'
#     clean_txt = text
#     for char in punctuation:
#         clean_txt = clean_txt.replace(char, " ")

#     words = clean_txt.split()
#     word_count = len(words)
#     if words:
#         shortd_word = min(words, key=len)
#     else:
#         shortd_word = "-"

#     print("\n" + "="*40)
#     print("             ANALYSIS RESULTS")
#     print("="*40)
#     print(f"~ Sentence count:                   {sentence_count}")
#     print(f"~ Word count:                       {word_count}")
#     print(f"~ Characters (no spaces):           {char_without_spaces}")
#     print(f"~ Sortest word:                     '{shortd_word}' (length: {len(shortd_word)})")
#     print("="*40)

# if __name__ == "__main__":
#     user_text = input("Enter text for analysis:\n")
#     analyze_txt(user_text)

# N100:
# class Product:
#     def __init__(self, name: str, price: int, quantity: int):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def set_price(self, new_price:float)->None:
#         if new_price <0:
#             print("Error: The price cannot be negative")
#             return
#         old_price = self.price
#         self.price = new_price
#         print(f"Price for '{self.name}' updated: ${old_price:.2f} --> ${self.price:.2f}")

#     def restock(self, amount:int) -> None:
#         if amount <= 0:
#             print("Error: Restock amount must be greater than zero!")
#             return
#         self.quantity += amount
#         print(f"Restocked! '{self.name}': +{amount} pcs (Total: {self.quantity} pcs)")

#     def buy(self, amount: int) -> bool:
#         if amount <= 0:
#             print("Error: Purchase amount must be greater than zero!")
#             return False
#         if amount > self.quantity:
#             print(f"Not enough stock for '{self.name}'! Requested: {amount}, available: {self.quantity}")
#             return False

#         self.quantity -= amount
#         total_cost = amount * self.price
#         print(f"Purchase successful! Bought '{self.name}': {amount} pcs for ${total_cost:.2f}")
#         print(f"Remaining stock: {self.quantity} pcs")
#         return True

#     def get_info(self):
#         print("\n"+"="*40)
#         print("             PRODUCT INFORMATION")
#         print("="*40)
#         print(f"~ Name:             {self.name}")
#         print(f"~ Price:            {self.price:.2f}")
#         print(f"~ Stock Quantity:   {self.quantity} pcs")
#         print("="*40+"\n")

# if __name__ == "__main__":
#     laptop = Product(name="Gaming Laptop", price=1200, quantity=10)
#     laptop.get_info()
#     laptop.set_price(1099.99)
#     laptop.buy(3)
#     laptop.get_info()
#     laptop.buy(10)
#     laptop.restock(5)
#     laptop.get_info()