# src/app/validation.py

from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema


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