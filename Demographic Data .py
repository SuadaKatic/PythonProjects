#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 
from scipy import stats
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings 
warnings. filterwarnings ('ignore')
plt.rcParams['figure.figsize'] = 8,4


# In[2]:


stats = pd.read_csv(r'C:\\Users\\suada\\Downloads\\P4-Demographic-Data.csv')


# In[3]:


stats.head()


# In[5]:


stats.columns


# In[6]:


len(stats.columns)


# In[9]:


stats.head(10)


# In[11]:


stats.tail()


# In[14]:


#stats.info()


# In[13]:


stats.describe()


# In[16]:


#Renaming columns in data set 
stats.columns=['CountryName','CountryCode','BirthRate',               'InternetUsers','IncomeGroup']


# In[17]:


stats.head()


# In[18]:


#subsetting rows and columns 

stats[21:35]


# In[19]:


stats[: : 25]


# In[20]:


stats[: : -1]


# In[24]:


stats[['CountryName','BirthRate']].head()


# In[29]:


#Combining rows and columns 
stats[20:50][['CountryName','BirthRate','InternetUsers']].head()


# In[30]:


result = stats.BirthRate/stats.InternetUsers


# In[32]:


result.head()


# In[33]:


stats['MyCalc']=stats.BirthRate/stats.InternetUsers


# In[34]:


stats.head()


# In[36]:


stats=stats.drop('MyCalc',axis=1)


# In[37]:


stats.head()


# In[50]:


Filter1=stats.InternetUsers<5


# In[51]:


stats[Filter1]


# In[52]:


Filter2=stats.BirthRate>30


# In[53]:


stats[Filter2]


# In[54]:


stats[(stats.BirthRate>30)&(stats.InternetUsers<5)]


# In[57]:


stats[stats.IncomeGroup=='High income']


# In[58]:


stats[stats.CountryName=='Bosnia and Herzegovina']


# In[65]:


vis1=sns.distplot(stats['InternetUsers'],bins=20)


# In[76]:


vis1=sns.distplot(stats['BirthRate'],bins=20)


# In[66]:


vis2=sns.boxplot(data=stats, x='IncomeGroup',y='BirthRate')


# In[68]:


vis3=sns.lmplot(data=stats,x='InternetUsers',y='BirthRate',fit_reg=False)


# In[74]:


vis3 = sns.lmplot(x='InternetUsers',y= 'BirthRate',data=stats,                   fit_reg = False,hue = 'IncomeGroup',                  scatter_kws={"s":50},aspect=1)

      


# In[ ]:




