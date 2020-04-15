#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from flask import Flask, render_template
import pandas as pd
import requests
import pymongo


# In[2]:


###Scrape the Latest News Title and Paragraph from the NASA Mars News Site
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

#Create the Response
response = requests.get(url)

#Create the BeautifulSoup Object
soup = bs(response.text, 'html.parser')
print(soup.prettify)


# In[3]:


#Return Code for All News Titles & Paragraphs
titles = soup.find_all('div', class_='content_title')
#Method to Return All Matching Elements Found at https://stackoverflow.com/questions/30147223/beautiful-soup-findall-multiple-class-using-one-query
paragraphs = soup.select('.grid_layout')[1].find_all('div', class_='rollover_description_inner')

#Error Handling
try:
    title = titles[0].text
    paragraph = paragraphs[0].text

    #Check to See if there is a News Article
    if (title and paragraph):
        print(title)
        print(paragraph)

#Error Response
except:
    print("Error: Article Not Found")


# In[4]:


###Scrape the Featured Mars Image from the NASA Mars News Site

#Create URL for the Space Images Site
url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

#Create the Path
executable_path = {'executable_path': 'chromedriver.exe'}
browser1 = Browser('chrome', **executable_path, headless=False)

#Visit the Website
browser1.visit(url1)


# In[5]:


#Display the Code
html1 = browser1.html
soup1 = bs(html1, 'html.parser')
print(soup1.prettify())


# In[6]:


#Return the Featured Image
try:
    image_extension = soup1.body.find_all('a', class_='fancybox')[1]['data-fancybox-href']
    featured_image_url = url1 + image_extension
    print(featured_image_url)
except:
    print('Error: The featured Mars image could not be found.')

#Close the Browser
#Method Found at https://splinter.readthedocs.io/en/latest/browser.html
window1 = browser1.windows[0]
try:
    window1.close()
except:
    print("The window is closed.")


# In[19]:


###Scrape the Latest Mars Weather Tweet from the Twitter Webpage

#Import Selenium to Handle Dynamically Loaded Page
#Found Method at https://stackoverflow.com/questions/56746181/why-python-output-doesnt-match-html-for-target-website
#Found Method to Construct Driver at https://stackoverflow.com/questions/45499517/beautifulsoup-parser-cant-access-html-elements
#Found Method to Enable BeautifulSoup to Interact with Driver at https://github.com/SeleniumHQ/selenium/issues/5998
from selenium import webdriver

#Create the URL
url2 = 'https://twitter.com/marswxreport?lang=en'

#Create the Driver
#Found Method to Get Driver to Work at https://github.com/SeleniumHQ/selenium/issues/5998
options = webdriver.ChromeOptions() 
options.add_argument('--headless')
driver = webdriver.Chrome('C:/Users/bjros/OneDrive/Desktop/KU_Data_Analytics_Boot_Camp/Homework Assignments/Homework Week 12/web-scraping-challenge/Missions_to_Mars/chromedriver.exe')

#Get the URL
driver.get(url2)


# In[20]:


#Utilize Page Source
html2 = driver.page_source

#Create the BeautifulSoup Object
soup2 = bs(html2, 'html.parser')
print(soup2.prettify())


# In[21]:


#Import Module to Allow Compilement
#Method Found at https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import re

#Return the Latest Weather Tweet
#Learned About Compiling from https://stackoverflow.com/questions/38395751/python-beautiful-soup-find-string-and-extract-following-string
try:
    mars_weather = soup2.find_all(re.compile('span'), class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0', string=re.compile('^InSight'))[0].text
    print(mars_weather)
except:
    print('Error: The latest Mars weather tweet could not be found.')


# In[22]:


#Close the Mars Tweet Twitter Webpage
driver.close()


# In[11]:


###Put the Mars Facts in a Table

#Create URL
url3 = 'https://space-facts.com/mars/'

#Read HTML to Create Table
tables = pd.read_html(url3)
mars_table = tables[0]
mars_table = mars_table.rename(columns={mars_table.columns[0]:'Description', mars_table.columns[1]:'Value'})
mars_table = mars_table.set_index('Description')
mars_table


# In[12]:


###Scrape the USGS Astrogeology Site for High-Resolution Images of Mar's Hemispheres

#Create the URLs
url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
url5 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
url6 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
url7 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

#Return the Responses
cerberus_response = requests.get(url4)
schiaparelli_response = requests.get(url5)
syrtis_response = requests.get(url6)
valles_response = requests.get(url7)

#Create the BeautifulSoup Object
soup4 = bs(cerberus_response.text, 'html.parser')
print(soup4.prettify)
print('-'*100)
print('-'*100)
print('-'*100)
soup5 = bs(schiaparelli_response.text, 'html.parser')
print(soup5.prettify)
print('-'*100)
print('-'*100)
print('-'*100)
soup6 = bs(syrtis_response.text, 'html.parser')
print(soup6.prettify)
print('-'*100)
print('-'*100)
print('-'*100)
soup7 = bs(valles_response.text, 'html.parser')
print(soup7.prettify)
print('-'*100)
print('-'*100)
print('-'*100)


# In[13]:


#Pull the Image Files & Titles

#Cerberus
cerberus_image = soup4.find_all('div', class_='downloads')[0].li.a['href']
print(cerberus_image)
cerberus_title = soup4.find_all('h2', class_='title')[0].text
print(cerberus_title)

#Schiaparelli
schiaparelli_image = soup5.find_all('div', class_='downloads')[0].li.a['href']
print(schiaparelli_image)
schiaparelli_title = soup5.find_all('h2', class_='title')[0].text
print(schiaparelli_title)

#Syrtis
syrtis_image = soup6.find_all('div', class_='downloads')[0].li.a['href']
print(syrtis_image)
syrtis_title = soup6.find_all('h2', class_='title')[0].text
print(syrtis_title)

#Valles
valles_image = soup7.find_all('div', class_='downloads')[0].li.a['href']
print(valles_image)
valles_title = soup7.find_all('h2', class_='title')[0].text
print(valles_title)

#Create List of Dictionaries
mars_list = [{'title1':cerberus_title, 'img_url1':cerberus_image}, {'title2':schiaparelli_title, 'img_url2':schiaparelli_image},
            {'title3':syrtis_title, 'img_url3':syrtis_image}, {'title4':valles_title, 'img_url4':valles_image}]
mars_list


# In[23]:


#Create the Dictionary
mars_dictionary = {'title':title, 'paragraph':paragraph, 'featured_image':featured_image_url, 
                'mars_tweet':mars_weather, 'mars_facts':mars_table, 'mars_images':mars_list}


# In[ ]:




