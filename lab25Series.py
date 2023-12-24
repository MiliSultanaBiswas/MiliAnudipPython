#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[23]:


#months of a year
months=['January','February','March','April','May','June','July','August','September','October','November','December']

electricity_usage=[350,320,310,330,340,370,380,360,350,330,320,330] # electricity_usage for every month`` 

gas_usage=[20,18,16,15,12,10,8,9,12,15,17,19] # gas_usage for every month

print("electricity_usage:") # show like heading

# making the series and here index is months and according months their electricity_usage and it store in a variable
a=pd.Series(electricity_usage, index=months)

print(a)#printing the series
print("\n") # it is for a new line gap
print("gas_usage:") # show like heading
# making the series and here index is months and according months their gas_usage and it store in a variable
v=pd.Series(gas_usage, index=months)
print(v)#printing the series


# In[25]:


#months of a year
months=['January','February','March','April','May','June','July','August','September','October','November','December']
revenue=[5000,5200,4800,5400,5600,5800,6100,5900,6200,6500,7000,6900] # revenue for every month
print("revenue foe every month is:")# show like heading
# making the series and here index is months and according months their revenue and it store in a variable
a=pd.Series(revenue, index=months)

print(a)#printing the series


# In[ ]:




