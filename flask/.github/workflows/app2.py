from flask import flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=5000, debug=True)