#import sqlite3
#
## Создание и подключение к базе данных
#connection = sqlite3.connect('example.db')  # Файл базы данных создается в текущей директории
#cursor = connection.cursor()
#
## Создание таблицы
#cursor.execute('''
#CREATE TABLE form_data (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    field_1 VARCHAR(255),
#    field_2 VARCHAR(255),
#    field_3 VARCHAR(255)
#);
#
#''')
#
#
#
## Сохранение изменений
#connection.commit()
#
## Запрос данных
##cursor.execute('SELECT * FROM employees')
##rows = cursor.fetchall()
#
## Вывод данных
##print("Employees in the database:")
##for row in rows:
##    print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}")
#
## Закрытие соединения
#connection.close()
#
import os

print("Current working directory:", os.getcwd())