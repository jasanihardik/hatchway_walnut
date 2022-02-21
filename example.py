import requests
from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api, reqparse

from Posts import Posts

app = Flask(__name__)
api = Api(app)

CORS(app)


class Ping(Resource):
    @staticmethod
    def get():
        responseData = {'success': True}
        return responseData


class AllPosts(Resource):
    descendingOrder = False

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('tags',
                            required=True,
                            help="Tags parameter is required")\
            .replace_argument('tags', dest='tag', type=str, action="split")
        parser.add_argument('sortBy',
                            choices=("id", "reads", "likes", "popularity"),
                            default="id",
                            help="sortBy parameter is invalid")
        parser.add_argument('direction',
                            choices=("desc", "asc"),
                            default="asc",
                            help="direction parameter is invalid")
        args = parser.parse_args()

        response = requests.get('https://api.hatchways.io/assessment/blog/posts', params=args)

        if args["direction"] == "desc":
            descendingOrder = True

        sortedPostsData = {'posts': sorted(response.json()['posts'], key=lambda x: x[args["sortBy"]], reverse=descendingOrder)}

        return sortedPostsData


api.add_resource(Ping, '/api/ping')  # Route 1
api.add_resource(AllPosts, '/api/posts/all')  # Route 2
api.add_resource(Posts, '/api/posts') # Route 3

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
