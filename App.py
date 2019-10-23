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
        temp.changeState(int(pin), True)
        return "On"

class TurnOff(Resource):
    def get(self, pin):
        temp = controller()
        temp.changeState(int(pin), False)
        return "Off"

class Clear(Resource):
	def get(self):
		temp = controller()
		temp.cleanAll()
		return "Clean all gpios"


api.add_resource(Clear, '/clean')
api.add_resource(TurnOn, '/turnon/<pin>')
api.add_resource(TurnOff, '/turnoff/<pin>')
api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
    app.run(debug=True)

