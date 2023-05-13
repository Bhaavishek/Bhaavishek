#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv(r'C:\Users\bhavi\OneDrive\Desktop\Jupyter Data\bundesliga_player.csv')
df.info()


# In[3]:


df.shape


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[6]:


df.head()


# In[7]:


#df.corr()


# In[8]:


df['price'].fillna(df['price'].mean() , inplace = True)
df['max_price'].fillna(df['max_price'].mean(), inplace= True)
df['foot'].fillna(df['foot'].value_counts().index[0], inplace=True)
df['player_agent'].fillna('Unknown', inplace= True)


# In[9]:


num = ['age' ,'height','price','max_price','shirt_nr']
cat = ['position','foot','club','outfitter']


# In[10]:


#def barplots(df,x,y):
#    f,ax = plt.subplots(1,3,figsize=(20,10))
#    Group_data = df.groupby(y)
#    sns.histplot( df, x=x, hue= y, kde= True, ax = ax[0])
#    sns.barplot(x = Group_data[x].mean().index ,
#                y = Group_data[x].mean().values,
#                ax = ax[1], palette='mako')
#    
#    for container in ax[1].containers:
#        ax[1].bar_label(container, color= 'red', size = 15)
#        ax[1].set_xticklabel(Group_data [x].mean().index, rotation=50)
#    
#    palette_color = sns.color_palette('summer')
#    
#    plt.pie(x = df[y].value_counts(), labels = df[y].value_counts().index, autopct= '%.00f%%', color = palette_color )
#    plt.suptitle("{} Bar plot grouped by {} and pie chart", format(x.capitalize(), y) , size= 20)
#    plt.show()


# In[11]:


def barplots(df, x, y):
    f,ax=plt.subplots(1,3,figsize=(20,10))
    Group_data = df.groupby(y)
    sns.histplot(df, x=x, hue=y, kde=True, ax=ax[0])
    sns.barplot(x = Group_data [x].mean().index, 
                y = Group_data[x].mean().values,
                ax= ax[1],  palette = 'mako')
    for container in ax[1].containers:
        ax[1].bar_label(container,color='black',size=15)
    ax[1].set_xticklabels(Group_data [x].mean().index, 
                          rotation = 50)

    palette_color = sns.color_palette('summer')
    plt.pie(x = df[y].value_counts(),
            labels=df[y].value_counts().index,
            autopct='%.0f%%',shadow=True,
            colors= palette_color)
    
    plt.suptitle("{} barplots grouped by {} and pie charts".format(x.capitalize(), y), size=20)
    plt.show()


# In[12]:


for i in cat:
    for j in num:
        barplots(df, j, i)


# # Scatterplots

# In[13]:


sns.pairplot(df, vars=num)
plt.show()

