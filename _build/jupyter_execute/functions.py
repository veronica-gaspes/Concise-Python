#!/usr/bin/env python
# coding: utf-8

# # Functions and methods
# 
# In Python we can also use functions (and a special kind of functions called methods) to build expressions. There are many many functions and methods, we present only some of them. The Python documentation lists some of the functions available in [Built in functions](https://docs.python.org/3/library/functions.html).
# 
# ## Functions for integer numbers
# 
# The Python documentation lists functions specific for numbers in [Numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

# In[1]:


str(3)


# In[2]:


abs(-3)


# In[3]:


abs(3)


# In[4]:


divmod(123456789,10)


# In[5]:


max(1,2)


# In[6]:


max(5,4,3,2,1)


# In[7]:


min(1,2)


# In[8]:


min(5,4,3,2,1)


# In[9]:


type(3)


# ## Functions for floating point numbers
# 
# Many of the functions in [Numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) are for floating point numbers. There are many more in the library ```math``` that you need to import if you want to use it. You import the library with the instruction 
# ```import math``` (see the examples below).

# In[10]:


import math


# In[11]:


# pi is a number, not a function.
# Notice the use of the name of the library (math) and the .
math.pi


# In[12]:


math.sqrt(2)


# In[13]:


# e is a number, not a function
math.e


# In[14]:


math.log(math.e)


# In[15]:


math.sin(math.pi / 2)


# In[16]:


# almost 0!

math.cos(math.pi / 2)


# In[17]:


math.floor(3.1)


# In[18]:


math.floor(3.6)


# In[19]:


math.ceil(3.1)


# In[20]:


math.ceil(3.6)


# ## Functions and methods for strings
# 
# Methods are used in a strange way: ```expression.method(arguments)```! Instead of ```function(all the arguments)```. You should think of the expression to the left of the ```.``` as being one more argument to the method.
# 
# In the examples below, ```len``` is a function that has only one argument: the string for which it calculates the length.  But ```split``` is a method: it uses the string before the ```.``` and results in a list of strings. 
# 
# You can find very many functions and methods in [Text sequence type](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
# 

# In[21]:


len('this')


# In[22]:


len('this is a sentence')


# In[23]:


'this is a sentence'.split()


# In[24]:


# You can specify the separator:

'this is a sentence'.split('a')


# In[25]:


# Notice the empty string after the last 'e' in the result.

'this is a sentence'.split('e')


# In[26]:


# join uses the string before the dot as connector to put together all
# the strings in argument (a list of strings)

'_'.join(['this','is','a','sentence'])


# In[27]:


# Notice the big T in the result!

'this is a sentence'.capitalize()


# In[28]:


'this is a sentence'.upper()


# In[29]:


'THIS IS A SENTENCE'.lower()


# In[30]:


'THIS IS A SENTENCE'.endswith('ENCE')


# In[31]:


'THIS IS A SENTENCE'.startswith('THIS')


# ## Functions for lists
# 
# Lots of functions and methods for lists are described in [Sequence types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).

# In[32]:


len([])


# In[33]:


min([1,2,3,4])


# In[34]:


max([1,2,3,4])


# In[35]:


sum([1,2,3,4])


# In[36]:


sum([x ** 2 for x in [1,3,5,7,9]])


# In[37]:


sorted([5,4,3,2,1])

