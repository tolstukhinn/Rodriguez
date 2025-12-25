import time

# Задача 1 (ООП: наследование и переопределение методов).
# Создайте родительский класс Logger с методом log(message), который выводит строку в формате:
# "[LOG]: message".
# Создайте дочерний класс ErrorLogger, который наследует от Logger.
# В классе ErrorLogger:
# Переопределите метод log(message), чтобы он выводил строку в формате: "[ERROR]: message"
# Добавьте новый метод log_with_time(message),
# который выводит: "[ERROR][2025-01-01]: message" (дата может быть фиктивной, например "2025-01-01")
# Создайте объект error_logger = ErrorLogger() и вызовите:
# error_logger.log("Случилась ошибка")
# error_logger.log_with_time("Тоже ошибка")
# Примечание: в реальной автоматизации такое наследование используется для кастомизации логирования.

class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")
class ErrorLogger(Logger):
    def log(self, message):
        print(f"[ERROR]: {message}")
    def log_with_time(self, message):
        print(f"[ERROR][2025-01-01]: {message}")
error_logger = ErrorLogger()
error_logger.log("Случилась ошибка")
error_logger.log_with_time("Тоже ошибка")

# Задача 2 (Функции: аргументы с дефолтными значениями и возврат данных).
# Создайте функцию format_api_response, которая принимает три параметра:
# status (обязательный) — строка, статус ответа
# data (обязательный) — данные ответа (любого типа)
# pretty (необязательный, по умолчанию False) — булево значение
# Функция должна возвращать словарь в формате:
# {"status": status, "data": data}
# Если pretty=True, то значение status должно быть приведено к верхнему регистру.
# Вызовите функцию три раза и выведите результаты:
# format_api_response("success", {"id": 123})
# format_api_response("error", None, pretty=True)
# format_api_response("pending", [1, 2, 3], pretty=False)
# Примечание: в авто-тестах такие функции используются для обработки ответов API.

def format_api_response(status,data,pretty=False):
    if pretty:
        status = status.upper()
    return {"status": status, "data": data}
print(format_api_response("success", {"id": 123}))
print(format_api_response("error", None, pretty=True))
print(format_api_response("pending", [1, 2, 3], pretty=False))

# Задача 3 (Словари: вложенные структуры и обновление).
# В автоматизации часто работают с JSON-ответами API. Дан словарь, имитирующий ответ API:
# python
# api_response = {
#     "status": "success",
#     "data": {
#         "user": {
#             "id": 456,
#             "name": "Иван",
#             "email": "ivan@example.com"
#         },
#         "subscription": "premium"
#     },
#     "timestamp": "2025-01-15T10:30:00Z"
# }
# Напишите код, который:
# Извлекает email пользователя и сохраняет в переменную email
# Изменяет тип подписки (subscription) с "premium" на "enterprise"
# Добавляет новый ключ "version" со значением "v2.1" на верхнем уровне словаря (рядом с status, data, timestamp)
# Выводит:
# Извлечённый email
# Весь обновлённый словарь
# Примечание: Обратите внимание на уровни вложенности.

api_response = {
     "status": "success",
     "data": {
         "user": {
             "id": 456,
             "name": "Иван",
             "email": "ivan@example.com"
         },
         "subscription": "premium"
     },
     "timestamp": "2025-01-15T10:30:00Z"
 }

email = api_response["data"]["user"]["email"]
api_response["data"]["subscription"] = "enterprise"
api_response["version"] = "v2.1"
print(email)
print(api_response)

# Задача 4 (Работа с файлами: чтение и фильтрация).
# Представьте, что у вас есть файл server_logs.txt с логами веб-сервера (создавать файл не нужно).
# Пример содержимого:
# text
# 2025-01-15 10:00:15 INFO User login successful
# 2025-01-15 10:01:22 ERROR Database connection failed
# 2025-01-15 10:02:45 WARNING High memory usage
# 2025-01-15 10:03:10 INFO Backup completed
# 2025-01-15 10:04:33 ERROR File not found
# Напишите код, который:
# Открывает файл server_logs.txt в режиме чтения с помощью with.
# Читает файл построчно.
# Выводит только строки, содержащие "ERROR" (полностью всю строку)
# Подсчитывает количество таких строк и выводит: "Найдено ошибок: X"
# Примечание: в автоматизации такой анализ логов — обычная задача.

# with open("server_logs.txt", "r") as f:
#     error_count = 0
#     for line in f:
#         if "ERROR" in line:
#             print(line.strip())
#             error_count += 1
#     print(f"Найдено ошибок: {error_count}")

