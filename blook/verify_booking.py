import sys
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from invokes import invoke_http

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
CORS(app)

booking_URL = "http://localhost:5002/booking"
send_email_URL = "http://send_email:5020/send_email_verify"
# activity_URL = "http://localhost:5001/activity"
# customer_URL = "http://localhost:5003/customer"

@app.route("/verify_booking", methods=['POST'])
def receiveVerification():
    print("----- vendor verifying booking by customer -----")
    order = None
    if request.is_json:
        order = request.get_json()
        print(order)
        print("***Successfully received verify request in JSON format***")
        print("---Verifiying booking---")
        result = sendVerification(order)
        print("\n---Verifiying booking success---\n")
        print(f"Booking Status updated: {result}\n")

        if result['code'] in range(200,300):
            print("---Invoking email micoservice---\n")
            email_result = sendVerifyBookingEmail(order)
            print("\n---email success---\n")

        return jsonify(result), result["code"]
    
    else:
        data = request.get_data()
        print("Received an invalid order:")
        print(data)
        return jsonify({"code": 400,
                        # make the data string as we dunno what could be the actual format
                        "data": str(data),
                        "message": "Order should be in JSON."}), 400  # Bad Request input


def sendVerification(order):
        print("\n -------------Processing the verification of booking-----------------\n")
        print(f"Order:    {order}")
        booking_ID = order["id"]
        test = '{"status": "YES"}'
        update = json.loads(test)

        print("\nPOST to: " + booking_URL + "/" + str(booking_ID))
        bookingUpdate_result = invoke_http(booking_URL + "/" + str(booking_ID), method='PUT', json=update)
        changed = bookingUpdate_result['data']
        print(f"this is the result: {changed}")

        return {
            "code": 201,
            "data": [changed]
        }

def sendVerifyBookingEmail(order):
    print("\n ----------Preparing to send req to email microserivce------------\n")
    print(f"Order:    {order}")
    booking_ID = order["id"]
    email_result = invoke_http(send_email_URL, method='POST', json=order)



if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          ": verify booking microservice ...")
    app.run(host='0.0.0.0', port=5030, debug=True)
    



