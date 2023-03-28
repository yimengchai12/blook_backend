
# need to pip install sendgrid 

import sys
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
# from invokes import invoke_http

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
CORS(app)

booking_URL = "http://localhost:5004/booking"

@app.route("/send_email", methods=['POST'])
def receiveEmailRequest():
    # Check if the order contains valid JSON
    print("--email request received--")
    order = None
    if request.is_json:
        order = request.get_json()
        print("received email request in json:  ", order)
        result = sendEmail(order)
        return jsonify(result), result["code"]
    else:
        data = request.get_data()
        print("Received an invalid order:")
        print(data)
        return jsonify({"code": 400,
                        # make the data string as we dunno what could be the actual format
                        "data": str(data),
                        "message": "Order should be in JSON."}), 400  # Bad Request input


def sendEmail(order):
    print("Processing the sending of email notification")
    print(order)
    print("tetstetstetstfwefewgfweg")
    booking_ID = order['data']["id"]
    customer_ID = order['data']["customer_id"]
    total_pax = order['data']["total_pax"]

    customer_data = request.get_data(f'http://localhost:5003/customer/{customer_ID}')
    print(customer_data)
    customer_data = customer_data.json()
    customer_name = customer_data["data"]["first_name"]
    print("customer name: " + customer_name +"\n")
    
    activity_data = request.get_data(f'http://localhost:5001/activity/{booking_ID}')
    activity_data = activity_data.json()
    activity_name = activity_data["data"]["name"]

    message = Mail(
    from_email='julianooi80@gmail.com',
    to_emails='mrjulianooii@gmail.com',
    subject='Your booking has been confirmed',
    html_content=f'<h2>Dear {customer_name}</h2>, <br> <h3>Your booking for <strong>{activity_name}</strong> for a total of {total_pax} pax has been confirmed. Your booking ID is <strong>{booking_ID}</strong>.<br>We hope you enjoy your time!</h3>')

    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        code = response.status_code
        print("Status code: ", code)
        return {
            'code': code,
            'message': "success"
        }
        # print("Response body: ")
        # print(response.body)
        # print("response header: ")
        # print(response.headers)
    except Exception as e:
        print(e.message)


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          ": send email microservice ...")
    app.run(host='0.0.0.0', port=5005, debug=True)
    



