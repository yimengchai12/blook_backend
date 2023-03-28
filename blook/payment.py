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
stripe.api_key = 'sk_test_51MqXdHE3thje2p8MDiPdiAf9rL1wQHZirFYfmKIetPDBkvyX2avd9BtxfIJ1BpThFRSTyoBSGBbk48BQygVYXkWo00kAK2chaW'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:'#idk what localhost to use

CORS(app)  

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
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
    app.run(host='0.0.0.0', port=5005, debug=True)
