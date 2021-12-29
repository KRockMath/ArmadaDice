# -*- coding: utf-8 -*-
"""
Created 2021-12-15

@author: KrockMath

https://pythonspot.com/flask-web-app-with-python/
https://www.askpython.com/python-modules/flask/flask-forms
need to host here: https://docs.github.com/en/pages
"""


#mostly to just run better on my machine to import diceresults, remove from final push
import os
cwd = os.getcwd() + str('\\OtherGithub\\ArmadaDice\\')
print(cwd)

import sys
sys.path.append(cwd)
#%%
#render_template and jsonify not used ATM
from flask import Flask,render_template,request
import diceresults as dr
import pandas as pd
#%%
app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
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
def makehtml(BlueDice,RedDice,BlackDice):
    oneresult = dr.fullresults(BlueDice,RedDice,BlackDice)

    info = "post results: blue:"+str(BlueDice)+" red:"+str(RedDice)+" black:"+str(BlackDice)+"<br>JSON Object:"

    cssstyle = '''<style>
               #client_logos {
                display: inline-block;
                width:100%;
                }
              </style>
    '''
    header = "<html> "+cssstyle + '''<head>
     <title>Star Wars Armada Dice Calculator</title>
    </head>
<form action="http://armadadice.pythonanywhere.com/">
    <input type="submit" value="Back to Start" />
</form>
    '''
    finalresult = header+info+'<br>'  + str(dict(oneresult)) +'<br>'+ dr.htmlrender( dict(oneresult)  ) + '\n </html>'
    return finalresult

#%%
@app.route('/action_to_perform_after_submission',methods = ['GET','POST'])
#helpful: https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
def action_to_perform_after_submission():
    if request.method == 'GET':
        return 'get result'
    if request.method == 'POST':
        #results = dr.totals(2,3,2)
        BlueDice = int(request.form['BlueDice'])
        RedDice = int(request.form['RedDice'])
        BlackDice = int(request.form['BlackDice'])
        finalresult = makehtml(BlueDice,RedDice,BlackDice)
        print(finalresult)
        return finalresult

        #return f"post result: "+str(jsonify(results)) #didn't show results as a string. just put post resutls


#%%
if __name__ == "__main__":
    app.debug = False  #False True remove this from final
    app.run(port=8000)





#+ s str( dr.htmlrender( dict( dr.fullresults(2,2,5) ) )) )
#fullresults(3,3,6)


