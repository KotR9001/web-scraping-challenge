# In[54]:
from IPython import get_ipython

#Create the Function for Converting the File
def scrape():
    file = get_ipython().getoutput('jupyter nbconvert --to python mission_to_mars.ipynb --output scrape_mars.py')
    mars_dictionary = {'title':title, 'paragraph':paragraph, 'featured_image':featured_image_url, 
                       'mars_tweet':mars_weather, 'mars_facts':mars_table, 'mars_images':mars_list}
    return file, mars_dictionary

#Convert the File
scrape()


# In[ ]:

# import necessary libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo

# Create connection to MongoDB
#Method Found at http://carrefax.com/new-blog/2017/6/30/insert-a-dictionary-into-mongodb

# create instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

#Create the scrape route
@app.route('/scrape')
def mongo_insert():
    scrape()
    return db.mars_collection.insert(scrape())

#Create the index route
@app.route('/')
def index():
    mars_data = db.mars_collection.find()
    return render_template('index.html', mars_data=mars_data)

if __name__ == "__main__":
    app.run(debug=True)