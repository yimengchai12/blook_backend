#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ
from dotenv import load_dotenv

load_dotenv()

import requests
from invokes import invoke_http
import json


import stripe
from invokes import invoke_http
# booking_URL =  "http://booking:5002/booking" 


# This is your test secret API key.
stripe.api_key = os.getenv("STRIPE_KEY")

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:5006'#idk what localhost to use
# app.config['STRIPE_SECRET_KEY']="sk_test_51Miv0mDVT8kjXSeFhyISeAE8DvBk8A2i1naRDbWDYNEblx1IiBTkbG5fXBG38daqRngJSiq1cpx25hSkZ1OPNrTN00oqJCRNJF"

CORS(app)  
@app.route('/payment/<string:product_id>', methods=['GET'])
def get_product_id(product_id):
    # Replace "PRODUCT_ID" with the ID of the product you want to retrieve the default price for
    # Retrieve the product object using its ID
    product = stripe.Product.retrieve(product_id)
    # Get the default price ID from the product object
    default_price_id = product.default_price
    return default_price_id
    # Print the default price ID
    # return jsonify(
    #         {
    #             "code": 200,
    #             "data": {
    #                 "price_id": default_price_id
    #             }
    #         }
    #     )

# from get_booking_details result, pass result.data.product_result.price_id, quantity from front end. pass a json from front end to receive request on backend.
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_details = request.get_json()
        print("\nReceived checkout details in JSON:", checkout_details)
        customer_id = checkout_details["customer_id"]
        print("\nCustomer ID:", customer_id)
        activity_id = checkout_details["activity_id"]
        print("\nActivity ID:", activity_id)
        quantity = checkout_details["total_pax"]
        print("\nTotal Pax:", quantity)
        datetime = checkout_details["datetime"]
        print("\nDatetime:", datetime)
        payment_amount = checkout_details["payment_amount"] #need multiply by quantity on front end
        price_id = get_product_id(activity_id)
        print("\nPayment Amount:", payment_amount)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': price_id,
                    'quantity': quantity,

                },
            ],
            mode='payment',
            # success_url=YOUR_DOMAIN + '/success.html',
            success_url = 'http://127.0.0.1:3000/bookingsuccessful',
            # cancel_url=YOUR_DOMAIN + '/cancel.html',
            # allow_promotion_codes = True,
            client_reference_id = json.dumps(checkout_details),
            # discounts=[{'coupon': ''},],
            cancel_url = 'http://127.0.0.1:3000/bookingfailed',
        )
    except Exception as e:
        return str(e)

    # return redirect(checkout_session.url, code=303)
    return {'url': checkout_session.url}


@app.route('/create-checkout-session/<string:coupon_id>', methods=['POST'])
def create_checkout_session_with_Coupon(coupon_id):
    try:
        checkout_details = request.get_json()
        print("\nReceived checkout details in JSON:", checkout_details)
        customer_id = checkout_details["customer_id"]
        print("\nCustomer ID:", customer_id)
        activity_id = checkout_details["activity_id"]
        print("\nActivity ID:", activity_id)
        quantity = checkout_details["total_pax"]
        print("\nTotal Pax:", quantity)
        datetime = checkout_details["datetime"]
        print("\nDatetime:", datetime)
        payment_amount = checkout_details["payment_amount"] #need multiply by quantity on front end
        price_id = get_product_id(activity_id)
        print("\nPayment Amount:", payment_amount)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': price_id,
                    'quantity': quantity,

                },
            ],
            mode='payment',
            # success_url=YOUR_DOMAIN + '/success.html',
            success_url = 'http://127.0.0.1:3000/bookingsuccessful',
            # cancel_url=YOUR_DOMAIN + '/cancel.html',
            # allow_promotion_codes = True,
            client_reference_id = json.dumps(checkout_details),
            discounts=[{'coupon': coupon_id},],
            cancel_url =  'http://127.0.0.1:3000/bookingfailed',
        )
    except Exception as e:
        return str(e)

    # return redirect(checkout_session.url, code=303)
    return {'url': checkout_session.url}












if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": stripe payment ...")
    app.run(host='0.0.0.0', port=5006, debug=True)
