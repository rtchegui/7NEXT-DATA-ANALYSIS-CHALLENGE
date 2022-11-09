#!/usr/bin/env python
# coding: utf-8

# In[1]:


## #importing libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


#loading and check data data
store_dataset=pd.read_csv('C:\\Users\\User\\Documents\\data_analysis_challenge_data.csv')


# In[3]:


print(type(store_dataset))


# In[4]:


store_dataset.info()


# In[5]:


print(store_dataset.shape)


# In[6]:


print(store_dataset.shape[0])


# In[7]:


print(store_dataset.shape[1])


# In[8]:


store_dataset.head()


# In[9]:


#Data overview
print(f"Rows     : {store_dataset.shape[0]}")
print(f"Columns  : {store_dataset.shape[1]}" ,)
print()


# In[10]:


# Print the column names
print(f"Features : {store_dataset.columns.tolist()}")
print()


# In[11]:


# Print the total number of null values in the data
print(f"Missing values :  {store_dataset.isnull().sum().values.sum()}")


# In[12]:


# For each column, print the number of unique values
print(f"Unique values :  {store_dataset.nunique()}")


# In[13]:


#Descriptive statistics for continuous variables 
store_dataset.describe().T 


# In[14]:


#correlation
corr = store_dataset.corr()
print(type(corr))
print(corr)


# In[15]:


store_new=store_dataset


# In[16]:


print(store_new)


# In[17]:


##  Sales by store – Calculate the total sales amount made by each store over the 
##   entire three months and visualize with a plot of your choice.

store_new1=store_new[['STORECODE', 'VALUE']]


# In[18]:


store_new1=store_new1.groupby('STORECODE').sum('VALUE')


# In[19]:


print(store_new1)


# In[20]:


store_new1.plot.bar()


# In[21]:


## 2.	Sales by category – For each store, find the category of products that’s sold the most (qty) a
##  nd visualize with a plot of 

store_new1=store_new[store_new["STORECODE"]=='N1']


# In[22]:


## For the first Store 

store_new2=store_new1[['GRP', 'QTY']]


# In[23]:


store_new2=store_new2.groupby('GRP').sum('QTY')


# In[24]:


print(store_new2)


# In[25]:


store_new2.sort_values(by=['QTY'],inplace=True,ascending=False)
df=store_new2.head()


# In[26]:


df.plot.bar()


# In[27]:


## For store N2 

store_N2=store_new[store_new["STORECODE"]=='N2']
store_N2=store_N2[['GRP', 'QTY']]
store_N2=store_N2.groupby('GRP').sum('QTY')
print(store_N2)
store_N2.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N2.head())
store_N2.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N2=store_N2.head()
df_N2.plot.bar()


# In[28]:


## For store N3

store_N3=store_new[store_new["STORECODE"]=='N3']
store_N3=store_N3[['GRP', 'QTY']]
store_N3=store_N3.groupby('GRP').sum('QTY')
print(store_N3)
store_N3.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N3.head())
store_N3.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N3=store_N3.head()
df_N3.plot.bar()


# In[29]:


## For store N4 

store_N4=store_new[store_new["STORECODE"]=='N4']
store_N4=store_N4[['GRP', 'QTY']]
store_N4=store_N4.groupby('GRP').sum('QTY')
print(store_N4)
store_N4.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N4.head())
store_N4.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N4=store_N4.head()
df_N4.plot.bar()


# In[30]:


## For Store N5 

store_N5=store_new[store_new["STORECODE"]=='N5']
store_N5=store_N5[['GRP', 'QTY']]
store_N5=store_N5.groupby('GRP').sum('QTY')
print(store_N5)
store_N5.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N5.head())
store_N5.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N5=store_N5.head()
df_N5.plot.bar()


# In[31]:


## For Store N6 

store_N6=store_new[store_new["STORECODE"]=='N6']
store_N6=store_N6[['GRP', 'QTY']]
store_N6=store_N6.groupby('GRP').sum('QTY')
print(store_N6)
store_N6.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N6.head())
store_N6.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N6=store_N6.head()
df_N6.plot.bar()


# In[32]:


## For Store N7 

store_N7=store_new[store_new["STORECODE"]=='N7']
store_N7=store_N7[['GRP', 'QTY']]
store_N7=store_N7.groupby('GRP').sum('QTY')
print(store_N7)
store_N7.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N7.head())
store_N7.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N7=store_N7.head()
df_N7.plot.bar()


# In[33]:


## For Store N8
store_N8=store_new[store_new["STORECODE"]=='N8']
store_N8=store_N8[['GRP', 'QTY']]
store_N8=store_N8.groupby('GRP').sum('QTY')
print(store_N8)
store_N8.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N8.head())
store_N8.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N8=store_N8.head()
df_N8.plot.bar()


# In[34]:


## For Store N9 

store_N9=store_new[store_new["STORECODE"]=='N9']
store_N9=store_N9[['GRP', 'QTY']]
store_N9=store_N9.groupby('GRP').sum('QTY')
print(store_N9)
store_N9.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N9.head())
store_N9.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N9=store_N9.head()
df_N9.plot.bar()


