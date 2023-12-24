#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd #import pandas
import numpy as np # import numpy


# In[4]:


#create a data feame by using the dictionary
df=pd.DataFrame({'Math':[78,85,96,80,86],'English':[84,94,89,83,86],'Hindi':[86,97,96,72,83]}) 
print(df) # print the data frame


# In[6]:


# takimg the hole data by using the different dictionary
exam_data={'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
           'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
          'attempts':[1,3,2,3,2,3,1,1,2,1],
          'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']}
Labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(exam_data,index=Labels) # set the data frame and set the labels as index and store it in df. 
print(df) # print the hole data frame. 


# In[ ]:




