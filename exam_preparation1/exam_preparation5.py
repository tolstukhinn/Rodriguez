
# Задача 1 (Операции сравнения).
# Создайте переменные:
# x = 15
# y = 25
# Напишите код, который выводит результаты всех шести операций сравнения между x и y (>, <, ==, !=, >=, <=).
# Каждый результат выводите на отдельной строке в формате:
# x > y: False
# x < y: True
# Используйте f-строки.

x = 15
y = 25
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Задача 2 (Списки: срезы).
# Создайте список:
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Напишите код, который с помощью срезов выводит:
# Первые 3 элемента
# Последние 3 элемента
# Каждый второй элемент, начиная с первого (т.е. Элементы с чётными индексами: 0, 2, 4...)
# Каждый вывод — на отдельной строке, в виде списка.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[0:3])
print(numbers[-3:])
print(numbers[0::2])

# Задача 3 (Функции: аргументы с дефолтными значениями).
# Создайте функцию make_coffee, которая принимает три аргумента:
# type (вид кофе, обязательный)
# size (размер, по умолчанию "medium")
# sugar (сахар, по умолчанию True)
# Функция должна возвращать строку в формате:
# "Кофе: [type], Размер: [size], Сахар: [sugar]".
# Вызовите функцию три раза и выведите результаты:
# Только с обязательным аргументом "espresso"
# С двумя аргументами "latte", "large"
# Со всеми тремя аргументами "cappuccino", "small", False

def make_coffee(coffee_type, size = "medium", sugar = True):

    return f"Кофе: {coffee_type}, Размер: {size}, Сахар: {sugar}"

print(make_coffee("espresso"))
print(make_coffee("latte", size = "large"))
print(make_coffee("cappuccino", "small", False))

# Задача 4 (Словари: получение ключей, значений, элементов).
# Создайте словарь:
# car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
# Напишите код, который выводит:
# Все ключи словаря (в виде списка)
# Все значения словаря (в виде списка)
# Все пары ключ-значение (в виде списка кортежей)
# Каждый вывод — на отдельной строке. Используйте соответствующие методы словаря.

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "blue"}

print(car.keys())
print(car.values())
print(car.items())

# Задача 5 (Цикл for с range).
# Напишите код, который с помощью цикла for и функции range() выводит все чётные числа от 2 до 20 включительно.
# Каждое число должно выводиться на отдельной строке.
# Подсказка: используйте range() с тремя аргументами (start, stop, step).

for number in range(2,21,2):
    print(number)

# Задача 6 (ООП: создание класса, конструктор, методы).
# Создайте класс BankAccount с конструктором __init__, принимающим два параметра:
# owner (владелец счёта, строка)
# balance (баланс, число, по умолчанию 0)
# Сохраните их в атрибуты self.owner и self.balance.
# Добавьте два метода:
# deposit(amount) — увеличивает баланс на указанную сумму
# withdraw(amount) — уменьшает баланс на указанную сумму, но только если средств достаточно
# (если нет, выводит "Недостаточно средств")
# Создайте объект account = BankAccount("Иван", 1000).
# Проведите операции: положить 500, снять 300, снять 2000.
# Выведите итоговый баланс.
# Примечание: метод withdraw может выводить сообщение, но не должен возвращать None в случае неудачи.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств")

