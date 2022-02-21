import json

import requests
from flask import Flask, jsonify, request, Response

from urllib.parse import urlparse
from urllib.parse import parse_qs

app = Flask(__name__)

# url = "https://api.hatchways.io/assessment/blog"
url = "https://api.hatchways.io/assessment/blog/posts?tag=science"


@app.route('/api/ping', methods=['GET'])
def hello_world():
    # return 'Hello, World!'
    # return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    # Response_status_code = Response.status_code
    # return Response("Response body(JSON):\n\t{\n'success':true\n}", "\nResponse status code:" == Response.status_code,
    # mimetype='application/json')
    response = requests.get("https://api.hatchways.io/assessment/blog/posts?tag=science")
    res_status_code = response.status_code
    print(res_status_code)

    # json_return = {
    #     "Response body(JSON)":
    #         # {'success':true}
    #     # "Response status code": res_status_code
    # }
    return jsonify(res_status_code, response.json())


@app.route('/api/posts', methods=['GET'])
def search():
    # args = request.args.get(url)
    # tag = args.get('tag')
    # r = requests.get(url)
    # print(r)
    # print(type(args))
    # print(type(args.to_dict()))
    # print(args.get("tag"))
    # #args.get("tag", default="", type=str)

    # parsed_url = urlparse(url)
    # captured_value = parse_qs(parsed_url.query)['tech']
    # print(captured_value)

    # hit this url after  runnig code:
    # http://127.0.0.1:5000/api/posts?tag=tech&science


    lst = input().split(',')
    print(lst)

    parameters = {
        # "tag": "tech"
        #"tag": ["tech", "science"]
        "tags": ["tech", "science"]
        #"tag": "tech"

    }

    response = requests.get("https://api.hatchways.io/assessment/blog/posts", params=parameters)
    responsee_back = response.json()
    print(responsee_back)

    return jsonify(responsee_back)


if __name__ == '__main__':
    app.run(debug=True)
