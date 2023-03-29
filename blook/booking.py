#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/booking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  

class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(32), nullable=False)
    activity_id = db.Column(db.Integer, nullable=True)
    booking_datetime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    datetime = db.Column(db.String(10), nullable=False)
    total_pax = db.Column(db.Integer, nullable=True)
    payment_amount = db.Column(db.Float(precision=2), nullable=False)
    status = db.Column(db.String(3), nullable=False, default= 'NO')
    
    # def __init__(self, id, customer_id, activity_id, booking_datetime, datetime, total_pax, payment_amount, status):
    #     self.id = id
    #     self.customer_id = customer_id
    #     self.activity_id = activity_id
    #     self.booking_datetime = booking_datetime
    #     self.datetime = datetime
    #     self.total_pax = total_pax
    #     self.payment_amount = payment_amount
    #     self.status = status


    def json(self):
        dto = {
            'id': self.id,
            'customer_id': self.customer_id,
            'activity_id': self.activity_id,
            'booking_datetime': self.booking_datetime,
            'datetime': self.datetime,
            'total_pax': self.total_pax,
            'payment_amount': self.payment_amount,
            'status': self.status
        }
        return dto


@app.route("/booking")
def get_all():
    bookinglist = Booking.query.all()
    if len(bookinglist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [booking.json() for booking in bookinglist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no booking."
        }
    ), 404


@app.route("/booking/<string:booking_id>")
def find_by_booking_id(booking_id):
    booking = Booking.query.filter_by(id=booking_id).first()
    if booking:
        return jsonify(
            {
                "code": 200,
                "data": booking.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "booking_id": booking_id
            },
            "message": "Booking not found."
        }
    ), 404


@app.route("/booking", methods=['POST'])
def create_booking():
    customer_id = request.json.get('customer_id', None)
    activity_id = request.json.get('activity_id', None)
    payment_amount = request.json.get('payment_amount', None)
    total_pax = request.json.get('total_pax', None)
    datetime = request.json.get('datetime', None)
    booking = Booking(customer_id=customer_id, activity_id=activity_id, payment_amount=payment_amount, total_pax=total_pax, datetime=datetime)

    try:
        db.session.add(booking)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the booking. " + str(e)
            }
        ), 500
    
    print(json.dumps(booking.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": booking.json()
        }
    ), 201


@app.route("/booking/<string:booking_id>", methods=['PUT'])
def update_order(booking_id):
    try:
        booking = Booking.query.filter_by(id=booking_id).first()
        if not booking:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "booking_id": booking_id
                    },
                    "message": "Booking not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['status']:
            booking.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": booking.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "booking_id": booking_id
                },
                "message": "An error occurred while updating the booking. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5002, debug=True)
