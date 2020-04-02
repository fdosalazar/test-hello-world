from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'ok': True, 'message': 'Hello World!'}

class HealthCheck(Resource):
    def get(self):
        return {'ok': True, 'message': 'Health is OK!'}

api.add_resource(HelloWorld, '/')
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')