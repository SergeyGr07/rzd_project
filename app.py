from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
# from flask_login import login_required
# from user import login_manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(100), nullable=False)
    field2 = db.Column(db.String(100), nullable=False)
    field3 = db.Column(db.String(100), nullable=False)
    field4 = db.Column(db.String(100), nullable=False)
    field5 = db.Column(db.String(100), nullable=False)
    field6 = db.Column(db.String(100), nullable=False)
    field7 = db.Column(db.String(100), nullable=False)
    field8 = db.Column(db.String(100), nullable=False)


@app.route('/data', methods=['POST'])
def index():
    if request.method == 'POST' and request.json.get('api_key') == "kjh2sdkvhKJGHs8kdjbfs456fhgsdvjhbs45bskdbksKJ689KBGJVjndvkjb6t":
        data = Data(id=request.json['id'], field1=request.json['field1'], field2=request.json['field2'],
                    field3=request.json['field3'], field4=request.json['field4'], field5=request.json['field5'],
                    field6=request.json['field6'], field7=request.json['field7'], field8=request.json['field8'])
        db.session.add(data)
        db.session.commit()
        return jsonify({'message': 'Data saved successfully'}), 201
    else:
        data = Data.query.all()
        return jsonify("Invalid request!"), 400


@app.route('/clear_data')
def clear_data():
    try:
        # Удаление всех записей из таблицы Data
        db.session.query(Data).delete()
        db.session.commit()
        return jsonify({'message': 'All data cleared successfully'}), 200
    except Exception as e:
        # Обработка ошибок, если они возникнут
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/watcher')
def watcher():
    data = Data.query.all()
    return render_template('main.html', data=data)


if __name__ == '__main__':
    # app.run(debug=True)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
