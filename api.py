from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask import make_response, jsonify
api=Api()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    





api.add_resource(HelloWorld, '/hello')