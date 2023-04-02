from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

# import amqp_setup
# import pika
import json

app = Flask(__name__)
CORS(app)

customer_URL = "http://customer:5003/customer"
activity_URL = environ.get('booking_URL') or "http://booking:5002/booking" 
error_URL = "http://localhost:5008/error"
payment_URL = "http://payment:5006/payment"


# { "customer_id": 2, "activity_id": 2 }
@app.route("/get_booking_details/<string:customer_id>/<string:activity_id>", methods=['GET'])
def get_booking_details(customer_id, activity_id):
    # Simple check of input format and data of the request are JSON
    # if not request.is_json:
    try:
        # booking_details = request.get_json()
        # print("\nReceived a booking in JSON:", booking_details)
        # do the actual work
        # 1. Send order info {cart items}
        result = processBookingDetails(customer_id, activity_id)
        print('\n------------------------')
        print('\nresult: ', result)
        return jsonify(result), result["code"]

    except Exception as e:
        # Unexpected error in code
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": "get_booking_details.py internal error: " + ex_str
        }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400
    



def processBookingDetails(customer_id, activity_id):
    #invoke customer microservice 
    print('\n-----Invoking customer microservice-----')
    # customer_id = booking_details["customer_id"]
    customer_result = invoke_http(customer_URL + "/" + str(customer_id))
    print('customer_result:', customer_result)

    code = customer_result["code"]
    message = json.dumps(customer_result)
    if code not in range(200, 300):
        print('\n\n-----Invoking error microservice as order fails-----')
        invoke_http(error_URL, method="POST", json=customer_result)
        # - reply from the invocation is not used; 
        # continue even if this invocation fails
        print("customer status ({:d}) sent to the error microservice:".format(
            code), customer_result)

        # 7. Return error
        return {
                "code": 500,
                "data": {"customer_result": customer_result},
                "message": "Customer retrieval failure sent for error handling."
            }
    
    

    # Invoke the activity microservice
    print('\n-----Invoking activity microservice-----')
    # activity_id = booking_details["activity_id"]
    activity_result = invoke_http(activity_URL + "/" + str(activity_id))
    print('activity_result:', activity_result)

    code = activity_result["code"]
    message = json.dumps(activity_result)
    if code not in range(200, 300):
        print('\n\n-----Invoking error microservice as order fails-----')
        invoke_http(error_URL, method="POST", json=activity_result)
        # - reply from the invocation is not used; 
        # continue even if this invocation fails
        print("activity status ({:d}) sent to the error microservice:".format(
            code), activity_result)

        # 7. Return error
        return {
                "code": 500,
                "data": {"activity": activity_result},
                "message": "Activity retrieval failure sent for error handling."
            }
    

    # Invoke the activity microservice
    # print('\n-----Invoking payment microservice-----')
    # product_id = activity_id
    # print(payment_URL + "/" + str(product_id))
    # product_result = invoke_http(payment_URL + "/" + str(product_id))
    # print('product_result:', product_result)

    # code = product_result["code"]
    # message = json.dumps(product_result)
    # if code not in range(200, 300):
    #     print('\n\n-----Invoking error microservice as order fails-----')
    #     invoke_http(error_URL, method="POST", json=product_result)
    #     # - reply from the invocation is not used; 
    #     # continue even if this invocation fails
    #     print("activity status ({:d}) sent to the error microservice:".format(
    #         code), product_result)

    #     # 7. Return error
    #     return {
    #             "code": 500,
    #             "data": {"product": product_result},
    #             "message": "product retrieval failure sent for error handling."
    #         }
  




    # # 7. Return created order, shipping record
    return {
        "code": 201,
        "data": {
            "activity_result": activity_result,
            "customer_result": customer_result, 
            # "product_result": product_result
        }
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5012, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
