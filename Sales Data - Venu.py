#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("Sales Data.csv")


# In[4]:


df.head()


# In[5]:


df


# In[6]:


df.shape


# In[7]:


df.info


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


import seaborn as sns


# In[10]:


df.head()


# In[11]:


continuous = ['Price Each',"Sales"]
discrete = ['order id','product','quantity ordered','order dtae','purchase address','month','city','hour']


# In[12]:


df[continuous].describe()


# In[13]:


df.describe(include='object')


# In[14]:


df.describe(include='all')


# In[15]:


df['Product'].value_counts()


# In[16]:


df['Quantity Ordered'].value_counts()


# In[17]:


df['Price Each'].value_counts()


# In[18]:


df['Order Date'].value_counts()


# In[19]:


df['Purchase Address'].value_counts()


# In[20]:


df['Month'].value_counts()


# In[21]:


df['Sales'].value_counts()


# In[22]:


df['City'].value_counts()


# In[23]:


df['Hour'].value_counts()


# In[24]:


df.isnull().sum()


# In[25]:


sns.displot(df['Price Each'], bins=10,kde=True)
plt.show()


# In[26]:


sns.displot(df['Sales'], bins=10,kde=True)
plt.show()


# In[27]:


sns.boxplot(y=df["Price Each"])
plt.show()


# In[28]:


sns.boxplot(y=df["Sales"])
plt.show()


# In[29]:


sns.scatterplot(x=df['Price Each'],y=df['Sales'])
plt.show()


# In[30]:


sns.scatterplot(x=df['Sales'],y=df['Price Each'])
plt.show()


# In[31]:


sns.relplot(x=df['Price Each'],y=df['Sales'])
plt.show()


# In[32]:


sns.relplot(x=df['Sales'],y=df['Price Each'])
plt.show()


# In[33]:


import seaborn as sns


# In[35]:


sns.scatterplot(x=df['Price Each'],y=df['Sales'],data=df,hue='Product')
plt.show()


# In[36]:


sns.scatterplot(x=df['Price Each'],y=df['Sales'],data=df,style='Product')
plt.show()


# In[37]:


sns.relplot(x=df['Price Each'],y=df['Sales'],data=df,hue='Product')
plt.show()


# In[38]:


sns.relplot(x=df['Price Each'],y=df['Sales'],data=df,style='Product')
plt.show()


# In[42]:


sns.relplot(x='Price Each',y='Sales',data=df,kind='line')
plt.show()


# In[48]:


from pandas.core.arrays.sparse import SparseArray as _SparseArray


# In[50]:


df['sno']=pd.Dataframe(np.arange(1,18170))
df
return _SparseArray


# In[52]:


sns.pairplot(df,vars=continuous)
plt.show()


# In[53]:


c_m=df[["Price Each","Sales"]].corr()
c_m


# In[54]:


sns.heatmap(c_m,annot=True)
plt.show()


# In[56]:


sns.countplot(x=df['Product'])
plt.show()


# In[57]:


sns.countplot(y='Product',data=df)
plt.show()


# In[ ]:




