from flask import Flask, request
from flask_cors import CORS
from .handler import PostHandler


app = Flask('gnosticserver')
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def process_post():
    header = request.headers.copy()
    try:
        url = header['url']
        header.pop(url)
    except KeyError as e:
        url = 'undefined'
    try:
        ph = PostHandler(request.stream)
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
    pass
    # jsonify_wholedb()

@app.route('/<timestamp>', methods=['GET'])
def process_get_ts(timestamp):
    pass
