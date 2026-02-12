# Задача 1.
# Создайте словарь student с ключами:
# "name" (значение - ваше имя строкой)
# "age" (значение - ваш возраст числом)
# "city" (значение - ваш город строкой)
# Затем обновите возраст в словаре, увеличив его на 1, и добавьте новый ключ "grade" со значением "A".
# Выведите итоговый словарь на экран.

student = {
    "name": "Nikita",
    "age": 26,
    "city": "Krasnoyarsk"
}
student["age"] = 27
student["grade"] = "A"
print(student)

# Задача 2.
# Создайте словарь car с ключами: "brand" (значение "Toyota"), "model" (значение "Camry"), "year" (значение 2022).
# Напишите код, который:
# Выводит значение по ключу "model"
# Проверяет наличие ключа "color" в словаре
# Если ключа нет, выводит "Ключ 'color' отсутствует"
# Используйте метод для проверки наличия ключа.

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022
}
print(car["model"])
if "color" not in car:
    print("Ключ 'color' отсутствует")
# assert "color" in car, "Ключ 'color' отсутствует"

# Задача 3.
# Создайте словарь fruit_prices с элементами: "apple": 50, "banana": 30, "orange": 40.
# Напишите код, который:
# Удаляет элемент с ключом "banana" из словаря.
# Получает список всех ключей словаря и список всех значений.
# Выводит оба списка на экран.
# Используйте методы для удаления и получения ключей/значений.

fruit_prices = {
    "apple": 50,
    "banana": 30,
    "orange": 40
}
# del fruit_prices["banana"]
fruit_prices.pop("banana")
print(fruit_prices.keys())
print(fruit_prices.values())

# Задача 4.
# Создайте пустой словарь user_data.
# Напишите код, который последовательно:
# Добавляет ключ "login" со значением "user123"
# Добавляет ключ "email" со значением "user@mail.com"
# Обновляет значение "login" на "new_user123"
# Проверяет, есть ли в словаре ключ "email", и если есть - выводит его значение.
# Выведите итоговый словарь на экран.

user_data = {

}
user_data["login"] = "user123"
user_data["email"] = "user@mail.com"
user_data["login"] = "new_user123"
if "email" in user_data:
    print(user_data["email"])
print(user_data)

# Задача 5.
# Создайте словарь book с ключами:
# "title" (значение "Python Basics"), "author" (значение "Ivan Petrov"), "pages" (значение 300).
# Напишите код, который:
# Проверяет, есть ли в словаре значение "Ivan Petrov"
# Проверяет, есть ли в словаре значение 2024
# Для каждой проверки выводит "Значение найдено" или "Значение не найдено"
# Используйте метод для проверки наличия значения.

book = {
    "title": "Python Basics",
    "author": "Ivan Petrov",
    "pages": "300"
}
if "Ivan Petrov" in book.values():
    print("Значение найдено")
else:
    print("Значение не найдено")
if 2024 in book.values():
    print("Значение найдено")
else:
    print("Значение не найдено")

# Задача 6.
# Создайте словарь config с элементами: "theme": "dark", "language": "en", "volume": 75.
# Напишите код, который:
# Получает список всех пар «ключ-значение» словаря
# Выводит этот список на экран.
# Используйте метод для получения всех пар ключ-значение.

config = {
    "theme": "dark",
    "language": "en",
    "volume": 75
}
print(config.items())

# Задача 7.
# Создайте словарь country_capitals с элементами: "Russia": "Moscow", "France": "Paris", "Japan": "Tokyo".
# Напишите код, который:
# Проверяет наличие ключа "Germany" в словаре
# Если ключа нет - добавляет пару "Germany": "Berlin"
# Проверяет наличие ключа "France" в словаре
# Если ключ есть - выводит его значение.
# Выведите итоговый словарь на экран.

country_capitals = {
    "Russia": "Moscow",
    "France": "Paris",
    "Japan": "Tokyo"
}
if "Germany" not in country_capitals:
    country_capitals["Germany"] = "Berlin"
if "France" in country_capitals:
    print(country_capitals["France"])
print(country_capitals)