from flask import request, Flask

app1 = Flask(__name__)


@app1.route('/')
def hello_world():
    return "Hello World!, This is app1"

if __name__ == "__main__":
    app1.run(debug=True, host='0.0.0.0')

