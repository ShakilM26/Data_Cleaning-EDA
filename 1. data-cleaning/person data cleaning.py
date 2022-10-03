#!/usr/bin/env python
# coding: utf-8

# In[176]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[177]:


df = pd.read_csv('employee.csv')


# In[ ]:





# # Data Cleaning

# In[178]:


df.columns[df.isnull().any()]


# In[179]:


col = ['company', 'salary', 'credit_card', 'balance', 'vehicle']
df[col].isnull().sum()

# it's not a good process


# In[180]:


# it's a good way to find actual columns

null = df.columns[df.isnull().any()]
df[null].isnull().sum()


# In[181]:


# percentage of missing values in each col

for col in df.columns:
    missing_percent = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(missing_percent*100)))


# In[182]:


# missing value visualize

cols = df.columns
colors = ['black', 'white']
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colors))


# In[183]:


df.info()


# we can see that there is no numeric columns. But we know salary and balance col is numeric. so we have to make it numeric.

# In[184]:


df[['salary', 'balance']] = df[['salary', 'balance']].replace(r'\$', r'', regex=True)


# In[185]:


df['salary'] = df['salary'].str.replace(',','')
df['balance'] = df['balance'].str.replace(',','')

 
# we have to make sure there is no  comma


# but still our columns is object datatype. so we have to make it numeric first.

# In[186]:


df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df['balance'] = pd.to_numeric(df['balance'], errors='coerce')


#  Here is the thing. we can't make it integer because it's still have nan values

# In[187]:


median_salary = df['salary'].median()
print(median_salary)

median_balance = df['balance'].median()
print(median_balance)


# In[188]:


# using median we fill our missing gap in salary and balance cols

df['salary'] = df['salary'].fillna(median_salary)

df['balance'] = df['balance'].fillna(median_balance)


# In[189]:


# Now we can make it integer column

df['salary']=df['salary'].apply(np.int64)
df['balance']=df['balance'].apply(np.int64)


# In[ ]:





# # Fill text value in Company col

# In[190]:


# I have 60 nan values in this column. 
# I decided to use limits to fill our nan values so that we can use multiple values.
# I have divided these 60 null values into 4 parts.


# In[191]:


df = df.fillna(value={'company':'Google'}, limit=20)


# In[192]:


df=df.fillna(value={'company':'Microsoft'}, limit=10)


# In[193]:


df=df.fillna(value={'company':'Facebook'}, limit=12)


# In[194]:


df=df.fillna(value={'company':'Apple'}, limit=10)


# In[195]:


df=df.fillna(value={'company':'Amazon'}, limit=8)


# In[196]:


# Since here our dataset is generated from fake data generating website. So here are the random company names. 
# So I am replacing some of the familiar names for our convenience.

df = df.replace({'company':{'Browsecat':'Netflix', 'Wikizz': 'Intel', 'Pixoboo':'IBM'}})


# In[197]:


# See !! 

df['company'].value_counts().head(10)


# ## I have filled the null values in the Vehicle column with zeros to keep track of the null values. 
# 
# ## As we have cleaned our salary column. Now we can use our salary column to remove the zeros and set a more accurate value.
# 

# In[198]:


df['vehicle'] = df['vehicle'].fillna('zeroes')


# In[199]:


# I divided the salary column into 4 parts 
# 1. 20 to 35
# 2. 35 to 50 
# 3. 50 to 70
# 4. 70 to 90
# 5. 90 to 110


# ## 20k to 35k

# In[200]:


# checking which car has been used more in this range

df[(df['salary'] < 35000) & (df['salary'] >= 20000)]['vehicle'].value_counts().head(10)


# In[201]:


# Using our desired condition

condi = [(df['salary'] < 35000) & (df['salary'] >= 20000) & (df['vehicle']=='zeroes')]
values = ['Dodge']
df['vehicle'] = np.select(condi, values, default=df['vehicle'])


# In[202]:


# Now check again and BINGO !!

df[(df['salary'] < 35000) & (df['salary'] >= 20000)]['vehicle'].value_counts().head(5)


# ## 35k to 50k

# In[203]:


df[(df['salary'] < 50000) & (df['salary'] >= 35000)]['vehicle'].value_counts().head(10)


# In[204]:


