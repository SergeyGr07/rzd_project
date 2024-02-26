from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
# from flask_login import login_required
from user import login_manager


app = Flask(__name__)
CORS(app)
app.secret_key = 'your secret key'
login_manager.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    field1 = request.args.get('field1')
    field2 = request.args.get('field2')

    return jsonify({'field1': field1, 'field2': field2})


@app.route('/loging')
# @login_required
def main_page():
    return render_template('login.html')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
