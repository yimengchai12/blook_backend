from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/activity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "Hello, World!"













if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
