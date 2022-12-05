# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

# Create connection to MongoDB
#Method Found at http://carrefax.com/new-blog/2017/6/30/insert-a-dictionary-into-mongodb

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

#Create the scrape route
@app.route('/scrape')
def mongo_insert():
    mars_listings = mongo.db.mars_collection
    mars_data = scrape()
    mars_listings.update({}, mars_data, upsert=True)
    return redirect("/")

#Create the index route
@app.route('/')
def index():
    mars_listings1 = mongo.db.mars_collection.find_one()
    if mars_listings1 == None:
        mars_listings1 = {'title':'not yet scraped', 'paragraph':'not yet scraped', 'featured_image':'not yet scraped', 
                    'mars_tweet':'not yet scraped', 'mars_facts':'not yet scraped', 'mars_images':'not yet scraped'}
    print(f"Show: {type(mars_listings1)}")
    return render_template('index.html', mars_listings1=mars_listings1)

if __name__ == "__main__":
    app.run(debug=True)