# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create connection to MongoDB
#Method Found at http://carrefax.com/new-blog/2017/6/30/insert-a-dictionary-into-mongodb

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)


#Create the scrape route
@app.route('/scrape')
def mongo_insert():
    mars_listings = mongo.db.mars_db
    mars_data = scrape_mars.scrape()
    mars_listings.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

#Create the index route
@app.route('/')
def index():
    mars_data = scrape_mars.scrape()
    return render_template('index.html', mars_data=mars_data)

if __name__ == "__main__":
    app.run(debug=True)