from flask import Flask

from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return 'Go to <a href="http://127.0.0.1:5000/tracker/">Tracker</a>'


if __name__ == '__main__':
    app.run(debug=True)
