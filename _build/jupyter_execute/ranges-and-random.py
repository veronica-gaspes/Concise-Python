#!/usr/bin/env python
# coding: utf-8

# # Ranges and random
# 
# Here are som more expressions, of a more unusual form but very useful and well used in Python. 
# 
# ## Range  
# 
# Ranges are mostly used to control loops and in list comprehensions in Python, but you can also transform them into lists. The Python documentation describes them in [ranges](https://docs.python.org/3/library/stdtypes.html#ranges).
# 
# 

# In[1]:


# range of numbers 0 ... 9. 

range(10)


# In[2]:


# the list funtion turns the range into a list, 
# so you can see the values in the range.

list(range(10))


# In[3]:


# you can also indicate  with what number to start the range.

list(range(2,10))


# In[4]:


# and you can say with what step to go from one number to the next

# start with 0, end at 9 and use a step of 2:
list(range(0,10,2))


# ## Random
# 
# Random numbers and random values of other types are very useful. For example, to test our programs with random data when we explore how efficient programs are. There are a number of functions for generating random values and the Python documentation describes the ones we will use most often in [functions for integers](https://docs.python.org/3/library/random.html#functions-for-integers), [functions for sequences](https://docs.python.org/3/library/random.html#functions-for-sequences) and [real-valued distributions](https://docs.python.org/3/library/random.html#real-valued-distributions).
# 
# In order to use all the functions we illustrate here you need to import the library ```random```:
# 
# ```import random```
# 
# ### Random integer numbers

# In[5]:


import random


# In[6]:


# a random number that can be 0 or 1 or 2 or ... or 9. 
random.randrange(10)


# In[7]:


# a random number that can be 2 or 3 or ... or 9

random.randrange(2,10)


# In[8]:


# simulate throwing a dice:

random.randrange(1,7)


# In[9]:


# combine list comprehension and random numbers to
# simulate throwing 5 dices:

[random.randrange(1,7) for x in range(5)]


# In[10]:


# 10 experiments throwing 5 dices 
# The value of this expression is a list of 10 lists with 5 elements each!

[[random.randrange(1,7) for x in range(5)] for y in range(10)]


# ### Functions for sequences
# 
# Sequences can be strings, lists or ranges.

# In[11]:


# a random letter from the alphabet:

random.choice('abcdefghijklmnopqrstuvwxyz')


# In[12]:


# a random even number in the range 0 ... 999999:

random.choice(range(0,1000000,2))


# ### Floating point numbers
# 
# There are many interesting functions to generate numbers according to very specific distributions. We will only use one (maybe): a number in the interval $[0,1)$

# In[13]:


random.random()

