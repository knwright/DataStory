from flask import Flask, render_template
from flask_restplus import Api, Resource
import pymongo 
import pandas as pd
import os

# Read the data.
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db=client.bigfootdb

# Restful flask app
app = Flask(__name__)
api = Api(app=app)

# Homepage route displaying the story
@api.route("/")
class mainpage(Resource):
    def get(self):
        return render_template("index.html")

# Route displaying graphs
@api.route("/visualizations")
class graphs(Resource):
    def get(self):
        return render_template("index.html")

# Route displaying data
@api.route("/data")
class data(Resource):
    def get(self):
        data = list(db.STATE.find())
        print(data)
        # return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)