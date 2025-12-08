# Задача 1.
# Создайте класс Dog (Собака) с конструктором __init__,
# который принимает параметр name (имя) и сохраняет его в атрибут self.name.
# Добавьте метод bark, который выводит на экран строку: "[имя] говорит: Гав!".
# Создайте объект класса Dog с именем "Барсик" и вызовите его метод bark.

class Dog():
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} говорит: Гав!")

my_dog = Dog("Барсик")
my_dog.bark()

# Задача 2.
# Создайте класс Book (Книга) с конструктором __init__, который принимает два параметра:
# title (название книги)
# author (автор книги)
# Сохраните эти значения в атрибуты self.title и self.author.
# Добавьте метод get_info, который возвращает строку в формате: "Название: [title], Автор: [author]".
# Создайте объект класса Book с названием "Мастер и Маргарита" и автором "Булгаков".
# Выведите на экран результат вызова метода get_info для этого объекта.

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}"

my_book = Book("Мастер и Маргарита", "Булгаков")
print(my_book.get_info())

# Задача 3.
# Создайте класс BankAccount (Банковский счёт) с конструктором __init__, который принимает один параметр:
# owner (владелец счёта, строка)
# В конструкторе создайте атрибут self.balance и установите его значение в 0 (начальный баланс).
# Добавьте два метода:
# deposit(amount) — увеличивает баланс на указанную сумму amount
# get_balance() — возвращает текущий баланс.
# Создайте объект класса BankAccount с владельцем "Иван".
# Проведите операции:
# Внесите 1000 на счёт.
# Внесите ещё 500 на счёт.
# Выведите на экран итоговый баланс, используя метод get_balance().

class BankAccount():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def get_balance(self):
        return self.balance

my_bank_account = BankAccount("Иван")
my_bank_account.deposit(1000)
my_bank_account.deposit(500)
print(my_bank_account.get_balance())

# Задача 4.
# Создайте класс Student (Студент) с конструктором __init__, который принимает два параметра:
# name (имя студента)
# student_id (номер студенческого билета)
# Сохраните эти значения в атрибуты self.name и self.student_id.
# Добавьте метод introduce, который выводит на экран строку:
# "Меня зовут [name], мой номер студенческого: [student_id]".
# Создайте два объекта класса Student:
# student1 — имя "Анна", номер "S12345"
# student2 — имя "Петр", номер "S67890"
# Вызовите метод introduce для каждого объекта.

class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def introduce(self):
        print(f"Меня зовут {self.name}, мой номер студенческого: {self.student_id}")

student1 = Student("Анна", "S12345")
student2 = Student("Петр", "S67890")
student1.introduce()
student2.introduce()

# Задача 5.
# Создайте класс Rectangle (Прямоугольник) с конструктором __init__, который принимает два параметра:
# length (длина)
# width (ширина)
# Сохраните эти значения в атрибуты self.length и self.width.
# Добавьте два метода:
# area() — возвращает площадь прямоугольника (длина × ширина)
# perimeter() — возвращает периметр прямоугольника (2 × (длина + ширина))
# Создайте объект класса Rectangle с длиной 5 и шириной 3.
# Выведите на экран площадь и периметр этого прямоугольника, вызвав соответствующие методы.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(5, 3)
print(my_rectangle.area())
print(my_rectangle.perimeter())

# Задача 6.
# Создайте класс Car (Автомобиль) с конструктором __init__, который принимает три параметра:
# brand (марка автомобиля)
# model (модель автомобиля)
# year (год выпуска)
# Сохраните эти значения в соответствующие атрибуты self.brand, self.model, self.year.
# Добавьте метод get_age(current_year),
# который принимает текущий год как параметр и возвращает возраст автомобиля (текущий год минус год выпуска).
# Создайте объект класса Car с маркой "Toyota", моделью "Camry", годом выпуска 2018.
# Вызовите метод get_age с текущим годом 2025 и выведите результат на экран.

class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_age(self, current_year):
        return current_year - self.year

my_car = Car("Toyota", "Camry", 2018)
print(my_car.get_age(current_year=2025))

# Задача 7 (комбинированная: атрибуты, методы, логика).
# Создайте класс LibraryBook (Книга в библиотеке) с конструктором __init__, который принимает:
# title (название)
# author (автор)
# total_copies (общее количество экземпляров, целое число)
# В конструкторе инициализируйте:
# Атрибуты self.title, self.author, self.total_copies
# Атрибут self.available_copies, равный total_copies (все экземпляры доступны изначально)
# Добавьте методы:
# borrow() — если есть доступные экземпляры (available_copies > 0),
# уменьшает available_copies на 1 и возвращает True. Если нет — возвращает False.
# return_book() — увеличивает available_copies на 1 (но не больше total_copies)
# get_info() — возвращает строку: "[title] (автор: [author]), доступно: [available_copies]/[total_copies]"
# Создайте объект book = LibraryBook("1984", "Оруэлл", 3) и выполните:
# Два успешных взятия книги
# Попытку взять книгу, когда экземпляров уже нет
# Возврат одной книги
# Вывод информации о книге через get_info()

class LibraryBook:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
    def get_info(self):
        return f"{self.title} (автор: {self.author}), доступно: {self.available_copies}/{self.total_copies}"

book = LibraryBook("1984", "Оруэлл", 3)
print(book.borrow())
print(book.borrow())
print(book.borrow())
print(book.borrow())
print(book.get_info())
book.return_book()
print(book.get_info())