# Задача 5 (Циклы и условные операторы: обработка данных).
# В авто-тестах часто приходится фильтровать данные. Дан список словарей, представляющих пользователей:
# python
# users = [
#     {"name": "Alice", "age": 25, "active": True},
#     {"name": "Bob", "age": 30, "active": False},
#     {"name": "Charlie", "age": 22, "active": True},
#     {"name": "Diana", "age": 28, "active": True},
#     {"name": "Eve", "age": 35, "active": False}
# ]
# Напишите код, который:
# С помощью цикла for проходит по списку users
# Выводит имена активных пользователей (где active == True)
# Подсчитывает количество неактивных пользователей
# После цикла выводит: "Неактивных пользователей: X"
# Примечание: используйте условные операторы внутри цикла.

users = [
     {"name": "Alice", "age": 25, "active": True},
     {"name": "Bob", "age": 30, "active": False},
     {"name": "Charlie", "age": 22, "active": True},
     {"name": "Diana", "age": 28, "active": True},
     {"name": "Eve", "age": 35, "active": False}
 ]
users_count = 0
for user in users:
    if user["active"]:
        print(user["name"])
    if user["active"] == False:
        users_count += 1
print(users_count)

# Задача 6 (Строки и f-строки: форматирование отчёта).
# В автоматизации часто нужно генерировать читаемые отчёты. Даны переменные:
# python
# test_name = "Login Test"
# status = "PASSED"
# duration_sec = 12.345
# timestamp = "2025-01-15 14:30:22"
# Напишите код, который создаёт строку report в формате:
# text
# [2025-01-15 14:30:22] Login Test: PASSED (12.35s)
# Требования:
# Используйте f-строку
# Время выполнения (duration_sec) выведите с двумя знаками после запятой
# Добавьте букву s после времени (секунды)
# Вся строка должна быть сохранена в переменную report и выведена
# Подсказка: для форматирования числа используйте {duration_sec:.2f}.

test_name = "Login Test"
status = "PASSED"
duration_sec = 12.345
timestamp = "2025-01-15 14:30:22"

report = f"[{timestamp}] Login Test: {status} ({duration_sec:.2f}s)"
print(report)

# Задача 7 (Списки: срезы и слияние — подготовка тестовых данных).
# В авто-тестах часто нужно комбинировать данные. Даны два списка:
# python
# admins = ["admin1", "admin2", "admin3"]
# users = ["user1", "user2", "user3", "user4", "user5"]
# Напишите код, который:
# Создаёт новый список test_accounts, содержащий:
# Первых 2 администраторов из списка admins
# Последних 3 пользователей из списка users.
# Выводит test_accounts.
# Затем добавляет в test_accounts нового пользователя "guest"
# Выводит итоговый список
# Примечание: используйте срезы и метод добавления в список.

admins = ["admin1", "admin2", "admin3"]
users = ["user1", "user2", "user3", "user4", "user5"]

test_accounts = admins[0:2] + users[-3:]
print(test_accounts)
test_accounts.append("guest")
print(test_accounts)

# Задача 8 (Тернарный оператор: компактная проверка в авто-тестах).
# В тестах часто нужно выбирать значение в зависимости от условия. Даны переменные:
# python
# environment = "production"
# timeout = 30 # значение по умолчанию.
# Напишите код, который с помощью тернарного оператора присваивает переменной timeout:
# 10, если environment == "production"
# 60, если environment != "production"
# Затем выведите timeout.
# Примечание: в авто-тестах так настраивают таймауты для разных окружений.

environment = "production"
timeout = 30

timeout = 10 if environment == "production" else 60
print(timeout)

# Задача 9 (Декоратор: измерение времени выполнения).
# В авто-тестах часто нужно замерять время выполнения операций. Создайте декоратор measure_time, который:
# Выводит "Начало выполнения".
# Выполняет декорируемую функцию.
# Выводит "Конец выполнения"
# Дополнительно: выводит время выполнения в секундах (используйте time.time())
# Примените декоратор к функции heavy_operation, которая:
# Выводит "Выполняю тяжёлую операцию..."
# Ждёт 0.5 секунды (используйте time.sleep(0.5))
# Вызовите декорированную функцию.
# Подсказка: импортируйте модуль time.
# Для замера времени: start = time.time() в начале, end = time.time() в конце, разница = end - start.

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print("Начало выполнения")
        func(*args, **kwargs)
        end = time.time()
        print("Конец выполнения")
        print(end - start)
    return wrapper
@measure_time
def heavy_operation():
    print("Выполняю тяжёлую операцию...")
    time.sleep(0.5)
heavy_operation()





















