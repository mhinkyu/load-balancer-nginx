from flask import request, Flask

app2 = Flask(__name__)

@app2.route('/')
def hello_world():
    return "Hello World!, This is app2"

if __name__ == "__main__":
    app2.run(debug = True, host = '0.0.0.0')