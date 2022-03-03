#!/usr/bin/env python 

from flask import Flask, render_template
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)

#setup mongo connection with database
app.config['MONGO_URI']="mongodb://localhost:27017/shows_db"
mongo = PyMongo(app)

#connect to collection
tv_shows = mongo.db.tv_shows

#INSERT
@app.route("/insert")
def insert():
    # insert new records

    # Community
    post_data= {'name':'Community',
                'seasons':6,
                'duration':'24 minutes',
                'year':2009,
                'date_added':datetime.datetime.utcnow()}
    # insert this record
    tv_shows.insert_one(post_data)

    # Explained
    post_data= {'name':'Explained',
                'seasons':3,
                'duration':'15 minutes',
                'year':2018,
                'date_added':datetime.datetime.utcnow()}
    # insert this record
    tv_shows.insert_one(post_data)

    # confirmation that entries were created
    return 'entries created'

#UPDATE
@app.route("/update")
def update():
    # The item we want to update
    item = {'name': 'My Life is Murder'}
    # The new value we want to set
    updated_values = { "$set": { 'seasons': 7 } }
    # make the update
    tv_shows.update_one(item, updated_values)
    # confirmation that we updated the value
    return 'entry updated'

#DELETE
@app.route("/delete")
def delete():
    # Delete the original record
    tv_shows.delete_one({'name': 'My Life is Murder'})
    # confirm we deleted it
    return 'entry deleted'

#READ ALL
@app.route("/")
def all():
    #find all items in db and save to a variable
    all_shows = list(tv_shows.find())
    # Display current data base to see results
    return render_template('index.html', data=all_shows)



if __name__ == "__main__":
    app.run(debug=True)