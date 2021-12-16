# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:49:09 2021

@author: KrockMath
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return "Member Name: "+str(name)


if __name__ == "__main__":
    app.run()