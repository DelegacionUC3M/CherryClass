#!/usr/bin/python

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __init__(self, name, desc):
        self.name = name
        self.description = desc

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
