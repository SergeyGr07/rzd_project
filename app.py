from flask import Flask, render_template

from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return render_template("loging_page.html")


if __name__ == '__main__':
    app.run(debug=True)
