#!/usr/bin/env python
# coding: utf-8

# # List methods and operations
# 
# Methods and operations can also be used to build statements. 
# 
# In the Python documentation you will find several methods and operations that are commands to modify lists. They are documented in [mutable sequences](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable).
# 
# Here we show some of the most common ones. Remeber that statements do not have values, they do something (like assignment: change the value of a variable).

# In[1]:


lst = [1,2,3,4]
lst


# In[2]:


lst.reverse()


# In[3]:


lst


# In[4]:


lst.sort()


# In[5]:


lst


# In[6]:


import random
random.shuffle(lst)


# In[7]:


lst


# In[8]:


# Be careful of this kind of thing:

s = lst.sort()


# In[9]:


# commands do not have values! So what did we store in s?

s


# In[10]:


# what type does s have?

type(s)


# In[11]:


random.shuffle(lst)


# In[12]:


# Can Python calculate a sorted version of a list?
# YES! We know this from the chapter on expressions, 
# Python has the function sorted that given a list calculates 
# another list that is a sorted version of the argument!

s = sorted(lst)
(lst, s)


# In[13]:


# Assign to a slice

s[1:3]=[0,0]
s


# In[14]:


# Assign to a slice!

s[1:3] = []
s


# In[15]:


# repeat s 

s *= 3
s

