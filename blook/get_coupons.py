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
coupon_URL = "http://coupon:5013/coupon" 
error_URL = "http://localhost:5008/error"
# payment_URL = "http://payment:5006/payment"


# { "customer_id": 2, "activity_id": 2 }
@app.route("/get_coupons/<string:customer_id>", methods=['GET'])
def get_coupons(customer_id):
    # Simple check of input format and data of the request are JSON
    # if not request.is_json:
    try:
        # booking_details = request.get_json()
        # print("\nReceived a booking in JSON:", booking_details)
        # do the actual work
        # 1. Send order info {cart items}
        print('\n-----Invoking customer microservice-----')
        # customer_id = booking_details["customer_id"]
        customer_result = invoke_http(customer_URL + "/" + str(customer_id))
        print('customer_result:', customer_result)
        code = customer_result["code"]
        customer_point = customer_result["data"]["point"]
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
        else:
            print('\n-----Invoking coupon microservice-----')
            # customer_id = booking_details["customer_id"]
            coupon_result = invoke_http(coupon_URL + "/" + str(customer_point))
            print('coupon_result:', coupon_result)

            code = coupon_result["code"]
            message = json.dumps(coupon_result)
            if code not in range(200, 300):
                print('\n\n-----Invoking error microservice as order fails-----')
                invoke_http(error_URL, method="POST", json=coupon_result)
                # - reply from the invocation is not used; 
                # continue even if this invocation fails
                print("customer status ({:d}) sent to the error microservice:".format(
                    code), coupon_result)

                # 7. Return error
                return {
                        "code": 500,
                        "data": {"coupon_result": coupon_result},
                        "message": "Coupon retrieval failure sent for error handling."
                    }
            

        print('\n------------------------')
        print('\nresult: ', coupon_result)
        return coupon_result


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
    



# to exchange for coupons
@app.route("/get_coupons/<string:customer_id>/<string:coupon_point>", methods=['GET'])
def get_coupons_customer(customer_id, coupon_point):
    # Simple check of input format and data of the request are JSON
    # if not request.is_json:
    try:
        print('\n-----Invoking coupon microservice-----')
        coupon_result = invoke_http(coupon_URL + "/get/" + str(coupon_point))
        print('coupon_result:', coupon_result)

        code = coupon_result["code"]
        coupon_id = coupon_result["data"]["coupon"]["coupon_id"]
        message = json.dumps(coupon_result)
        if code not in range(200, 300):
            print('\n\n-----Invoking error microservice as order fails-----')
            invoke_http(error_URL, method="POST", json=coupon_result)
            # - reply from the invocation is not used; 
            # continue even if this invocation fails
            print("customer status ({:d}) sent to the error microservice:".format(
                code), coupon_result)

            # 7. Return error
            return {
                    "code": 500,
                    "data": {"coupon_result": coupon_result},
                    "message": "Coupon retrieval failure sent for error handling."
                }
        
        print('\n-----Invoking customer microservice-----')
        # customer_id = booking_details["customer_id"]
        customer_result = invoke_http(customer_URL + "/" + str(customer_id), method="PUT", json=coupon_result)
        print('customer_result:', customer_result)
        code = customer_result["code"]
        customer_point = customer_result["data"]["point"]
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
        
        print('\n-----Invoking coupon microservice-----')
        # customer_id = booking_details["customer_id"]
        coupon_customer_result = invoke_http(coupon_URL + "/" + str(customer_id) + "/" + str(coupon_id) + "/" + str(coupon_point) ,method="POST")
        print('customer_result:', coupon_customer_result)
        code = coupon_customer_result["code"]
        message = json.dumps(coupon_customer_result)
        if code not in range(200, 300):
            print('\n\n-----Invoking error microservice as order fails-----')
            invoke_http(error_URL, method="POST", json=coupon_customer_result)
            # - reply from the invocation is not used; 
            # continue even if this invocation fails
            print("customer status ({:d}) sent to the error microservice:".format(
                code), coupon_customer_result)

            # 7. Return error
            return {
                    "code": 500,
                    "data": {"coupon_customer_result": coupon_customer_result},
                    "message": "Coupon Customer retrieval failure sent for error handling."
                }
        

        print('\n------------------------')
        print('\nresult: ', coupon_customer_result)
        return coupon_customer_result


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

   

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5014, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
