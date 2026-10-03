
# N76:
# with open("example.txt", "r") as f:
#     lines = sum(1 for line in f)
# print(f"Number of lines in the file: {lines}")   

# N77:
# with open("example.txt", "r") as f:
#     words = sum(len(line.split()) for line in f)
# print(f"Number of words in the file: {words}")

# N78:
# with open("example.txt", "r") as f:
#     longest_line = max(f, key=len)
# print(f"The longest line in the file is: {longest_line.strip()}")

# N79:
# with open("example.txt", "r") as f:
#     with open("example2.txt", "w") as f2:
#         for line in f:
#             f2.write(line)

# N80:
# lst = [1, 2, 3, 4, 5]
# with open("example.txt", "rw") as f:
#     for item in lst:
#         f.write(f"{item}\n")
# with open("example.txt", "r") as f:
#     content = f.read()
# print(content)

# N81:
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))   

# if b != 0:
#     result = a / b
# else:
#     result = None
#     print("Ошибка: деление на ноль невозможно.")

# N82:
# def read_number(prompt: str = "Введите число: ") -> float:
#     user_input = input(prompt)
#     try:
#            return float(user_input)
#     except ValueError:
#             print("Ошибка: введите корректное число.")
# num = read_number()
# if num is not None:
#     print(f"Вы ввели число: {num}")

# N83:
# def safe_read_file(file_path: str) -> str:
#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         print(f"Ошибка: файл по пути '{file_path}' не найден.")
#     except PermissionError:
#         print(f"Ошибка: нет прав на чтение файла '{file_path}'.")
#     except UnicodeDecodeError:
#         print("Ошибка: не удалось декодировать файл (проверьте кодировку).")
#     except OSError as e:
#         print(f"Системная ошибка при работе с файлом: {e}")
#     return ''

# content = safe_read_file("example.txt")

# N84:
# def get_valid_integer(prompt: str = "Введите целое число: ") -> int:
#     while True:
#         user_input = input(prompt)
#         try:
#             return int(user_input)
#         except ValueError:
#             print("Ошибка: введите корректное целое число.")
# age = get_valid_integer("Введите ваш возраст: ")
# print(f"Вы ввели возраст: {age}")

# N85:
# def process_data(file_path: str):
#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             line = file.readline().strip()
#             num = float(line)
#             result = 100 /num
#             print(f"Результат деления 100 на {num} равен {result}")
#     except (ValueError, ZeroDivisionError) as e:
#         print(f"Математическая ошибка или ошибка формата данных: {e}")
#     except FileNotFoundError:
#         print(f"Ошибка: файл по пути '{file_path}' не найден.")
#     except Exception as e:
#         print(f"Произошла непредвиденная ошибка: {e}")

# process_data("example.txt")
