#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd 
import numpy as np
df=pd.read_csv('AmazonB.csv')
print(df.to_string())
amazon = pd.read_csv("AmazonB.csv")
amazon.head(20)


# In[28]:


x=df['Item Subtotal'].mean()
print("The average item cost $",x)


# In[16]:


y=df['Item Subtotal'].median()
print("The median price is $", y)


# In[15]:


z=df['Item Subtotal'].mode()
print("The most common price is $", z)


# In[35]:


m=df['Item Subtotal'].min()
print("The least expensive item was $",m)


# In[29]:


s=df['Item Subtotal'].sum()
print("The total spent was $", s)


# In[34]:


d=df['Item Subtotal'].std()
print("The standard deviation was", d)


# In[37]:


e=df['Item Subtotal'].max()
print("The most expensive item was $",e)


# In[82]:


import matplotlib.pyplot as plt 

df.plot(kind='scatter', x='Category', y='Item Subtotal Tax')
plt.show()


# In[59]:


df.plot(kind='bar', x='Category', y='Item Subtotal')
plt.show


# In[108]:





# In[121]:


df=pd.read_csv('AmazonB.csv')
y2="Item Subtotal Tax"
df.plot(x='Category', y='Item Total')
plt.show()


# In[122]:


import numpy as np
df=pd.read_csv('AmazonB.csv')
df=pd.DataFrame(np.random.randn(10,2),columns= ["Item Subtotal", 'Item Tax Subtotal'])
x='Category'
y='0,10,20,30,40,50'
df=df.cumsum()
plt.figure()
df.plot()
plt.legend()


# In[123]:


df=df.cumsum()
plt.figure()
df.plot()
plt.legend()


# In[132]:


df=pd.read_csv('AmazonB.csv')
df.plot('Category', 'Item Subtotal Tax')
plt.show()


# In[138]:


df=pd.read_csv('AmazonB.csv')
df.plot(kind='pie', x='Category', y='Item Subtotal')
plt.show


# In[ ]:




