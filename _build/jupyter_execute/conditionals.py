#!/usr/bin/env python
# coding: utf-8

# # Conditionals
# 
# Conditionals are used to choose between different statements. The ```if``` statement is what Python provides for choosing between different statements. The Python documentation has more information in [if](https://docs.python.org/3/reference/compound_stmts.html#if).
# 
# Here are some examples. 

# In[1]:


# We want to simulate flipping a coin.
# We start by importing random:

import random


# In[2]:


if random.randrange(0,2) == 0: print('HEADS')
else                         : print('TAILS')


# In[3]:


# We assign to val before testing because every time we use the
# expression random.random() we get a new value!

val = random.random()
# 4 tenths of the times heads, 4 tenths of the times tails
# 2 tenths of the times standing
if   val < 0.4 : print('HEADS')
elif val < 0.8 : print('TAILS')
else          : print('STANDING')


# In[ ]:




