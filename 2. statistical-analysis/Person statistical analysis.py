#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np


# In[11]:


df = pd.read_csv('employee_stat.csv', index_col=0)


# #### Descriptive

# In[12]:


df.describe()

# we can use include='all'


# #### Numerical

# In[13]:



df['salary'].describe().astype(int)


# #### Categorical

# In[14]:




df['country'].describe()


# In[15]:


# we can break down descriptive statistics functions 
# there are some other functions like ...sum, cumsum, abs etc

print('Standard Deviation: ', df['salary'].std())
print('Average of Balance: ', df['balance'].mean())
print('0.50 Quartile: ', df['salary'].quantile(q=0.50))


# #### The mode is the value that appears most often in a set of data values. 
# #### mode() - mostly used for categorical data.
# #### together (mean, median and mode) called central tendency.  

# In[16]:


print('Salary Mode:', df['salary'].mode())
print('Balance Mode:', df['balance'].mode())


# In[ ]:





# ### SAMPLE  is a small representative things who can represent main dataset.  It saves time, boosts the performance of the model, and improves visualization.

# In[17]:


sample = df.sample(frac=0.25)
sample.info()


# In[ ]:





# In[ ]:





# In[ ]:





# In[10]:





# In[ ]:




