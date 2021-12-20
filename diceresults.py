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
testlist = totalresults(1,3,5)
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

results = totals(2,3,2)
#df = pd.DataFrame(results)
#print(df)

print(''+str(results)    )
test = dict(results)
print(str(test))






