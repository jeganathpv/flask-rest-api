  
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

class HelloWorld(Resource):
    @app.route('/test', methods=['GET'])
    @cross_origin(support_credentials=True)
    def helloWorld():
        return "Hello World!, I am from Heroku"


if __name__ == "__main__":
    api.add_resource(HelloWorld)
    app.run()