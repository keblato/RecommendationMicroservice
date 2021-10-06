# src/app/main.py:
from operator import ge
from flask import Flask, jsonify, request
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)



movies=pd.read_csv('../data/movies.csv', sep=',', encoding = 'utf-8')
tfvector= TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tfvector.fit_transform(movies['genres'])
cosine_sim2 = linear_kernel(tfidf_matrix, tfidf_matrix)

'''The Content-Based Recommender relies on the similarity of the items being recommended. The basic idea is that if 
you like an item, then you will also like a “similar” item. It generally works well when it’s easy to determine 
the context/properties of each item. 
'''

# Build a 1-dimensional array with movie titles
titles = movies['movieId']
indices = pd.Series(movies.index, index=movies['movieId'])


# Function that get movie recommendations based on the cosine similarity score of movie genres
def genre_recommendations(movieId):
    idx = indices[movieId]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

def recommendation_ready():
    if movies is None:
        return  False
    return True

def create_recommendations(movies):

    return True



# https://pythonhosted.org/Flask-Inputs/#module-flask_inputs
# https://json-schema.org/understanding-json-schema/
# we want an object containing a required greetee  string value
movieId_schema = {
   'type': 'object',
   'properties': {
       'movieId': {
           'type': 'integer',
       }
   },
   'required': ['movieId']
}


class GreetingInputs(Inputs):
   json = [JsonSchema(schema=movieId_schema)]


def validate_movieId(request):
   inputs = GreetingInputs(request)
   if inputs.validate():
       return None
   else:
       return inputs.errors


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.route("/", methods=['GET'])
def index() -> str:
    # transform a dict into an application/json response 
    return jsonify({"message": "It Works"})
        
@app.route("/movieR", methods=['POST'])
def hello() -> str:
   errors = validate_movieId(request)
   if errors is not None:
       print(errors)
       raise InvalidUsage(errors)
   movieId = request.json.get("movieId", None)
   response ={"recommendations": list(genre_recommendations(movieId))}
   return jsonify(response)

@app.route("/movieGOOD", methods=['GET'])
def movieGOOD() -> str:

   return True


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
   response = jsonify(error.to_dict())
   response.status_code = error.status_code
   return response
if __name__ == '__main__':
    app.run(host="0.0.0.0")      

