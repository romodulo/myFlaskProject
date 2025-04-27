from flask import Flask, render_template, request
from flask_cors import CORS
# import json
import dataPoints

app = Flask(__name__)
# CORS(app, resources={r"/Get/API": {"origins": "http://127.0.0.1:5173"}})
# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)


content = dataPoints.p1
content2 = dataPoints.p2
content3 = dataPoints.p3
# print(type(content)) #test_print
# print(content) #test_print

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/Post/API', methods=['GET', 'POST'])
def post_Api():
    if request.method == 'POST':
        return "do-something"
    else:
        return "do-something else"

@app.route('/Get/API', methods=['GET', 'POST'])
def get_Api():
    if request.method == 'GET':
        return content
    else:
        return "data unavailable"

@app.route('/Get/API/Data', methods=['GET', 'POST'])
def get_ApiData():
    if request.method == 'GET':
        return content2
    else:
        return "data unavailable"

@app.route('/Get/API/3rdButton', methods=['GET', 'POST'])
def get_3rdButton():
    if request.method == 'GET':
        return content3
    else:
        return "data unavailable"
