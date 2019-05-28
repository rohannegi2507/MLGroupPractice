# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:41:11 2019

@author: Nikita
"""
import pandas as pd
#create a data frame - dictionary is used here where keys get converted to column names and values to row values.
data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                    'Rank':[121,40,100,130,11]})
print(data)

## to describe the data
data.describe()
print(data.describe())

print(data.info())

#now , work on sorting 
data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data.sort_values(by=['ounces'],ascending=True,inplace=False)
##inplace = True will make changes to the data
## multiple column sort 
data.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False)

## to remove the duplicates 
data.drop_duplicates()

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)