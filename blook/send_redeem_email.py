
# need to pip install sendgrid 

import sys
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from invokes import invoke_http

import amqp_setup

# monitorBindingKey='#'


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
CORS(app)



booking_URL = "http://booking:5002/booking"
activity_URL = "http://activity:5001/activity"
customer_URL = "http://customer:5003/customer"



@app.route("/send_redeem_email", methods=['POST'])
def receiveRedeemEmailRequest():
    amqp_setup.check_setup()
    queue_name = 'Redeem_Log'
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived a email request by " + __file__)
    print() # print a new line feed


    # Check if the order contains valid JSON
    print("\n-----Email request received-----")
    order = None
    if request.is_json:
        order = request.get_json()
        print(order)
        print("***Successfully received email request in JSON format***")
        print("processing email")
        result = sendRedeemEmail(json.loads(body))
        return jsonify(result), result["code"]
    else:
        data = request.get_data()
        print("Received an invalid order:")
        print(data)
        return jsonify({"code": 400,
                        # make the data string as we dunno what could be the actual format
                        "data": str(data),
                        "message": "Order should be in JSON."}), 400  # Bad Request input


def sendRedeemEmail(order):
    print("\n -------------Processing the sending of email notification-----------------\n")
    print(f"\nBooking:   {order}\n")
    customer_ID = order['data']["customer_id"]
    activity_ID = order['data']['activity_id']

    # GET Customer details
    customer_result = invoke_http(customer_URL + "/" + str(customer_ID), method='GET')
    print('customer_result:', customer_result)
    print(customer_result)
    customer_name = customer_result["data"]["first_name"] + " " + customer_result["data"]["last_name"]
    customer_email = customer_result["data"]["email"]
    print(f"\nBooking for {customer_name} with the email {customer_email}")

    # GET Activity details
    activity_result = invoke_http(activity_URL + "/" + str(activity_ID), method='GET', json=None)
    print(f"this is activity_result: {activity_result}")
    activity_name = activity_result["data"]["name"]
    print(f"{activity_name} was booked\n")
    

    print("------Preparing to send email--------")
    message = Mail(
    from_email='julianooi80@gmail.com',
    to_emails="yimengchai12@gmail.com",
    subject='Thank you! Leave a review!',
    html_content=f'<h2>Dear {customer_name}</h2>, <br> <h3>Thank you for booking <strong>{activity_name}</strong> with us. We hope you enjoyed you time with us! Do leave us a review to let us know how we can improve! Posting a review will earn you 100 points</h3>')

    try:
        sg = SendGridAPIClient("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")
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
    receiveRedeemEmailRequest()
    app.run(host='0.0.0.0', port=5022, debug=True)
    



