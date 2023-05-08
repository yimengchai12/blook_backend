
# need to pip install sendgrid 

import sys
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from invokes import invoke_http
from dotenv import load_dotenv

import amqp_setup
load_dotenv()

# monitorBindingKey='#'


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
CORS(app)

booking_URL = "http://booking:5002/booking"
activity_URL = "http://activity:5001/activity"
customer_URL = "http://customer:5003/customer"

@app.route("/send_email", methods=['POST'])
def receiveEmailRequest():
    amqp_setup.check_setup()
    queue_name = 'Booking_Log'
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived a email request by " + __file__)
    sendEmail(json.loads(body))
    print() # print a new line feed


    # Check if the order contains valid JSON
    print("\n-----Email request received-----")
    order = None
    if request.is_json:
        order = request.get_json()
        print(order)
        print("***Successfully received email request in JSON format***")
        print("processing email")
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

# @app.route("/send_redeem_email", methods=['POST'])
def sendEmail(order):
    print("\n -------------Processing the sending of email notification-----------------\n")
    print(f"\nRedeem Booking:   {order}\n")
    booking_ID = order["data"]["id"]
    customer_ID = order["data"]["customer_id"]
    activity_ID = order["data"]['activity_id']
    total_pax = order["data"]["total_pax"]

    customer_result = invoke_http(customer_URL + "/" + str(customer_ID), method='GET')
    print('customer_result:', customer_result)
    # # customer_result=json.dumps(customer_result)
    print(customer_result)
    # print("check" + customer_result)
    customer_name = customer_result["data"]["first_name"] + " " + customer_result["data"]["last_name"]
    customer_email = customer_result["data"]["email"]
    print(f"\nBooking with ID {booking_ID} is for {customer_name} with the email {customer_email}")
  

    booking_result = invoke_http(booking_URL + "/" + str(booking_ID), method='GET', json=None)
    total_pax = booking_result["data"]["total_pax"]
    payment_amt = booking_result["data"]["payment_amount"]

    activity_result = invoke_http(activity_URL + "/" + str(activity_ID), method='GET', json=None)
    activity_name = activity_result["data"]["name"]

    print(f"{activity_name} for {total_pax} pax and ${payment_amt} has been successfully paid\n")
    

    print("------Preparing to send email--------")
    message = Mail(
    from_email='julianooi80@gmail.com',
    to_emails=customer_email,
    subject='Your booking has been confirmed',
    html_content=f'<h2>Dear {customer_name}</h2>, <br> <h3>Your booking for <strong>{activity_name}</strong> for a total of {total_pax} pax has been confirmed. Your booking ID is <strong>{booking_ID}</strong>.<br>We hope you enjoy your time!</h3>')

    try:
        sg = SendGridAPIClient(os.getenv("sendgrid_api"))
        response = sg.send(message)
        code = response.status_code
        print("Email successfully send!\nStatus code: ", code)
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
    # print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveEmailRequest()
    app.run(host='0.0.0.0', port=5020, debug=True)
    



