# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:44:57 2021

@author: KrockMath

https://pythonspot.com/flask-web-app-with-python/
"""

#Flask Tutorial

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=8000)
