#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


df = pd.read_csv('employee_filter.csv', index_col=0)


# In[ ]:





# In[8]:


# percentage of gender

round(df['gender'].value_counts()/df['gender'].count()*100,2)


# In[9]:


# percentage of country

round(df['country'].value_counts()/df['country'].count()*100,2)


# In[10]:


# Find Sheryl Itzakson

df[df['full_name'].str.contains('Sheryl Itzakson')]


# In[11]:


# Find female employee who is working with amazon and from poland

df[(df.gender.str.contains('F')) & (df.country.str.contains('Poland')) & (df.company.str.contains('Amazon'))]


# In[ ]:





# In[13]:


# Find paula tulley's country, job and company

df[df['full_name'].str.contains('Paula Tulley', case=True)][['full_name','country','job_title','company']]


# In[14]:


# I just want to paula's university name

df[df['full_name'].str.contains('Paula Tulley')]['university']


# In[ ]:





# In[ ]:





# In[15]:


# Find a project manager who must be older than 30 

df[(df['job_title']=='Project Manager') & (df.age >= 30)]


# In[16]:


# How many specialist are in this dataset ?

len(df[df['job_title'].str.contains('Specialist')])


# In[17]:


# Highest paid specialist

df[df['job_title'].str.contains('Specialist')].sort_values(by='salary', ascending=False).head(5)


# In[18]:


# find scientist

len(df[df.job_title.str.contains('Scientist')])


# In[19]:


# find software related

len(df[df.job_title.str.contains('Software')])


# In[20]:


# Find analyst

len(df[df.job_title.str.contains('Analyst')])


# In[21]:


# Find who working with data

len(df[df.job_title.str.contains('Data')])


# In[22]:


# Find who working with database

len(df[df.job_title.str.contains('Database')])


# In[23]:


# find engineer's

len(df[df.job_title.str.contains('Engineer')])


# In[24]:


# find professor's

len(df[df.job_title.str.contains('Professor')])


# In[39]:


# find project manager 

len(df[df.job_title.str.contains('Project Manager')])


# In[ ]:





# In[25]:


# Find the person who get highest salary. Find his name, salary, company and country

df[df['salary'].max()==df['salary']][['full_name','salary','company','country']]


# In[27]:


# How many people's have salary and balance more than 50000

len(df[(df['salary']>50000) & (df['balance']>50000)])


# In[ ]:





# In[ ]:





# In[28]:


# Count Google employee from every country 

df[df['company']=='Google']['country'].value_counts()


# In[29]:


# How many people from each country are working in the giant (Google,Apple etc) company?

df[(df['company']=='Google') + (df['company']=='Amazon') + (df['company']=='Apple') +
  (df['company']=='Microsoft') + (df['company']=='Facebook')]['country'].value_counts()


# In[ ]:





# In[ ]:





# In[30]:


# Find 5 person visa credit-card user who get the minimum salary

df[df['credit_card']=='visa'].sort_values(by='salary').head(5)


# In[31]:


# How many people use mastercard

df['credit_card'].value_counts()['mastercard']


# In[32]:


# get group visa

df.groupby('credit_card').get_group('visa')


# In[33]:


# How many people's use every credit_card in poland

df.query("country=='Poland'")['credit_card'].value_counts()


# In[34]:


# How many visa credit cards does each country use?

df.groupby('credit_card').get_group('visa')['country'].value_counts()


# In[35]:


# if you want to be more specific

df.groupby('credit_card').get_group('visa')['country'].value_counts()['Bangladesh']


# In[ ]:





# In[ ]:





# In[36]:


# Find the person whose name length is bigger than anyone

def get_max_len(lst):
    return max(enumerate(lst), key=lambda x: len(x[1]))

print(get_max_len(df['full_name']))


# In[37]:


df[df['full_name']=='Merrill Le Breton De La Vieuville']


# In[38]:


# Another way to find this 

df[df.full_name.apply(lambda x: len(x) > 30)]


# In[ ]:





# In[ ]:





# In[ ]:




