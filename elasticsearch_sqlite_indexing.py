from elasticsearch import Elasticsearch
import sqlite3

# Подключение к Elasticsearch
elasticsearch_host = 'localhost'
elasticsearch_port = 9200
elasticsearch_username = 'nastya'
elasticsearch_password = 'nastya'

elasticsearch_connection = Elasticsearch(
    [{'host': elasticsearch_host, 'port': elasticsearch_port, "scheme": "http"}],
    http_auth=(elasticsearch_username, elasticsearch_password)
)

# Удаление существующего индекса, если он существует
index_name = "my_index"
if elasticsearch_connection.indices.exists(index=index_name):
    elasticsearch_connection.indices.delete(index=index_name, ignore=[400, 404])

# Создание нового индекса
elasticsearch_connection.indices.create(index=index_name)

# Подключение к базе данных
database_connection = sqlite3.connect('database.db')
database_cursor = database_connection.cursor()

# Выполнение SQL-запроса для выборки данных из таблицы Documents
database_cursor.execute('SELECT * FROM Documents')
data_list = database_cursor.fetchall()

# Индексация данных в Elasticsearch
for doc in data_list:
    elasticsearch_connection.index(
        index=index_name,
        id=doc[0],
        body={
            "text": doc[1],
        },
        doc_type="_doc"  # Тип документа
    )

# Закрытие соединения с базой данных
database_connection.close()