from elasticsearch import Elasticsearch

# Подключение к Elasticsearch
elasticsearch_host = 'localhost'
elasticsearch_port = 9200
elasticsearch_username = 'nastya'
elasticsearch_password = 'nastya'

elasticsearch_connection = Elasticsearch(
    [{'host': elasticsearch_host, 'port': elasticsearch_port, "scheme": "http"}],
    http_auth=(elasticsearch_username, elasticsearch_password)
)

# Ввод строки для поиска
print('Введите строку для поиска:')
search_string = input()

# Поиск в Elasticsearch
search_body = {
    'query': {
        'match_phrase': {
            "text": search_string
        }
    }
}
search_result = elasticsearch_connection.search(index="my_index", body=search_body)

# Вывод результатов поиска в файл
output_file = 'search_results.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    total_hits = search_result['hits']['total']['value']
    file.write(f'Искомое слово: {search_string}\n')
    file.write(f'Найдено совпадений: {total_hits}\n')
    file.write('--- Результаты поиска ---\n')
    for hit in search_result['hits']['hits']:
        file.write(f'Документ ID: {hit["_id"]}\n')
        file.write('Текст документа: ')
        file.write(hit["_source"]["text"].replace(search_string, f'👉 {search_string} 👈'))
        file.write('\n☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝\n\n')

print(f'Результаты поиска сохранены в файле: {output_file}')