# In[35]:


## For Store N10 

store_N10=store_new[store_new["STORECODE"]=='N10']
store_N10=store_N10[['GRP', 'QTY']]
store_N10=store_N10.groupby('GRP').sum('QTY')
print(store_N10)
store_N10.sort_values(by=['QTY'],inplace=True,ascending=False)
print(store_N10.head())
store_N10.sort_values(by=['QTY'],inplace=True,ascending=False)
df_N10=store_N10.head()
df_N10.plot.bar()


# In[36]:


## 3.	Sales by day – For each store, find the day across all three months where the total sales amount is the highest. In other words, find the best day for each store in 
## terms of sales amount and visualize with a plot of your choice.

store_N1_day=store_new[store_new["STORECODE"]=='N1']
store_N1_day=store_N1_day[['DAY', 'VALUE']]
store_N1_day=store_N1_day.groupby('DAY').sum('VALUE')
print(store_N1_day)
store_N1_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N1_day.head())
store_N1_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N1_day=store_N1_day.head()
df_N1_day.plot.bar()


# In[37]:


## For every Store 

store_N2_day=store_new[store_new["STORECODE"]=='N2']
store_N2_day=store_N2_day[['DAY', 'VALUE']]
store_N2_day=store_N2_day.groupby('DAY').sum('VALUE')
print(store_N2_day)
store_N2_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N2_day.head())
store_N2_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N2_day=store_N2_day.head()
df_N2_day.plot.bar()

store_N3_day=store_new[store_new["STORECODE"]=='N3']
store_N3_day=store_N3_day[['DAY', 'VALUE']]
store_N3_day=store_N3_day.groupby('DAY').sum('VALUE')
print(store_N3_day)
store_N3_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N3_day.head())
store_N3_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N3_day=store_N3_day.head()
df_N3_day.plot.bar()


store_N4_day=store_new[store_new["STORECODE"]=='N4']
store_N4_day=store_N4_day[['DAY', 'VALUE']]
store_N4_day=store_N4_day.groupby('DAY').sum('VALUE')
print(store_N4_day)
store_N4_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N4_day.head())
store_N4_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N4_day=store_N4_day.head()
df_N4_day.plot.bar()

store_N5_day=store_new[store_new["STORECODE"]=='N5']
store_N5_day=store_N5_day[['DAY', 'VALUE']]
store_N5_day=store_N5_day.groupby('DAY').sum('VALUE')
print(store_N5_day)
store_N5_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N5_day.head())
store_N5_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N5_day=store_N5_day.head()
df_N5_day.plot.bar()


store_N6_day=store_new[store_new["STORECODE"]=='N6']
store_N6_day=store_N6_day[['DAY', 'VALUE']]
store_N6_day=store_N6_day.groupby('DAY').sum('VALUE')
print(store_N6_day)
store_N6_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N6_day.head())
store_N6_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N6_day=store_N6_day.head()
df_N6_day.plot.bar()

store_N7_day=store_new[store_new["STORECODE"]=='N7']
store_N7_day=store_N7_day[['DAY', 'VALUE']]
store_N7_day=store_N7_day.groupby('DAY').sum('VALUE')
print(store_N7_day)
store_N7_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N7_day.head())
store_N7_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N7_day=store_N7_day.head()
df_N7_day.plot.bar()


store_N8_day=store_new[store_new["STORECODE"]=='N8']
store_N8_day=store_N8_day[['DAY', 'VALUE']]
store_N8_day=store_N8_day.groupby('DAY').sum('VALUE')
print(store_N8_day)
store_N8_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N8_day.head())
store_N8_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N8_day=store_N8_day.head()
df_N8_day.plot.bar()

store_N9_day=store_new[store_new["STORECODE"]=='N9']
store_N9_day=store_N9_day[['DAY', 'VALUE']]
store_N9_day=store_N9_day.groupby('DAY').sum('VALUE')
print(store_N9_day)
store_N9_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N9_day.head())
store_N9_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N9_day=store_N9_day.head()
df_N9_day.plot.bar()

store_N10_day=store_new[store_new["STORECODE"]=='N10']
store_N10_day=store_N10_day[['DAY', 'VALUE']]
store_N10_day=store_N10_day.groupby('DAY').sum('VALUE')
print(store_N10_day)
store_N10_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
print(store_N10_day.head())
store_N10_day.sort_values(by=['VALUE'],inplace=True,ascending=False)
df_N10_day=store_N10_day.head()
df_N10_day.plot.bar()


# In[38]:


## Bonus:

## Sales by month – Calculate total sales amount across all stores per month to find the best 
## month across the given three months and visualize with a plot of your choice.


store_month=store_new[['MONTH', 'VALUE']]
store_month=store_month.groupby('MONTH').sum('VALUE')
print(store_month)
store_month.plot.bar()


# In[ ]:




