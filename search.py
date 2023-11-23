from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
from constants import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT, ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD

elasticsearch_connection = Elasticsearch(
    [{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT, "scheme": "http"}],
    http_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD)
)
@app.route('/', methods=['GET', 'POST'])
def search_page():
    if request.method == 'POST':
        keyword = request.form['keyword']
        search_body = {
            'query': {
                'match_phrase': {
                    "text": keyword
                }
            }
        }
        search_result = elasticsearch_connection.search(index="my_index", body=search_body)

        output_file = 'search_results.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            total_hits = search_result['hits']['total']['value']
            file.write(f'Искомое слово: {keyword}\n')
            file.write(f'Найдено совпадений: {total_hits}\n')
            file.write('--- Результаты поиска ---\n')
            for hit in search_result['hits']['hits']:
                file.write(f'Документ ID: {hit["_id"]}\n')
                file.write('Текст документа: ')
                file.write(hit["_source"]["text"].replace(keyword, f'👉 {keyword} 👈'))
                file.write('\n☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝☝\n\n')

        return render_template('result.html', keyword=keyword, output_file=output_file)

    return render_template('search.html')