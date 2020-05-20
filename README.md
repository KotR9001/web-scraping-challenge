# web-scraping-challenge
Mars Rendering


A project was carried out to render mars facts from various sites onto one central webpage. This endeavor utilized Beautiful Soup, Splinter,
Selenium, and MongoDB.


Data Parsing

-The latest Mars news title and paragraph text were taken from https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

-The latest Mars image was pulled from https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars

-The latest Mars tweet was obtained from https://twitter.com/marswxreport?lang=en

-A table of Mars facts was pulled from https://space-facts.com/mars/

-A series of Mars hemisphere images was taken from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

-All of these items were put in a dictionary and the Jupyter Notebook was converted into a Python file.


Data Rendering

-A Python file was created with a scraping function that would perform all of the data parsing.

-Another Python file was made to call in the scraping function, update a MongoDB database, call that data , and use Render_Template with
Flask to pass it onto the index.html file.

-A button was placed on the local iteration of the website to allow a user to scrape the latest Mars data and pictures from the web.