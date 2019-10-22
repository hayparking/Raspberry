from flask import Flask
from flask_restful import Resource, Api
from GPIOS import *

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self, name):
        return {"Hello": name}

class TurnOn(Resource):
    def get(self, pin):
        temp = controller()
        temp.changeState(pin, True)
        return "On"

class TurnOff(Resource):
    def get(self, pin):
        temp = controller()
        temp.changeState(pin, False)
        return "Off"

api.add_resource(TurnOn, '/turnon/<pin>')
api.add_resource(TurnOff, '/turnoff/<pin>')
api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
    app.run(debug=True)

