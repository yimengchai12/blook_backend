from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

customer_URL = "http://customer:5003/customer"
booking_URL = environ.get('booking_URL') or "http://booking:5001/booking" 
# shipping_record_URL = environ.get('shipping_record_URL') or "http://localhost:5002/shipping_record" 
# booking_log_URL = "http://localhost:5006/activity_log"
error_URL = "http://localhost:5008/error"


@app.route("/place_booking", methods=['POST'])
def place_booking():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            booking = request.get_json()
            print("\nReceived a booking in JSON:", booking)
            
            # r = requests.get('http://customer:5003/customer/1')
            # print('hello r ', r)
            # do the actual work
            # 1. Send order info {cart items}
            result = processBookingOrder(booking)
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
                "message": "place_booking.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400
    



def processBookingOrder(booking):
    #invoke customer microservice 
    print('\n-----Invoking customer microservice-----')
    customer_id = booking["customer_id"]
    customer_result = invoke_http(customer_URL + "/" + customer_id)
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
    
  

    # Invoke the booking microservice
    print('\n-----Invoking booking microservice-----')
    booking_result = invoke_http(booking_URL, method='POST', json=booking)
    print('booking_result:', booking_result)
  
    # Check the order result; if a failure, send it to the error microservice.
    code = booking_result["code"]
    message = json.dumps(booking_result)

    amqp_setup.check_setup()

    if code not in range(200, 300):
        # Inform the error microservice
        #print('\n\n-----Invoking error microservice as order fails-----')
        print('\n\n-----Publishing the (order error) message with routing_key=order.error-----')

        # invoke_http(error_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="booking.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
        # make message persistent within the matching queues until it is received by some receiver 
        # (the matching queues have to exist and be durable and bound to the exchange)

        # - reply from the invocation is not used;
        # continue even if this invocation fails        
        print("\nBooking status ({:d}) published to the RabbitMQ Exchange:".format(
            code), booking_result)

        # 7. Return error
        return {
            "code": 500,
            "data": {"booking_result": booking_result},
            "message": "booking creation failure sent for error handling."
        }

    # Notice that we are publishing to "Activity Log" only when there is no error in order creation.
    # In http version, we first invoked "Activity Log" and then checked for error.
    # Since the "Activity Log" binds to the queue using '#' => any routing_key would be matched 
    # and a message sent to “Error” queue can be received by “Activity Log” too.

    else:
        # 4. Record new order
        # record the activity log anyway
        #print('\n\n-----Invoking activity_log microservice-----')
        print('\n\n-----Publishing the (booking info) message with routing_key=booking.info-----')        

        # invoke_http(activity_log_URL, method="POST", json=order_result)            
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="booking.info", 
            body=message)
    
    print("\nOrder published to RabbitMQ Exchange.\n")
    # - reply from the invocation is not used;
    # continue even if this invocation fails
    
    # 5. Send new order to shipping
    # Invoke the shipping record microservice
    # print('\n\n-----Invoking shipping_record microservice-----')    
    
    # shipping_result = invoke_http(
    #     shipping_record_URL, method="POST", json=order_result['data'])
    # print("shipping_result:", shipping_result, '\n')

    # # Check the shipping result;
    # # if a failure, send it to the error microservice.
    # code = shipping_result["code"]
    # if code not in range(200, 300):
    #     # Inform the error microservice
    #     print('\n\n-----Invoking error microservice as shipping fails-----')
    #     print('\n\n-----Publishing the (shipping error) message with routing_key=shipping.error-----')

    #     invoke_http(error_URL, method="POST", json=shipping_result)
    #     message = json.dumps(shipping_result)
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="shipping.error", 
    #         body=message, properties=pika.BasicProperties(delivery_mode = 2))

    #     print("\nShipping status ({:d}) published to the RabbitMQ Exchange:".format(
    #         code), shipping_result)

    #     # # 7. Return error
    #     return {
    #         "code": 400,
    #         "data": {
    #             "order_result": order_result,
    #             "shipping_result": shipping_result
    #         },
    #         "message": "Simulated shipping record error sent for error handling."
    #     }

    # # 7. Return created order, shipping record
    # return {
    #     "code": 201,
    #     "data": {
    #         "order_result": order_result,
    #         "shipping_result": shipping_result
    #     }
    # }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
