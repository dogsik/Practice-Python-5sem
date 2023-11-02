import sqlite3
import csv

# Функция для чтения данных из CSV-файла и возвращения списка словарей
def read_csv_file(file_name):
    with open(file_name, 'r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        db_list = []
        for row in csv_reader:
            db_list.append(dict(row))
    return db_list

# Подключение к базе данных SQLite
database_connection = sqlite3.connect('database.db')
database_cursor = database_connection.cursor()

# Чтение данных из CSV-файла и вставка их в таблицу Documents
csv_file_name = 'posts.csv'
data_list = read_csv_file(csv_file_name)
for row in data_list:
    text = row['text']
    rubrics = row['rubrics']
    created_date = row['created_date']
    query = 'INSERT INTO Documents (text, rubrics, created_date) VALUES (?, ?, ?)'
    database_cursor.execute(query, (text, rubrics, created_date))

# Сохранение изменений в базе данных
database_connection.commit()

# Закрытие соединения с базой данных
database_connection.close()