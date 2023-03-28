from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/activity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Activity(db.Model):
    __tablename__ = 'activity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    address = db.Column(db.String(50), nullable=False)

    def __init__(self, id, name, description, price, address):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.addres = address

    def json(self):
        return {"id": self.id, "name": self.name, "description": self.description, "price": self.price, "address": self.address}


@app.route("/activity")
def get_all():
    activitylist = Activity.query.all()
    if len(activitylist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "activities": [activity.json() for activity in activitylist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no activity."
        }
    ), 404


@app.route("/activity/<string:id>")
def find_by_isbn13(id):
    activity = Activity.query.filter_by(id=id).first()
    if activity:
        return jsonify(
            {
                "code": 200,
                "data": activity.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Activity not found."
        }
    ), 404


@app.route("/activity/<string:id>", methods=['POST'])
def create_book(id):
    if (Activity.query.filter_by(id=id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Activity already exists."
            }
        ), 400

    data = request.get_json()
    activity = Activity(id, **data)

    try:
        db.session.add(activity)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the activity."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": activity.json()
        }
    ), 201


@app.route("/activity/<string:id>", methods=['PUT'])
def update_book(id):
    activity = Activity.query.filter_by(id=id).first()
    if activity:
        data = request.get_json()
        if data['title']:
            activity.title = data['title']
        if data['price']:
            activity.price = data['price']
        if data['availability']:
            activity.availability = data['availability'] 
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": activity.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "id": id
            },
            "message": "Activity not found."
        }
    ), 404


@app.route("/activity/<string:id>", methods=['DELETE'])
def delete_book(id):
    activity = Activity.query.filter_by(id=id).first()
    if activity:
        db.session.delete(activity)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "id": id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "id": id
            },
            "message": "Activity not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
