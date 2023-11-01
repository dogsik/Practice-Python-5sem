import sqlite3 #взаимодействия с базами данных SQLite

# Создаем подключение к базе данных
database_connection = sqlite3.connect('database.db')
# Создаем курсор для выполнения SQL-запросов
database_cursor = database_connection.cursor()

# Создаем таблицу Documents, если она не существует
database_cursor.execute('''
CREATE TABLE IF NOT EXISTS Documents (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    rubrics TEXT NOT NULL,
    created_date TEXT NOT NULL
)
''')

# Сохраняем изменения в базе данных
database_connection.commit()
# Закрываем соединение с базой данных
database_connection.close()