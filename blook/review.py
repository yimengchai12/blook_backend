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
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/review'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  

class Review(db.Model):
    __tablename__ = 'review'

    review_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(32), nullable=False)
    activity_id = db.Column(db.String(32), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    def __init__(self, review_id, customer_id, activity_id, rating, review_text, created):
        self.review_id = review_id
        self.customer_id = customer_id
        self.activity_id = activity_id
        self.rating = rating
        self.review_text = review_text
        self.created = created

    def json(self):
        dto = {
            'review_id': self.review_id,
            'customer_id': self.customer_id,
            'activity_id': self.activity_id,
            'rating': self.rating,
            'review_text': self.review_text,
            'created': self.created,
        }
        return dto


@app.route("/review")
def get_all():
    reviewlist = Review.query.all()
    if len(reviewlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "reviews": [review.json() for review in reviewlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reviews."
        }
    ), 404


@app.route("/review/<string:activity_id>")
def find_by_activity_id(activity_id):
    review = Review.query.filter_by(activity_id=activity_id).first()
    if review:
        return jsonify(
            {
                "code": 200,
                "data": review.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "activity_id": activity_id
            },
            "message": "Activity not found."
        }
    ), 404


@app.route("/review", methods=['POST'])
def create_review():
    customer_id = request.json.get('customer_id', None)
    activity_id = request.json.get('activity_id', None)
    rating = request.json.get('rating', None)
    review_text = request.json.get('review_text', None)
    review = Review(customer_id=customer_id, activity_id=activity_id, rating=rating, review_text=review_text)
    # review = Order(customer_id=customer_id, status='NEW')
    try:
        db.session.add(review)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the review. " + str(e)
            }
        ), 500
    
    print(json.dumps(review.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": review.json()
        }
    ), 201


@app.route("/review/<string:review_id>", methods=['PUT'])
def update_review(review_id):
    try:
        review = Review.query.filter_by(review_id=review_id).first()
        if not review:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "review_id": review_id
                    },
                    "message": "Review not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['rating']:
            review.rating = data['rating']
        if data['review_text']:
            review.review_text = data['review_text']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": review.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "review_id": review_id
                },
                "message": "An error occurred while updating the review. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5004, debug=True)
