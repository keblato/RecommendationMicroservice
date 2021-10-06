# src/app/main.py:
import sys
sys.path
from operator import ge
from flask import Flask, jsonify, request
import sys
sys.path.insert(0,'/home/mobileApp/RecommendationMicroservice/src')

from app.invalid_usage import InvalidUsage
from app.recommendations import genre_recommendations
from app.validation import validate_movieId
app = Flask(__name__)



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
    app.run(host='0.0.0.0')      

