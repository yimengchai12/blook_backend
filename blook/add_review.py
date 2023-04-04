import sys
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from invokes import invoke_http


app = Flask(__name__)
CORS(app)

customer_URL = "http://customer:5003/customer/"
review_URL = "http://review:5004/" # add to the back "review" or "pendingReview"

@app.route("/add_review", methods=['POST'])
def receiveVerification():
    print("\n----- Starting the Add Review Micro Service -----\n")
    order = None
    if request.is_json:
        order = request.get_json()
        print(order)
        print("***Successfully received request in JSON format***\n")

        result1 = addReview(order)

        return jsonify(result1), result1["code"]
    
    else:
        data = request.get_data()
        print("Received an invalid order:")
        print(data)
        return jsonify({"code": 400,
                        # make the data string as we dunno what could be the actual format
                        "data": str(data),
                        "message": "Order should be in JSON."}), 400  # Bad Request input


def addReview(order):
    print("Sending POST to:  " + review_URL + "review")
    create_review_result = invoke_http(review_URL + "review", method='POST', json=order)
    print(f"{create_review_result}\n")
    code = create_review_result["code"]
    if code not in range(200, 300):
        return {
                "code": 500,
                "data": {"review": create_review_result},
                "message": "Review creation failure."
            }

    customer_ID = order["customer_id"]
    print("Sending PUT to:  " + customer_URL + str(customer_ID) + "/add_review")
    customer_result = invoke_http(customer_URL + str(customer_ID) + "/add_review", method='PUT', json=None)
    print(f"{customer_result}\n")
    code = create_review_result["code"]
    if code not in range(200, 300):
        return {
                "code": 500,
                "data": {"customer": customer_result},
                "message": "Customer retrieval failure."
            }


    activity_ID = order["activity_id"]
    print("Sending DELETE to:  " + review_URL + "/review/pendingReview/" + str(customer_ID) + "/" + str(activity_ID))
    pendingReview = invoke_http(review_URL + "/review/pendingReview/" + str(customer_ID) + "/" + str(activity_ID), method='DELETE', json=None)
    print(f"{pendingReview}\n")
    code = pendingReview["code"]
    if code not in range(200, 300):
        return {
                "code": 500,
                "data": {"pendingReview": pendingReview},
                "message": "pendingReview retrieval failure."
            }
    

    return {
        "code": 200,
        'message': 'Review complex service successfully completed'
        }

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          ": add review microservice ...")
    app.run(host='0.0.0.0', port=5144, debug=True)
    



