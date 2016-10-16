'''
Created on Sep 17, 2016

@author: vineetgadodia
'''
from elasticsearch import Elasticsearch
import csv

es = Elasticsearch()

f = open("output.csv", 'rU')
reader = csv.DictReader(f)
for doc in reader:
    res = es.index(index="movies", doc_type='dialogues', body=doc)

es.indices.refresh(index="movies")
res = es.search(index="movies", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(movie_name)s %(actor_name)s: %(hindi_dialogue)s" % hit["_source"])
    
