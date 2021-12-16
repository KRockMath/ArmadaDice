# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:28:39 2021

@author: KXE2732
"""

from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html',name=name)

if __name__ == "__main__":
    app.run()