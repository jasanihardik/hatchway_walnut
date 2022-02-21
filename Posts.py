import grequests
from flask_restx import Resource, reqparse
from mergedeep import merge, Strategy


class Posts(Resource):

    def get(self):
        descendingOrder = False
        params = []

        parser = reqparse.RequestParser()
        parser.add_argument('tags',
                            required=True,
                            type=str,
                            action="split",
                            help="Tags parameter is required")
        parser.add_argument('sortBy',
                            choices=("id", "reads", "likes", "popularity"),
                            default="id",
                            help="sortBy parameter is invalid")
        parser.add_argument('direction',
                            choices=("desc", "asc"),
                            default="asc",
                            help="direction parameter is invalid")
        args = parser.parse_args()

        for tag in args['tags']:
            paramParser = reqparse.RequestParser()
            paramParser.add_argument('tag', tag)
            paramArgs = paramParser.parse_args()
            params.append(paramArgs)

        result = (grequests.get("https://api.hatchways.io/assessment/blog/posts", params=param) for param in params)
        results = grequests.imap(result)

        finalResult = {}
        for r in results:
            merge(finalResult, r.json(), strategy=Strategy.ADDITIVE)

        if args["direction"] == "desc":
            descendingOrder = True

        return {'posts': sorted(finalResult['posts'], key=lambda x: x[args["sortBy"]], reverse=descendingOrder)}