account = BankAccount(owner = "Иван", balance = 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
print(account.balance)

# Задача 7 (Логические операции в условиях).
# Создайте три переменные:
# is_weekend = True, is_sunny = False, has_money = True
# Напишите код, который выводит "Идём гулять", если:
# сегодня выходной (is_weekend) И хорошая погода (is_sunny)
# ИЛИ
# есть деньги (has_money) И хорошая погода (is_sunny)
# В противном случае выводит "Сидим дома".
# Используйте логические операторы and, or в одном условии if.

is_weekend = True
is_sunny = False
has_money = True

if is_weekend and is_sunny or has_money and is_sunny:
    print("Идём гулять")
else:
    print("Сидим дома")

# print("Идем гулять") if (is_weekend and is_sunny) or (has_money and is_sunny) else print("Сидим дома")

# Задача 8 (Работа с файлами: запись и чтение).
# Напишите код, который:
# Создаёт (или перезаписывает) файл task.txt в режиме записи ('w') с помощью with.
# Записывает в него строку "Выполнить задание"
# Закрывает файл (автоматически через with)
# Затем открывает тот же файл task.txt в режиме чтения ('r') с помощью with.
# Считывает всё содержимое и выводит его на экран
# Подсказка: используйте два отдельных блока with.

with open ("task.txt", "w") as f:
    f.write("Выполнить задание")
with open ("task.txt", "r") as f:
    print(f.read())

# Задача 9 (Строки: доступ к символам, длина, конкатенация).
# Даны две строки:
# str1 = "Python"
# str2 = "Programming"
# Напишите код, который:
# Выводит первый символ str1 и последний символ str2.
# Выводит длину обеих строк (каждую на отдельной строке)
# Создаёт новую строку result путём конкатенации str1, пробела и str2.
# Выводит result.
# Используйте индексацию, функцию len() и оператор +.

str1 = "Python"
str2 = "Programming"

print(str1[0])
print(str2[-1])
print(len(str1))
print(len(str2))
result = str1 + " " + str2
print(result)

# Задача 10 (Наследование: расширение функциональности).
# Создайте родительский класс Employee с конструктором __init__,
# принимающим name (имя) и salary (зарплата). Сохраните их в self.name и self.salary.
# Добавьте метод display_info, который возвращает строку "Имя: [name], Зарплата: [salary]".
# Создайте дочерний класс Manager, который наследует от Employee.
# В классе Manager:
# Добавьте конструктор __init__, принимающий name, salary и department (отдел).
# Используйте super().__init__(name, salary) для инициализации родительских атрибутов.
# Добавьте атрибут self.department.
# Переопределите display_info, чтобы возвращалась строка
# "Имя: [name], Зарплата: [salary], Отдел: [department]".
# Создайте объект manager = Manager("Анна", 80000, "IT") и вызовите display_info. Выведите результат.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}"
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_info(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}, Отдел: {self.department}"
manager = Manager("Анна", 80000, "IT")
print(manager.display_info())

# Задача 11 (Преобразование типов данных).
# У вас есть:
# num_str = "42" (строка)
# num_int = 8 (целое число)
# num_float = 3.14 (число с плавающей точкой)
# Напишите код, который:
# Преобразует num_str в целое число.
# Преобразует num_int в число с плавающей точкой.
# Преобразует num_float в целое число (отбрасывая дробную часть)
# Вычисляет сумму всех трёх преобразованных чисел.
# Выводит результат суммы
# Каждое преобразование должно быть отдельной операцией.

num_str = "42" #(строка)
num_int = 8 #(целое число)
num_float = 3.14 #(число с плавающей точкой)

num1 = int(num_str)
num2 = float(num_int)
num3 = int(num_float)
print(num1+num2+num3)

# Задача 12 (Условные операторы: if-elif-else).
# Создайте переменную grade = 85 (оценка).
# Напишите код, который выводит результат в соответствии с диапазонами:
# grade >= 90 → "Отлично"
# grade >= 75 → "Хорошо"
# grade >= 60 → "Удовлетворительно"
# grade < 60 → "Неудовлетворительно"
# Используйте цепочку if-elif-else.

grade = 85
if grade >= 90:
    print("Отлично")
elif grade >= 75:
    print("Хорошо")
elif grade >= 60:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")

# Задача 13 (Словари: добавление и обновление).
# Создайте словарь person = {"name": "Иван", "age": 30}.
# Напишите код, который:
# Добавляет ключ "city" со значением "Москва"
# Обновляет значение ключа "age" на 31.
# Удаляет ключ "name" (используйте метод или del)
# Выводит итоговый словарь

person = {
    "name": "Иван",
    "age": 30}

person["city"] = "Москва"
person["age"] = 31
person.pop("name")
print(person)

# Задача 14 (Цикл while с break).
# Напишите код, который с помощью цикла while выводит числа от 1 до 10, но прерывается, если число равно 5.
# Каждое число должно выводиться на отдельной строке.
# Подсказка: используйте условие if number == 5: break внутри цикла.

count = 0
while count < 10:
    count += 1
    if count == 5:
        break
    print(count)

# Задача 15 (Декоратор: простой пример).
# Создайте декоратор uppercase_result,
# который преобразует возвращаемое значение декорируемой функции в верхний регистр (если это строка).
# Декоратор должен работать с функциями, возвращающими строки.
# Примените декоратор к функции say_hello(), которая возвращает "hello, world!".
# Вызовите декорированную функцию и выведите результат.
# Подсказка: внутри wrapper вызовите func(), получите результат,
# примените к нему .upper() если это строка, и верните.

def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
@uppercase_result
def say_hello():
    return "hello, world!"
print(say_hello())