condi = [(df['salary'] < 50000) & (df['salary'] >= 35000) & (df['vehicle']=='zeroes')]
values = ['Ford']
df['vehicle'] = np.select(condi, values, default=df['vehicle'])


# In[205]:


df[(df['salary'] < 50000) & (df['salary'] >= 35000)]['vehicle'].value_counts().head(5)


# ## 50k to 70k

# In[206]:


df[(df['salary'] < 70000) & (df['salary'] >= 50000)]['vehicle'].value_counts().head(10)


# In[207]:


condi = [(df['salary'] < 70000) & (df['salary'] >= 50000) & (df['vehicle']=='zeroes')]
values = ['Ford']
df['vehicle'] = np.select(condi, values, default=df['vehicle'])


# In[208]:


df[(df['salary'] < 70000) & (df['salary'] >= 50000)]['vehicle'].value_counts().head(5)


# ## 70k to 90k

# In[209]:


df[(df['salary'] < 90000) & (df['salary'] >= 70000)]['vehicle'].value_counts().head(10)


# In[210]:


condi = [(df['salary'] < 90000) & (df['salary'] >= 70000) & (df['vehicle']=='zeroes')]
values = ['Chevrolet']
df['vehicle'] = np.select(condi, values, default=df['vehicle'])


# In[211]:


df[(df['salary'] < 90000) & (df['salary'] >= 70000)]['vehicle'].value_counts().head(5)


# ## 90k to 110k

# In[212]:


df[(df['salary'] < 110000) & (df['salary'] >= 90000)]['vehicle'].value_counts().head(10)


# In[213]:


condi = [(df['salary'] < 110000) & (df['salary'] >= 90000) & (df['vehicle']=='zeroes')]
values = ['Volkswagen']
df['vehicle'] = np.select(condi, values, default=df['vehicle'])


# In[214]:


df[(df['salary'] < 110000) & (df['salary'] >= 90000)]['vehicle'].value_counts().head(5)


# ## Now in the same way I will also fill the credit card column

# In[215]:


df['credit_card'] = df['credit_card'].fillna('zeroes')


# In[216]:


df['credit_card'].value_counts()


# In[217]:


df[df['credit_card']=='zeroes'].sort_values(by='salary').head(2)

# actually I checked before I emplement the process. 
# I checked the minimum salary 


# ## 30k to 50k

# In[218]:


df[(df.salary >= 30000) & (df.salary < 50000)]['credit_card'].value_counts()


# In[219]:


condi = [(df.salary < 50000) & (df.salary >= 30000) & (df.credit_card=='zeroes')]
values = ['visa-electron']
df['credit_card'] = np.select(condi, values, default=df['credit_card'])


# In[220]:


df[(df.salary >= 30000) & (df.salary < 50000)]['credit_card'].value_counts()


# ## 50k to 70k

# In[221]:


df[(df.salary >= 50000) & (df.salary < 70000)]['credit_card'].value_counts()


# In[222]:


condi = [(df.salary < 70000) & (df.salary >= 50000) & (df.credit_card=='zeroes')]
values = ['mastercard']
df['credit_card'] = np.select(condi, values, default=df['credit_card'])


# In[223]:


df[(df.salary >= 50000) & (df.salary < 70000)]['credit_card'].value_counts()


# ## 70k to 90k

# In[224]:


df[(df.salary >= 70000) & (df.salary < 90000)]['credit_card'].value_counts()


# In[225]:


condi = [(df.salary >= 70000) & (df.salary < 90000) & (df.credit_card=='zeroes')]
values = ['visa']
df['credit_card'] = np.select(condi, values, default=df['credit_card'])


# In[226]:


df[(df.salary >= 70000) & (df.salary < 90000)]['credit_card'].value_counts()


# ## 90k to 110k

# In[227]:


df[(df.salary >= 90000) & (df.salary <= 110000)]['credit_card'].value_counts()


# In[228]:


condi = [(df.salary >= 90000) & (df.salary <= 110000) & (df.credit_card=='zeroes')]
values = ['visa']
df['credit_card'] = np.select(condi, values, default=df['credit_card'])


# In[229]:


df[(df.salary >= 90000) & (df.salary <= 110000)]['credit_card'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# # Our data cleaning journey in an end

# In[ ]:




