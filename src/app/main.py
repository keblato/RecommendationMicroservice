# src/app/main.py:
import sys
#sys.path.insert(0,'/home/ubuntu/RecommendationMicroservice/src')

# from operator import ge
from flask import Flask, jsonify, request
#from flask import Flask

from app.invalid_usage import InvalidUsage
from app.recommendations import genre_recommendations
from app.validation import validate_movieId
app = Flask(__name__)



@app.route("/", methods=['GET'])
def index() -> str:
    # transform a dict into an application/json response 
    #return jsonify({"message": "It Works"})
    return "Hello Updated World!"
        
""" @app.route("/movieR", methods=['POST'])
def hello() -> str:
   errors = None
   if errors is not None:
       print(errors)
       raise InvalidUsage(errors)
   movieId = request.json.get("movieId", None)
   response = "a2" #{"recommendations": list(genre_recommendations(movieId))}
   return jsonify(response)
 """

if __name__ == '__main__':
    app.run(host='0.0.0.0')      

