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
send_email_URL = "http://127.0.0.1:5020/send_email"
pendingReview_URL = "http://localhost:5004/pendingReview"

@app.route("/verify_booking", methods=['POST'])
def receiveVerification():
    print("----- Starting the Verify Booking Micro Service -----\n")
    order = None
    if request.is_json:
        order = request.get_json()
        print(order)
        print("***Successfully received verify request in JSON format***\n")
        print("---Verifiying booking---\n")

        result1 = sendVerification(order)

        print("\n---Verifiying booking success---\n")
        print(f"Booking Status updated: {result1}\n")

        # if result['code'] in range(200,300):
        #     print("---Invoking email micoservice---\n")
        #     email_result = sendVerifyBookingEmail(order)
        #     print("\n---email success---\n")
        print("\n----- Ending  the Verify Booking Micro Service -----")
        return jsonify(result1), result1["code"]
    
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
        activity_id = order['activity_id']
        customer_id = order["customer_id"]
        test = '{"status": "YES"}'
        update = json.loads(test)

        # PUT to update booking status to YES
        print("\n----- Update booking -----")
        print("\nPOST to: " + booking_URL + "/" + str(booking_ID))
        bookingUpdate_result = invoke_http(booking_URL + "/" + str(booking_ID), method='PUT', json=update)
        print(bookingUpdate_result)
        changed = bookingUpdate_result['data']
        print(f"Successfully updated: {changed}")

        # POST to add new row into pendingReviews
        if bookingUpdate_result['code'] in range(200,300):
            print("\n----- Adding to pendingReviews -----")
            update2 = {"activity_id": activity_id, "customer_id":customer_id}
            pending_review_result = invoke_http(pendingReview_URL, method='POST', json=update2)
            print(f"Successfully added: {pending_review_result}")


            if pending_review_result['code'] in range(200,300):
                # POST to send email notification to review
                print("\n---Invoking email microservice---")
                email_result = invoke_http(send_email_URL, method='POST', json=update2)
                
                if email_result['code'] in range(200,300):
                    print(f"Successfully sent: {email_result}")
                    return {
                        "code": 201,
                        "data": [changed, pending_review_result['data'], email_result]
                    }

                # Email fail
                print("\n---Invoking email microservice failed---")
                return {
                        "code": 201,
                        "data": [changed, pending_review_result['data'], {"email_result": {"code" : 500}}]
                    }

            # Pending review + email fail
            print("\n---Invoking pending review microservice failed---")
            return {
                        "code": 201,
                        "data": [changed, {"pendingReview": {"code" : 500}}]
                    }

        # update booking status + Pending review + email fail
        print("\n---Invoking booking microservice failed---")
        return {
                        "code": 201,
                        "data": [{"booking": {"code" : 500}}]
                    }



if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          ": verify booking microservice ...")
    app.run(host='0.0.0.0', port=5030, debug=True)
    



