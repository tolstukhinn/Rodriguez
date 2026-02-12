# Задача 1.
# Создайте родительский класс Animal (Животное) с конструктором __init__,
# принимающим параметр name (имя). Сохраните его в self.name.
# Добавьте метод speak, который возвращает строку "Звук животного".
# Создайте дочерний класс Dog (Собака), который наследует от Animal.
# Переопределите метод speak в классе Dog, чтобы он возвращал строку "[имя] говорит: Гав!".
# Создайте объект класса Dog с именем "Барсик" и вызовите его метод speak. Выведите результат.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Звук животного"
class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав!"

my_dog = Dog("Барсик")
print(my_dog.speak())

# Задача 2.
# Создайте родительский класс Vehicle (Транспортное средство) с конструктором __init__,
# принимающим параметр brand (марка). Сохраните его в self.brand.
# Добавьте метод info, который возвращает строку "Марка: [brand]".
# Создайте дочерний класс Car (Автомобиль), который наследует от Vehicle.
# В классе Car:
# Добавьте конструктор __init__, который принимает два параметра: brand и model (модель).
# Используйте super().__init__(brand) для инициализации родительского атрибута.
# Сохраните model в self.model.
# Переопределите метод info, чтобы он возвращал строку "Марка: [brand], Модель: [model]".
# Создайте объект класса Car с маркой "Toyota" и моделью "Camry". Вызовите метод info и выведите результат.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def info(self):
        return f"Марка: {self.brand}"
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def info(self):
        return f"Марка: {self.brand}, Модель: {self.model}"

my_car = Car("Toyota", "Camry")
print(my_car.info())

# Задача 3.
# Создайте родительский класс Person (Человек) с конструктором __init__, принимающим параметр name (имя).
# Сохраните его в self.name.
# Добавьте метод introduce, который возвращает строку "Меня зовут [name]".
# Создайте дочерний класс Student (Студент), который наследует от Person.
# В классе Student:
# 1. Добавьте конструктор __init__, который принимает два параметра:
# name и student_id (номер студенческого билета).
# 2. Используйте super().__init__(name) для инициализации родительского атрибута.
# 3. Сохраните student_id в self.student_id.
# 4. Переопределите метод introduce, чтобы он возвращал строку
# "Меня зовут [name], мой номер студенческого: [student_id]".
# Создайте объект класса Student с именем "Анна" и номером "S12345".
# Вызовите метод introduce и выведите результат.

class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"Меня зовут {self.name}"
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def introduce(self):
        return f"Меня зовут {self.name}, мой номер студенческого: {self.student_id}"

my_student = Student("Анна", "S12345")
print(my_student.introduce())

# Задача 4.
# Создайте родительский класс Employee (Сотрудник) с конструктором __init__,
# принимающим два параметра: name (имя) и salary (зарплата). Сохраните их в self.name и self.salary.
# Добавьте метод get_info, который возвращает строку "Сотрудник: [name], Зарплата: [salary]".
# Создайте дочерний класс Manager (Менеджер), который наследует от Employee.
# В классе Manager:
# 1. Добавьте конструктор __init__, который принимает три параметра: name, salary и department (отдел).
# 2. Используйте super().__init__(name, salary) для инициализации родительских атрибутов.
# 3. Сохраните department в self.department.
# 4. Переопределите метод get_info, чтобы он возвращал строку
# "Менеджер: [name], Отдел: [department], Зарплата: [salary]".
# Создайте объект класса Manager с именем "Иван", зарплатой 50000 и отделом "Продажи".
# Вызовите метод get_info и выведите результат.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_info(self):
        return f"Сотрудник: {self.name} Зарплата: {self.salary}"
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def get_info(self):
        return f"Менеджер: {self.name}, Отдел: {self.department}, Зарплата: {self.salary}"

my_manager = Manager("Иван", 50000, "Продажи")
print(my_manager.get_info())

# Задача 5.
# Создайте родительский класс Device (Устройство) с конструктором __init__,
# принимающим параметр power (мощность в ваттах). Сохраните его в self.power.
# Добавьте метод describe, который возвращает строку "Устройство мощностью [power] Вт".
# Создайте дочерний класс Computer (Компьютер), который наследует от Device.
# В классе Computer:
# 1. Добавьте конструктор __init__, который принимает два параметра:
# power и ram (объём оперативной памяти в ГБ).
# 2. Используйте super().__init__(power) для инициализации родительского атрибута.
# 3. Сохраните ram в self.ram.
# 4. Переопределите метод describe, чтобы он возвращал строку "Компьютер мощностью [power] Вт с [ram] ГБ ОЗУ".
# Создайте объект класса Computer с мощностью 500 и памятью 16. Вызовите метод describe и выведите результат.

class Device:
    def __init__(self, power):
        self.power = power
    def describe(self):
        return f"Устройство мощностью {self.power} Вт"
class Computer(Device):
    def __init__(self, power, ram):
        super().__init__(power)
        self.ram = ram
    def describe(self):
        return f"Компьютер мощностью {self.power} Вт с {self.ram} ГБ ОЗУ"

my_computer = Computer(500,16)
print(my_computer.describe())

# Задача 6 (комбинированная: наследование, super, переопределение, добавление новых методов).
# Создайте родительский класс BankAccount (Банковский счёт) с конструктором __init__, принимающим два параметра:
# - owner (владелец счёта, строка)
# - balance (начальный баланс, по умолчанию 0)
# Сохраните их в self.owner и self.balance.
# Добавьте методы:
# 1. deposit(amount) — увеличивает баланс на amount
# 2. withdraw(amount) — если на счету достаточно средств, уменьшает баланс на amount и возвращает True;
# иначе возвращает False
# 3. get_info() — возвращает строку "Владелец: [owner], Баланс: [balance]"
# Создайте дочерний класс SavingsAccount (Сберегательный счёт), который наследует от BankAccount.
# В классе SavingsAccount:
# 1. Добавьте конструктор __init__, принимающий три параметра: owner, balance (по умолчанию 0)
# и interest_rate (процентная ставка, например 0.05 для 5%).
# 2. Используйте super().__init__(owner, balance) для инициализации родительских атрибутов.
# 3. Сохраните interest_rate в self.interest_rate.
# 4. Переопределите метод get_info(), чтобы он возвращал строку: "Владелец: [owner], Баланс: [balance],
# Ставка: [interest_rate]%" (ставку выведите в процентах, умножив на 100).
# 5. Добавьте новый метод add_interest() —
# который увеличивает баланс на balance * interest_rate (начисляет проценты).
# Создайте объект класса SavingsAccount с владельцем "Анна", начальным балансом 1000 и ставкой 0.05.
# Выполните:
# 1. Выведите информацию о счёте
# 2. Начислите проценты
# 3. Выведите информацию о счёте после начисления
# 4. Попробуйте снять 1200 (должно вернуть `False`)
# 5. Выведите итоговую информацию
# *Подсказка: для вывода ставки в процентах: f"{self.interest_rate * 100}%".*

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_info(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}"

class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def get_info(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}, Ставка: {self.interest_rate * 100}%"

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

my_user = SavingsAccount("Анна", 1000, 0.05)
print(my_user.get_info())
my_user.add_interest()
print(my_user.get_info())
print(my_user.withdraw(1200))
print(my_user.get_info())