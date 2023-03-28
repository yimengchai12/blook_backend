#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

import stripe
# This is your test secret API key.
stripe.api_key = "sk_test_51Miv0mDVT8kjXSeFhyISeAE8DvBk8A2i1naRDbWDYNEblx1IiBTkbG5fXBG38daqRngJSiq1cpx25hSkZ1OPNrTN00oqJCRNJF"

# 'sk_test_51MqXdHE3thje2p8MDiPdiAf9rL1wQHZirFYfmKIetPDBkvyX2avd9BtxfIJ1BpThFRSTyoBSGBbk48BQygVYXkWo00kAK2chaW'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:5006'#idk what localhost to use

CORS(app)  
@app.route('/<string:product_id>', methods=['GET'])
def get_product_id(product_id):
    # Replace "PRODUCT_ID" with the ID of the product you want to retrieve the default price for
    # Retrieve the product object using its ID
    product = stripe.Product.retrieve(product_id)

    # Get the default price ID from the product object
    default_price_id = product.default_price.id

    # Print the default price ID
    return jsonify(
            {
                "code": 200,
                "data": {
                    "price_id": default_price_id
                }
            }
        )

@app.route('/create-checkout-session/<string:price_id>/<string:quantity>', methods=['POST'])
def create_checkout_session(price_id, quantity):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': price_id,
                    'quantity': quantity,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": stripe payment ...")
    app.run(host='0.0.0.0', port=5006, debug=True)
