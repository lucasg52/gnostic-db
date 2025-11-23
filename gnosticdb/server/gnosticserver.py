from flask import Flask, request
from flask_cors import CORS
from .handler import PostHandler

app = Flask('gnosticserver')
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def process_post():
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

