from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(7), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    billing_address = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    def __init__(self, id, first_name, last_name, email, gender, address, billing_address, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.address = address
        self.billing_address = billing_address
        self.phone = phone
        
        

    def json(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email, "gender" :self.gender, "address": self.address, "billing_address": self.billing_address, "phone": self.phone}


@app.route("/customer")
def get_all():
    activitylist = Customer.query.all()
    if len(activitylist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "activities": [customer.json() for customer in activitylist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customer."
        }
    ), 404


@app.route("/customer/<string:id>")
def find_by_isbn13(id):
    customer = Customer.query.filter_by(id=id).first()
    if customer:
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404


@app.route("/customer/<string:id>", methods=['POST'])
def create_book(id):
    if (Customer.query.filter_by(id=id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Customer already exists."
            }
        ), 400

    data = request.get_json()
    customer = Customer(id, **data)

    try:
        db.session.add(customer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
                },
                "message": "An error occurred creating the customer."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": customer.json()
        }
    ), 201


@app.route("/customer/<string:id>", methods=['PUT'])
def update_book(id):
    customer = Customer.query.filter_by(id=id).first()
    if customer:
        data = request.get_json()
        if data['title']:
            customer.title = data['title']
        if data['price']:
            customer.price = data['price']
        if data['availability']:
            customer.availability = data['availability'] 
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "id": id
            },
            "message": "Customer not found."
        }
    ), 404


@app.route("/customer/<string:id>", methods=['DELETE'])
def delete_book(id):
    customer = Customer.query.filter_by(id=id).first()
    if customer:
        db.session.delete(customer)
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
            "message": "Customer not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
