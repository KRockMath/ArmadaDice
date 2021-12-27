# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:01:17 2021

@author: KRockMAth
Source: https://starwars-armada.fandom.com/wiki/Dice
"""

#import random
import numpy as np
import pandas as pd
#%%

def eightsided():
    return np.random.randint(8)

#eightsided()
#result = eightsided()

#%%
def bluedie(x):
    if x <= 4:
        return 'hit'
    elif x <= 6:
        return 'crit'
    else:
        return 'accr'

#blueresult = bluedie( eightsided() )
#print(blueresult)

#%%
def reddie(x):
    if x <= 2:
        return 'hit'
    elif x <= 4:
        return 'crit'
    elif x <= 5:
        return 'accr'
    elif x <= 6:
        return '2hits'
    else:
        return 'blnk'

#redresult = reddie( eightsided() )
#print(redresult)

#%%
def blackdie(x):
    if x <= 4:
        return 'hit'
    elif x <= 6:
        return 'hitcrit'
    else:
        return 'blnk'

#blackresult = blackdie( eightsided() )
#print(blackresult)

#%%
def fullresults(blues,reds,blacks):
    blueresults = []
    redresults = []
    blackresults = []
    i=1
    while i <= blues:
        blueresults.append( bluedie(eightsided()) )
        i = i+1

    i=1
    while i <= reds:
        redresults.append( reddie(eightsided()) )
        i = i+1

    i=1
    while i <= blacks:
        blackresults.append( blackdie(eightsided()) )
        i = i+1

#    list2 = ['Blues:',blueresults]+["Reds",redresults]+['Blacks:',blackresults]
    list2 = [['Blues',blueresults],["Reds",redresults],['Blacks',blackresults]]
    return list2
#%%  usage examples in Python:
#bydie = dict(fullresults(4,4,6))

#print(bydie.keys())
#print(bydie['Blues'])
#print(bydie['Reds'])
#print(bydie['Blacks'])
#print(bydie['Blues'][1])

def htmlrender(DiceResults):
    bluelist = DiceResults['Blues']
    redlist = DiceResults['Reds']
    blackslist = DiceResults['Blacks']
    htmlstring = ''
    tempstring = ''
    for x in bluelist:
        #print(x)
        if x == 'hit':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/bluehit.png">'
        elif x == 'crit':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/bluecrit.png">'
        elif x == 'accr':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/blueaccr.png">'
        htmlstring = htmlstring+ str(tempstring) + ' '
    #return htmlstring

    htmlstring = htmlstring+ "\n <br>"
    tempstring = ''

    for x in redlist:
        #print(x)
        if x == 'hit':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/redhit.png">'
        elif x == 'crit':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/redcrit.png">'
        elif x == 'accr':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/redaccr.png">'
        elif x == '2hits':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/red2hits.png">'
        elif x == 'blnk':
            tempstring = '<img src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/redblank.png">'
        htmlstring = htmlstring+ str(tempstring) + ' '

    htmlstring = htmlstring+ "\n <br>"
    tempstring = ''

    for x in blackslist:
        #print(x)
        if x == 'hit':
            tempstring = '<img style="display: inline; margin: 0 5px;" src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/blackhit.png">'
        elif x == 'hitcrit':
            tempstring = '<img style="display: inline; margin: 0 5px;" src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/blackhitcrit.png">'
        elif x == 'blnk':
            tempstring = '<img style="display: inline; margin: 0 5px;" src="https://www.pythonanywhere.com/user/ArmadaDice/files/home/ArmadaDice/mysite/assets/blackblank.png">'

        htmlstring = htmlstring+ str(tempstring) + ' '

    return str(htmlstring)

#test = htmlrender(bydie)
#print(test)

#%%
def totalresults(blues,reds,blacks):
    bluelist = []
    redlist = []
    blacklist = []
    i=1
    while i <= blues:
        bluelist.append( bluedie(eightsided()) )
        i = i+1

    i=1
    while i <= reds:
        redlist.append( reddie(eightsided()) )
        i = i+1

    i=1
    while i <= blacks:
        blacklist.append( blackdie(eightsided()) )
        i = i+1

    return (bluelist+redlist+blacklist)
#%%
#testlist = []
#testlist = totalresults(1,3,5)
#%%

def totals(blu,red,blk):
    testlist = totalresults(blu,red,blk)
    totalhits = testlist.count('hit')+2*testlist.count('2hits')+testlist.count('hitcrit')
    totalcrits = testlist.count('crit')+testlist.count('hitcrit')
    totalblanks = testlist.count('blnk')
    totalaccuracy = testlist.count('accr')

    blargh = []
    blargh.append(['Hits',totalhits])
    blargh.append(['Crits',totalcrits])
    blargh.append(['Blanks',totalblanks])
    blargh.append(['Accuracy',totalaccuracy])

    return blargh

#%%
#testing
#results = totals(2,3,2)
#df = pd.DataFrame(results)
#print(df)

#print(''+str(results)    )
#test = dict(results)
#print(str(test))






