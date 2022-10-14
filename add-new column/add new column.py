#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd


# In[42]:


df = pd.read_csv('employee_insight.csv', index_col=0)


# ### new column - age

# In[43]:


df['clean_birthday'] = pd.to_datetime(df['birthday'])
df.head(1)


# In[44]:


df['year'] = df['clean_birthday'].dt.year


# In[45]:


# our desired column employee's age

from datetime import datetime
today = datetime.today().year
df['age'] = today - df['year']
df.head(2)


# In[ ]:





# ### new column - continent

# In[46]:


continent = []

for i in df['country']:
    if i == 'Russia':
        continent.append('Asia')
    elif i == 'Japan':
        continent.append('Asia')
    elif i == 'Thailand':
        continent.append('Asia')
    elif i == 'South Korea':
        continent.append('Asia')
    elif i == 'Bangladesh':
        continent.append('Asia')
    elif i == 'Poland':
        continent.append('Europe')
    elif i == 'Croatia':
        continent.append('Europe')
    elif i == 'Norway':
        continent.append('Europe')
    elif i == 'United Kingdom':
        continent.append('Europe')
    elif i == 'Denmark':
        continent.append('Europe')
    elif i == 'Germany':
        continent.append('Europe')
    elif i == 'Switzerland':
        continent.append('Europe')
    elif i == 'Spain':
        continent.append('Europe')
    elif i == 'United States':
        continent.append('North America')
    elif i == 'Canada':
        continent.append('North America')
    elif i == 'Australia':
        continent.append('Oceania')
    else:
        None


# In[47]:


df['continent'] = continent


# In[48]:


df.head(2)


# In[ ]:





# ### after paying tax 

# In[49]:


# Using this source https://taxsummaries.pwc.com/united-states/individual/taxes-on-personal-income
# Though in my dataset minimum salary are 20030
# I am going to started the operation based on this website


# In[50]:


after_pay_tax = []

for i in df['salary']:
    if i >= 20000 and i <= 41775:
        after_pay_tax.append(i*0.12)
    elif i >=41776 and i <= 89075:
        after_pay_tax.append(i*0.22)
    elif i >= 89076 and i <= 170050:
        after_pay_tax.append(i*0.24)
    else:
        None


# In[51]:


df['income_tax'] = after_pay_tax
df['income_tax'] = df['income_tax'].astype(int)


# In[52]:


df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




