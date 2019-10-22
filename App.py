from flask import Flask
from flask_restful import Resource, Api
from GPIOS import *

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self, name):
        return {"Hello": name}

class TurnOn(Resource):
    def get(self):
        return "on"


api.add_resource(TurnOn, '/turnon')
api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
    app.run(debug=True)

