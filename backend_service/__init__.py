from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask_cors import CORS
import requests
from . import config
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()

class MovieList(Resource):

    def get(self):
        print("Call for: GET /movies")
        url = config.es_base_url['dialogues']+'/_search'
        query = {
            "query": {
                "match_all": {}
            },
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        movies = []
        for hit in data['hits']['hits']:
            movie = hit['_source']
            movie['id'] = hit['_id']
            movies.append(movie)
        return movies


class Search(Resource):

    def get(self):
        print("Call for GET /search")
        parser.add_argument('q')
        query_string = parser.parse_args()
        url = config.es_base_url['dialogues']+'/_search'
        query = {
            "query": {
                "multi_match": {
                    "fields": ["actor_name", "hindi_diag", "movie_name"],
                    "query": query_string['q'],
                    "type": "best_fields"
                }
            },
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        movies = []
        for hit in data['hits']['hits']:
            movie = hit['_source']
            movie['id'] = hit['_id']
            movies.append(movie)
        return movies

api.add_resource(MovieList, config.api_base_url+'/movies')
api.add_resource(Search, config.api_base_url+'/search')