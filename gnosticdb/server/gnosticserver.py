from flask import Flask, request, Response
from flask_cors import CORS
from .handler import PostHandler
from .db_send import format_to_json


app = Flask('gnosticserver')
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def process_post():
    headers = request.headers
    try:
        url = headers['url']
    except KeyError as e:
        url = 'undefined'
    try:
        ph = PostHandler(request.stream, url, headers)
        return {
            "status": "success"
        }
    except UnicodeDecodeError as e:
        print("Could not decode raw data as UTF-8.")
        return {
            "status": "error",
            "message": "failure" + str(e)
        }

@app.route('/', methods=['GET'])
def process_get():
    try:
        fulldb_json = format_to_json()
    except Exception as e:
        return {
            "status": "error",
            "message": "failure" + str(e)
        }
    return Response(fulldb_json, mimetype='application/json')
    # return {
    #         "status" : "success",
    #         # "message" : fulldb_json
    #     }

@app.route('/<timestamp>', methods=['GET'])
def process_get_ts(timestamp):
    return {
        "status": "error",
        "message": "not implemented"
    }
