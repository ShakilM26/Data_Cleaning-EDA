#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as pe
import plotly.graph_objects as go


# In[2]:


df = pd.read_csv('employee_filter.csv', index_col=0)
df.columns


# #### Using Bar-chart

# In[3]:


# credit_card user each country

pe.bar(df, y='credit_card', color='country', height=400, width=750, title='Credit-Card user')


# In[4]:


# top 10 country with employees

fig = pe.bar(df.country.value_counts().head(10), color=df.country.value_counts().head(10),
             title='Top 10 Country')
fig.update_layout(autosize=False)
fig.show()


# In[5]:


# Each continent with gender

fig = pe.bar(df, x='continent', color='gender', barmode='group', height=400, title='Gender in each Continent')
fig.update_traces(textposition='outside')
fig.update_layout(autosize=False)
fig.show()


# In[7]:


fig = pe.bar(df, x='year', y='age', hover_data=['salary', 'balance'], color='age',
             labels={'age':'age of employees'}, height=400)
fig.show()


# In[8]:


na = df.query("continent == 'North America'")
fig = pe.bar(na, x='age', y='salary', color='country', text='salary', height=400)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=30, xaxis_tickangle=-45)
fig.show()


# #### Histogram

# In[9]:


fig = pe.histogram(df, x='continent', y='salary', color='continent', height=400)
fig.update_layout(autosize=False)
fig.show()


# #### Pie chart

# In[10]:


# each continent with total salary

colors= ['mediumturquoise', 'darkorange', 'lightgreen', 'darkblue']
fig=go.Figure(data=[go.Pie(values=df.balance, labels=df.continent, textinfo='percent+label')])
fig.update_traces(hoverinfo='percent+label', textinfo='value', marker=dict(colors=colors))
fig.update_layout(autosize=False, height=350)
fig.show()


# In[ ]:





# In[ ]:


highest_salary = df.groupby('age')['balance'].sum()


# In[ ]:


pe.bar(highest_salary, y='balance', height=400)


# In[ ]:





# In[ ]:





# In[63]:


yearly_born = df.groupby('year')['full_name'].count()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




