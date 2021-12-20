# -*- coding: utf-8 -*-
"""
Created 2021-12-15

@author: KrockMath

https://pythonspot.com/flask-web-app-with-python/
https://www.askpython.com/python-modules/flask/flask-forms
"""

#Flask Tutorial

from flask import Flask,render_template,request
from flask import jsonify
import diceresults as dr
import pandas as pd
#%%
app = Flask(__name__)

@app.route("/",methods = ['GET'])
def main():
    return '''Welcome to Star Wars Armada Dice Calculator
    <br>
    <form action="action_to_perform_after_submission" method = "POST">
        <p>Blue Dice <input type = "text" name = "BlueDice" /></p>
        <p>Red Dice <input type = "text" name = "RedDice" /></p>
        <p>Black Dice <input type = "text" name = "BlackDice" /></p>
        <p><input type = "submit" value = "submit" /></p>
    </form>
     '''

#%%
@app.route('/action_to_perform_after_submission',methods = ['GET','POST'])

#helpful: https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
def action_to_perform_after_submission():
    if request.method == 'GET':
        return f"get result"
    if request.method == 'POST':
        #results = dr.totals(2,3,2)
        BlueDice = int(request.form['BlueDice'])
        RedDice = int(request.form['RedDice'])
        BlackDice = int(request.form['BlackDice'])
        info = "post results: blue:"+str(BlueDice)+" red:"+str(RedDice)+" black:"+str(BlackDice)+"<br>JSON Object:"
        fullresults = dr.totals(BlueDice,RedDice,BlackDice)
        return info+'<br>' + str(dict(fullresults))

        #return f"post result: "+str(jsonify(results)) #didn't show results as a string. just put post resutls


#%%
if __name__ == "__main__":
    app.debug = False  #False True remove this from final
    app.run(port=8000)

