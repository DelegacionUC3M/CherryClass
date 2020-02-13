#!/usr/bin/python

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from models import db, Record

# Configure the application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# Create the database and link it to the app
db.app = app
db.init_app(app)
db.create_all()


@app.route('/api/v1/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello world'}), 200


@app.route('/api/v1/record', methods=['GET', 'POST'])
def get_records():
    if request.method == 'GET':
        record_list = [r.serialize for r in Record.query.all()]
        return jsonify({'records': record_list})
    else:
        data = request.get_json()
        record = Record(data['name'], data['description'])
        db.session.add(record)
        db.session.commit()
        return jsonify({'message': 'record inserted correctly'}), 200


@app.route('/api/v1/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.get(record_id)
    return jsonify(record.serialize)


if __name__ == '__main__':
    app.run(debug=True)
