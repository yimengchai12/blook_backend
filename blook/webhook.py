import os
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import sys
from os import environ

import requests
from invokes import invoke_http
import json


import stripe
from invokes import invoke_http
booking_URL = "http://booking:5002/booking"
customer_URL = "http://customer:5003/customer"
send_email_URL = "http://send_email:5020/send_email"


# This is your test secret API key.
stripe.api_key = "sk_test_51Miv0mDVT8kjXSeFhyISeAE8DvBk8A2i1naRDbWDYNEblx1IiBTkbG5fXBG38daqRngJSiq1cpx25hSkZ1OPNrTN00oqJCRNJF"

# 'sk_test_51MqXdHE3thje2p8MDiPdiAf9rL1wQHZirFYfmKIetPDBkvyX2avd9BtxfIJ1BpThFRSTyoBSGBbk48BQygVYXkWo00kAK2chaW'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:5010'  # idk what localhost to use
# app.config['STRIPE_SECRET_KEY']="sk_test_51Miv0mDVT8kjXSeFhyISeAE8DvBk8A2i1naRDbWDYNEblx1IiBTkbG5fXBG38daqRngJSiq1cpx25hSkZ1OPNrTN00oqJCRNJF"

CORS(app)
# @app.route('/<string:product_id>', methods=['GET'])
# def get_product_id(product_id):
#     # Replace "PRODUCT_ID" with the ID of the product you want to retrieve the default price for
#     # Retrieve the product object using its ID
#     product = stripe.Product.retrieve(product_id)
#     # Get the default price ID from the product object
#     default_price_id = product.default_price

#     # Print the default price ID
#     return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "price_id": default_price_id
#                 }
#             }
#         )


@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = 'whsec_9a44ebec0d6a46d09a2238b75e46a20583d3d28b8256c9809e69157e5ee9c373'
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        # Invalid payload
        print('inalid payload')
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('invaid siganature')
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        print(event["data"]['object']["client_reference_id"])
        booking = json.loads(event["data"]['object']["client_reference_id"])
        print(event)
        print('\n-----Invoking booking microservice-----')
        booking_result = invoke_http(booking_URL, method='POST', json=booking)
        print('booking_result:', booking_result)
        code = booking_result["code"]
        message = json.dumps(booking_result)

        print('\n-----Invoking customer microservice-----')
        customer_id = booking["customer_id"]
        customer_result = invoke_http(
            customer_URL + "/" + customer_id, method='PUT', json=booking_result['data'])
        print('customer_result:', customer_result)
        code = customer_result["code"]
        message = json.dumps(customer_result)

        print('\n-----Invoking email microservice-----')
        # customer_id = booking["customer_id"]
        email_result = invoke_http(send_email_URL, method='POST', json=booking_result['data'])
        print('email_result:', email_result)
        code = email_result["code"]
        message = json.dumps(email_result)

    if event["type"] == "charge.succeeded":
        return jsonify(
{
                "code": 200,
                "message": "There are chargre."
            }
        ), 200

    return jsonify(
        {
            "code": 200,
            "message": "There are no books."
        }
    ), 200

    # TODO: run some custom code here


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": stripe payment ...")
    app.run(host='0.0.0.0', port=5010, debug=True)

