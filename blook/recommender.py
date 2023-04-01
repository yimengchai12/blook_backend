from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http
import numpy
# import amqp_setup
# import pika
# import json

app = Flask(__name__)
CORS(app)

activity_URL = "http://127.0.0.1:5001/activity"
review_URL = "http://127.0.0.1:5004/review"


@app.route("/")
def sendRecommendation():
    # Simple check of input format and data of the request are JSON
    print("---Starting up Recommendation microservice---\n")

    result = processRecommendation()
    print('\n------------------------')
    print('\nFINAL result: ', result)
    return jsonify(result), result["code"]


def processRecommendation():
    print('\n\n-----GET data from Activity microservice-----')
    activity_result = invoke_http(activity_URL, method='GET', json=None)
    activity_data_list = activity_result['data']['activities']

    print('\n\n-----GET data from Reviews microservice-----')
    review_result = invoke_http(review_URL, method='GET', json=None)
    review_data_list = review_result['data']['reviews']

    recommendation_dict = {}

    for activity in activity_data_list:
        for review in review_data_list:
            activity_ID = activity['id']
            review_rating = review['rating']
            review_activity = review['activity_id']

            if review_activity == activity_ID:
                if activity_ID not in recommendation_dict:
                    recommendation_dict[activity_ID] = [review_rating]
                elif  activity_ID in recommendation_dict:
                    recommendation_dict[activity_ID].append(review_rating)

    for activity in recommendation_dict:
        avg_rating = numpy.average(recommendation_dict[activity])
        recommendation_dict[activity] = avg_rating
    
    sorted_recommendation_dict = sorted(recommendation_dict.items(), key=lambda x:x[1], reverse=True)
    new_recommendation_dict = dict(sorted_recommendation_dict)

    output_dict = {}
    count = 0
    for activity in new_recommendation_dict:
        if count != 6:
            output_dict[activity] = new_recommendation_dict[activity]
            count +=1
        else:
            break

    print(f"---------This is the dict of recco in the format of (activity_id: avg_rating): {output_dict}---------")

    output = []
    mem = {}
    for activity_id in output_dict:
        activity_result = invoke_http(activity_URL + "/" + str(activity_id), method='GET', json=None)
        mem["id"] = activity_id
        mem['name'] = activity_result['data']['name']
        mem['description'] = activity_result['data']['description']
        mem['price'] = activity_result['data']['price']
        mem['address'] = activity_result['data']['address']
        mem["average_rating"] = output_dict[activity_id]
        output.append(mem)
        mem ={}
         
    print(f"THIS IS THE OUTPUT BEFORE JSON:  {output}")
    return {
                "code": 200,
                "data": output
            }

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
