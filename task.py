# N1:
name = input("Введите своё имя: ")
print(f'Привет, {name}')

# N2:
age = int(input("Введите свой возраст: "))
print(f'Через 10 лет вам будет {age + 10} лет')

# N3:
n = int(input("Введите число n: "))
nn = int(input("Введите число nn: "))
print(f'Сумма чисел n и nn равна {n + nn}')

# N4:
n1 = int(input("Введите число n1: "))
n2 = int(input("Введите число n2: "))
print(f'Сумма чисел n1 и n2 равна {n1 + n2}')
print(f'Разность чисел n1 и n2 равна {n1 - n2}')
print(f'Произведение чисел n1 и n2 равно {n1 * n2}')
print(f'Частное чисел n1 и n2 равно {n1 / n2}')

# N5:
a = int(input("Введите длину a: "))
b = int(input("Введите ширину b: "))
print(f'Площадь прямоугольника равна {a * b}')

# N6:
r = int(input("Введите радиус r: "))
print(f'Площадь круга равна {3.14 * r ** 2}')

# N7:
t = int(input("Введите температуру в градусах Цельсия: "))
f = (t * 9/5) + 32
print(f'Температура в градусах Фаренгейта равна {f}')

# N8:
s = int(input("Введите секунды: "))
h = s // 3600
m = (s % 3600) // 60
print(f'Время в формате чч:мм:сс равно {h:02}:{m:02}:{s % 60:02}')

# N9:
q = int(input("Введите число q: "))
p = int(input("Введите число p: "))
q, p = p, q
print(f'После обмена значений: q = {q}, p = {p}')

# N10:
user_inp = input("Введите строку: ")
try:
    int_val = int(user_inp)
    print(f'Преобразование в int | Значение: {int_val}, тип: {type(int_val)}')
except ValueError:
    print("Преобразование в int невозможно")

try:
    float_val = float(user_inp)
    print(f'Преобразование в float | Значение: {float_val}, тип: {type(float_val)}')
except ValueError:
    print("Преобразование в float невозможно")

str_val = str(user_inp)
print(f'Преобразование в str | Значение: \'{str_val}\', тип: {type(str_val)}')  

# N11:
i = int(input("Введите целое число i: "))
if i > 0:
    print("Число положительное")
elif i < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# N12:
num = int(input("Введите целое число: "))
if num % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

# N13:
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num1 > num2:
    print(f'Большее число: {num1}')
elif num2 > num1:
    print(f'Большее число: {num2}')
else:
    print("Числа равны")

# N14:
frst = int(input("Введите первое число: "))
scnd = int(input("Введите второе число: "))
thrd = int(input("Введите третье число: "))
print(f'Наибольшее число: {max(frst, scnd, thrd)}')

# N15:
number = int(input("Введите число: "))
if number % 3 == 0 and number % 5 == 0:
    print("число делится на 3 и на 5")
else:
    print("число не делится на 3 и на 5")

# N16:
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год является високосным")
else:
    print("Год не является високосным")

# N17:
user_age = int(input("Введите ваш возраст: "))
if user_age < 13:
    print("Вы ребёнок")
elif user_age < 20:
    print("Вы подросток")
elif user_age < 65:
    print("Вы взрослый")
else:
    print("Вы пенсионер")

# N18:
login = input("Введите логин: ")
password = input("Введите пароль: ")
if login == "admin" and password == "1234":
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

# N19:
month_num = int(input("Введите номер месяца (1-12): "))
try:
    if month_num < 1 or month_num > 12:
        raise ValueError("Номер месяца должен быть в диапазоне от 1 до 12")
except ValueError as e:
    print(e)
    exit()
if month_num in [12, 1, 2]:
    print("Зима")
elif month_num in [3, 4, 5]:
    print("Весна")
elif month_num in [6, 7, 8]:
    print("Лето")
else:
    print("Осень")

# N20:
a_triangle = int(input("Введите длину стороны треугольника: "))
b_triangle = int(input("Введите длину другой стороны треугольника: "))
c_triangle = int(input("Введите длину третьей стороны треугольника: "))
if a_triangle + b_triangle > c_triangle and a_triangle + c_triangle > b_triangle and b_triangle + c_triangle > a_triangle:
    print("Треугольник существует")
else:
    print("Треугольник не существует")

# N21:
for i in range(1, 101):
    print(i)
# N22:
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
# N23:
for i in range(100, 0, -1):
    print(i)
# N24:
N = int(input("Введите число N: "))
s = 0
for i in range(1, N + 1):
    s += i
print(f"Сумма чисел от 1 до {N} = {s}")
# N25:
product = 1
NN = int(input("Введите число NN: "))
for i in range(1, NN + 1):
    product *= i
