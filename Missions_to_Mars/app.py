import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_pymongo import PyMongo

from flask import Flask, jsonify, render_template, redirect, url_for

#################################################
# Database Setup
#################################################

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app.config["MONGO_URI"]= "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    mars_data = mongo.db.mars_db.find_one()
    print(mars_data)
    return render_template("Mars_index.html", data = mars_data)


@app.route("/scrape")
def names():
   from scrape_mars import scrape
   mars_scrape = scrape()
   mars= mongo.db.mars_db
   mars.update_one({},{"$set":mars_scrape},True)

   return redirect("/",code=302)

if __name__ == '__main__':
    app.run(debug=True)
