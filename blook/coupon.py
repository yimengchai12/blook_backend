from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/coupon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Coupon(db.Model):
    __tablename__ = 'coupon'

    coupon_id = db.Column(db.Integer, primary_key=True)
    coupon_point = db.Column(db.Integer, nullable=False)
    coupon_code = db.Column(db.String(50), nullable=False)

    def __init__(self,coupon_id, coupon_point, coupon_code):
        self.coupon_id = coupon_id
        self.coupon_point = coupon_point
        self.coupon_code = coupon_code

    def json(self):
        return { "coupon_id":self.coupon_id ,"coupon_point": self.coupon_point, "coupon_code": self.coupon_code}


class Coupon_Customer(db.Model):
    __tablename__ = 'coupon_customer'

    coupon_customer_id = db.Column(db.Integer, primary_key=True)
    coupon_id = db.Column(db.Integer, nullable= False)
    coupon_point = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)

    def json(self):
        return { "coupon_customer_id":self.coupon_customer_id ,"coupon_id":self.coupon_id ,"coupon_point": self.coupon_point, "customer_id": self.customer_id}





@app.route("/coupon")
def get_all():
    couponlist = Coupon.query.all()
    if len(couponlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "coupons": [coupon.json() for coupon in couponlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no coupon."
        }
    ), 404



@app.route("/coupon/get/<string:coupon_point>")
def get_coupon_with_point(coupon_point):
    coupon = Coupon.query.filter_by(coupon_point = coupon_point).first()
    if coupon:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "coupon": coupon.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no coupon."
        }
    ), 404


@app.route("/coupon/<string:coupon_point>")
def find_by_id(coupon_point):
    couponlist = Coupon.query.filter(Coupon.coupon_point <= coupon_point)
    if couponlist:
        return jsonify(
            {
                "code": 200,
                "data": [coupon.json() for coupon in couponlist]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Coupon not found."
        }
    ), 404


@app.route("/coupon/<string:customer_id>/<string:coupon_id>/<string:coupon_point>", methods=['POST'])
def create_coupon_customer(customer_id, coupon_id, coupon_point):
    coupon_customer = Coupon_Customer(customer_id = customer_id, coupon_id =coupon_id, coupon_point = coupon_point)
    try:
        db.session.add(coupon_customer)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the coupon exchange. " + str(e)
            }
        ), 500
    
    print(json.dumps(coupon_customer.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": coupon_customer.json()
        }
    ), 201



@app.route("/coupon/linked/<string:customer_id>")
def get_customer_linked_coupon(customer_id):
    couponlist = Coupon_Customer.query.filter_by(customer_id = customer_id)
    if couponlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "coupon": [coupon.json() for coupon in couponlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no coupon."
        }
    ), 404


#delete coupon 
@app.route("/coupon/<string:customer_id>/<string:coupon_id>", methods=['DELETE'])
def delete_customer_linked_coupon(customer_id, coupon_id):
    coupon = Coupon_Customer.query.filter_by(customer_id = customer_id, coupon_id = coupon_id).first()
    if coupon:
        db.session.delete(coupon)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "coupon": coupon.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no existing coupon."
        }
    ), 404



# @app.route("/coupon/<string:id>", methods=['POST'])
# def create_activity(id):
#     if (Activity.query.filter_by(id=id).first()):
#         return jsonify(
#             {
#                 "code": 400,
#                 "data": {
#                     "id": id
#                 },
#                 "message": "Activity already exists."
#             }
#         ), 400

    # data = request.get_json()
    # activity = Activity(id, **data)

    # try:
    #     db.session.add(activity)
    #     db.session.commit()
    # except:
    #     return jsonify(
    #         {
    #             "code": 500,
    #             "data": {
    #                 "id": id
    #             },
    #             "message": "An error occurred creating the activity."
    #         }
    #     ), 500

    # return jsonify(
    #     {
    #         "code": 201,
    #         "data": activity.json()
    #     }
    # ), 201


# @app.route("/activity/<string:id>", methods=['PUT'])
# def update_activity(id):
#     activity = Activity.query.filter_by(id=id).first()
#     if activity:
#         data = request.get_json()
#         if data['title']:
#             activity.title = data['title']
#         if data['price']:
#             activity.price = data['price']
#         if data['availability']:
#             activity.availability = data['availability'] 
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": activity.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "id": id
#             },
#             "message": "Activity not found."
#         }
#     ), 404


# @app.route("/activity/<string:id>", methods=['DELETE'])
# def delete_activity(id):
#     activity = Activity.query.filter_by(id=id).first()
#     if activity:
#         db.session.delete(activity)
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "id": id
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "id": id
#             },
#             "message": "Activity not found."
#         }
#     ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5013, debug=True)
