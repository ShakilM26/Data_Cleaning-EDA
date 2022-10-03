#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


df = pd.read_csv('employee_stat.csv', index_col=0)


# ## Descriptive

# In[6]:


df.describe()

# we can use include='all'


# In[9]:


# numerical 

df['salary'].describe().astype(int)


# In[11]:


# categorical

df['country'].describe()


# In[14]:


# we can break down descriptive statistics functions

print('Standard Deviation: ', df['salary'].std())
print('Average of Balance: ', df['balance'].mean())
print('0.50 Quartile: ', df['salary'].quantile(q=0.50))


# In[16]:


# The mode is the value that appears most often in a set of data values. 
# mode() - mostly used for categorical data.
# together (mean, median and mode) called central tendency. 

print('Salary Mode:', df['salary'].mode())
print('Balance Mode:', df['balance'].mode())


# In[23]:


# there are some other functions like ...sum, cumsum, abs etc


# In[22]:


# sample is a small representative things who can represent main dataset.
# It saves time, boosts the performance of the model, and improves visualization.

sample = df.sample(frac=0.25)
sample.info()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




