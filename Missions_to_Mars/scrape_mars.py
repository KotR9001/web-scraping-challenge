#!/usr/bin/env python
# coding: utf-8

#Convert Jupyter Notebook into Python Script

#Import Dependencies
#Method Found at https://medium.com/@researchplex/the-easiest-way-to-convert-jupyter-ipynb-to-python-py-912e39f16917
# and https://ipython.org/ipython-doc/rel-0.10.2/html/interactive/extension_api.html
import nbconvert
import IPython
from IPython import get_ipython
import mission_to_mars

#Create the Function for Converting the File
def scrape():
    exec(open(mission_to_mars).read())
    return mars_dictionary