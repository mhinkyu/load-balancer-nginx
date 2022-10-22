from flask import request, Flask
import json

app1 = Flask(__name__)
@app1.route('/')

def hello_world():
    return "Hello World!, This is app2"

if __name__=="__main__":
    app1.run(debuf = True, host = '0.0.0.0')