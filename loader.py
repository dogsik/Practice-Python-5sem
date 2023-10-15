from elasticsearch import Elasticsearch

import csv

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

print(f"Connected to ElasticSearch cluster `{es.info().body['serchText']}`") #cluster_name

#объект reader, который используется для чтения данных из файла.
with open("./posts.csv", "r") as f:
    reader = csv.reader(f) 

# Для каждой строки создаем объект document, содержащий значения из соответствующих столбцов CSV файла. Ключи в объекте document соответствуют конкретным полям данных в ElasticSearch.

    for i, line in enumerate(reader):
        document = {
            "text": line[0],
            
        }
        es.index(index="index", document=document)