print(f"Произведение чисел от 1 до {NN} = {product}")
# N26:
number = int(input("Введите число: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# N27:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
# N28:
c = 0
for i in range(1, 101):
    if i % 3 == 0:
        c += 1
print(f"Количество чисел от 1 до 100, которые делятся на 3: {c}")
# N29:
NNN = int(input("Введите число NNN: "))
sum_of_odd = 0
for i in range(1, NNN + 1):
    if i % 2 != 0:
        sum_of_odd += i
print(f"Сумма нечётных чисел от 1 до {NNN} = {sum_of_odd}")
# N30:
for i in range(1, 21):
    print(f"{i}^2 = {i ** 2}")

# N31:
while True:
    for i in range(1, 101):
        print(i)
    break

# N32:
while True:
    password = input("Введите пароль: ")
    if password == "secret":
        print("Доступ разрешён")
        break
    print("Неверный пароль, попробуйте снова")

# N33:
while True:
    number = int(input("Введите число: "))
    if number == 0:
        print("Вы ввели ноль, программа завершена")
        break
    print(f"Вы ввели число: {number}")

# N34:
while True:
    s = 0
    num = int(input("Введите число: "))
    if num == 0:
        print("Вы ввели ноль, программа завершена")
        break
    s += num
    print(f"Сумма введённых чисел: {s}")

# N35:
while True:
    us_num = int(input("Введите число: "))
    count_digit = 0
    for char in str(us_num):
        count_digit += 1
    print(f"Количество цифр в числе {us_num} равно {count_digit}")
    break

# N36:
while True:
    us_num = int(input("Введите число: "))
    sum_of_digits = 0
    for digit in str(us_num):
        sum_of_digits += int(digit)
    print(f"Сумма цифр числа {us_num} равна {sum_of_digits}")
    break

# N37:
while True:
    us_num = int(input("Введите число: "))
    reverse_num = 0
    while us_num > 0:
        reverse_num = (reverse_num * 10) + (us_num % 10)
        us_num //= 10
    print(f"Обратное число: {reverse_num}")
    break

# N38:
while True:
    us_num = int(input("Введите число: "))
    is_palindrome = str(us_num) == str(us_num)[::-1]
    if is_palindrome:
        print(f"Число {us_num} является палиндромом")
    else:
        print(f"Число {us_num} не является палиндромом")
    break

# N39:
while True:
    secret_number = 42
    user_guess = int(input("Угадайте число от 1 до 100: "))
    if user_guess < secret_number:
        print("Загаданное число больше, попробуйте снова")
    elif user_guess > secret_number:
        print("Загаданное число меньше, попробуйте снова")
    else:
        print("Поздравляем! Вы угадали число!")
        break

# N40:
while True:
    us_num = int(input("Введите число: "))
    if us_num > 0:
        print("Вы ввели положительное число, программа завершена")
        break
    print("Вы ввели отрицательное число, попробуйте снова")

# N41:
us_str = input("Введите строку: ")
print(f"количество символов: {len(us_str)}")

# N42:
us_str = input("Введите строку: ")
print(f'количество букв "a" в строке: {us_str.count("a")}')

# N43:
us_str = input("Введите строку: ")
result = us_str[::-1]
print(f'обратная строка: {result}')

# N44:
us_str = input("Введите строку: ")
reserved_str = us_str[::-1]
is_palindrome = us_str == reserved_str
if is_palindrome:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")

# N45:
us_str = input("Введите строку: ")
vowels = "aeiouAEIOU"
count_vowels = sum(1 for char in us_str if char in vowels)
print(f'Количество гласных букв в строке: {count_vowels}')

# N46:
us_str = input("Введите строку: ")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count_consonants = sum(1 for char in us_str if char in consonants)
print(f'Количество согласных букв в строке: {count_consonants}')

# N47:
us_str = input("Введите строку: ")
print(f'количество слов в строке: {len(us_str.split())}')

# N48:
us_str = input("Введите строку: ")
largest_word = max(us_str.split(), key=len)
print(f'самое длинное слово в строке: {largest_word}')

# N49:
us_str = input("Введите строку: ")
changed_str = us_str.replace(" ", "-")
print(f'строка с заменой пробелов на дефисы: {changed_str}')

# N50:
us_str = input("Введите строку: ")
key_word = input("Введите ключевое слово: ")
if key_word in us_str and us_str.startswith(key_word):
    print(f'строка начинается с ключевого слова "{key_word}"')

# N51:
listn = [1, 2, 3, 4, 5]
print(f'сумма элементов списка: {sum(listn)}')

# N52:
listn = [1, 2, 3, 4, 5]
max_value = 0
for i in listn:
    if i > max_value:
        max_value = i
print(f'наибольший элемент списка: {max_value}')

# N53:
listn = [1, 2, 3, 4, 5]
min_value = 0
for i in listn:
    if i < min_value:
        min_value = i
print(f'наименьший элемент списка: {min_value}')

# N54:
listn = [1, 2, 3, 4, 5]
count_even = sum(1 for i in listn if i % 2 == 0)
print(f'количество чётных чисел в списке: {count_even}')

# N55:
listn = [1, 2, 3, 4, 5]
odd_list = [i for i in listn if i % 2 != 0]
print(f'список нечётных чисел: {odd_list}')

# N56:
listn = [-1, 2, -3, 4, 5]
pos_list = [i for i in listn if i > 0]
print(f'список положительных чисел: {pos_list}')

# N57:
listn = [1, 2, 3, 4, 5]
reserved_str = listn[::-1]
print(f'обратный список: {reserved_str}')

# N58:
listn = [1, 2, 3, 4, 5]
max_scnd_value = sorted(listn)[-2]
print(f'второй наибольший элемент списка: {max_scnd_value}')

# N59:
lst = [1,1,4,2,5,22,67,94,2,9]
lst_cleaned = list(set(lst))
print(f'список без дубликатов: {lst_cleaned}')

# N60:
ls1 = [1, 2, 3, 5]
ls2 = [4, 5, 6, 3]
common_elements = [i for i in ls1 if i in ls2]
print(f'общие элементы двух списков: {common_elements}')

# N61:
tupl = tuple((1, 5, 3, 2, 8, 22, 15, 77, 3, 4))
max_value = max(tupl)
print(f'наибольший элемент кортежа: {max_value}')

# N62:
lst = [2, 2, 1, 3, 4, 5, 1, 2]
st = set(lst)
print(f'множество уникальных элементов: {st}')

# N63:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1 & set2
print(f'общие элементы двух множеств: {common_elements}')

# N64:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
unique_elements_of_set1 = set1 - set2
print(f'уникальные элементы первого множества: {unique_elements_of_set1}')

# N65:
dict_user = {
    'name': 'Isko',
    'age': 16,
    'town': 'Nukus'
}
# N66:
dict_user['grade'] = '10th'
# N67:
dict_user.pop('age')
print(f'Обновленный словарь: {dict_user}')

# N68:
st = input("Введите строку: ")
dict_char_count = {}
for char in st:
    if char in dict_char_count:
        dict_char_count[char] += 1
    else:
        dict_char_count[char] = 1
print(f'Словарь с подсчетом символов: {dict_char_count}')

# N69:
sentence = input("Введите предложение: ")
dict_word_count = {}
words = sentence.split()
for word in words:
    if word in dict_word_count:
        dict_word_count[word] += 1
    else:
        dict_word_count[word] = 1
print(f'Словарь с подсчетом слов: {dict_word_count}')

# N70:
dict2 = {
    'a': 1,
    'b': 2,
    'c': 3
}
max_value = max(dict2.values())
maxval_key = [i for i in dict2.keys() if dict2[i]==max_value]
print(*maxval_key)

# N71:
def summ(a,b):
    return a+b
print(summ(5, 12))

# N72:
def check_if_even(n):
    if n%2==0:
        return True
    return False
print(check_if_even(1235423))

# N73:
def maks(a,b,c):
    mx=0
    for i in [a,b,c]:
        if i>mx:
            mx=i
    return mx
print(maks(1,3,7))

# N74:
def factorial(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(factorial(5))

# N75:
def is_prime(n:int) ->bool:
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2== 0 or n%3==0:
        return False
    i=5
    while i**2 <=n:
        if n%i == 0 or n%(i+2)==0:
            return False
        i+=6
    return True
print(is_prime(173))

# N76:
def count_vowel(s: str) ->int:
    c = 0
    vowels = 'aeouiAEOUI'
    for i in s:
        if i in vowels:
            c+=1
    return c
print(count_vowel('lol kek cheburek HAHAHAHAH'))

# N77:
def reverse(st: str) -> str:
    return st[::-1]
print(reverse('qwerty'))

# N78:
def avg_list(ls: list) -> float:
    if not ls:
        return 0.0
    return sum(ls) / len(ls)
nums = [2, 5, 12, 74, 22, 65]
print(avg_list(nums))

# N79:
def sum_of_nums(*args: float) -> float:
    return sum(args)
print(sum_of_nums(12,7,99,35,74))

# N80:
def us_info(**kwargs)->str:
    if not kwargs:
        return 'User information not provided'
    prof_lines = ["--- User Profile ---"]
    for key, val in kwargs.items():
        format_key = key.replace("_",' ').capitalize()
        prof_lines.append(f"{format_key}: {val}")
    return "\n".join(prof_lines)
user1 = us_info(name="Isko", age=16)
print(user1)
print("\n" + "=" * 30 + "\n")

user2 =us_info(
    first_name="Jack",
    last_name="Smith",
    role="Developer",
    city="New-york",
    is_active=True,
    skills=["Python", "Git", "SQL"],
)
print(user2)

# N81:
squares = [i**2 for i in range(1,21)]
print(squares)