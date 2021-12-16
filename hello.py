# -*- coding: utf-8 -*-
"""
Created 2021-12-15

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
