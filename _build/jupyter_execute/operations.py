#!/usr/bin/env python
# coding: utf-8

# # Operations
# We now move to **operations**. Operations allow us to describe values indicating that something has to be calculated. Operations are specific to the different types, even if some of them mix types (for example comparing numbers results in a truth value!). 
# 
# It is important that you understand in what order the calculations are done when you use more than one operation to form an expression. This is guided (like in math) by what we call operator precedence, operator associativity and the order of evaluation. In the book this is described in detail in [an appendix](https://introcs.cs.princeton.edu/python/appendix_precedence/).
# In the Python documentation this is described in [chapters 6.16 and 6.17](https://docs.python.org/3/reference/expressions.html#evaluation-order)
# 
# ## Operations for integer numbers
# 
# You are encouraged to experiment with expressions that use several operators, for example ```3 + 5 - 4 / 2```, to understand precedence, associativity and the order of evaluation. In order to express the calculation that you want you might need to use paretheses to make it clear what operator has to be used first.

# In[1]:


3 + 4


# In[2]:


3 - 4


# In[3]:


3 + 4 - 5


# In[4]:


3 - 4 - 5


# In[5]:


3 - (4 - 5)


# In[6]:


# this operation converts (casts) 3 and  2 to float 
# and results in a float!

3 / 2


# In[7]:


# this operation returns the quotient of integer division.

123456789 // 10


# In[8]:


# this operation returns the remainder  of integer division.

123456789 % 10


# In[9]:


2 ** 32


# In[10]:


# These operations result in a boolean value.
# Make sure you agree to the values in the six-tuple!

(3 == 3, 3 != 3, 3 < 3, 3 > 3, 3 <= 3, 3 >= 3)


# ## Operations for floating point numbers
# 
# You are encouraged to experiment with expressions that use several operators, for example ```3 + 5 - 4 / 2```, to understand precedence, associativity and the order of evaluation. In order to express the calculation that you want you might need to use paretheses to make it clear what operator has to be used first.

# In[11]:


3.141592653589793 + 2.0


# In[12]:


0.123456789e2 - 1.5


# In[13]:


1.4142135623730951 * -1.4142135623730951


# In[14]:


10.3 / 1.234567


# In[15]:


1.4142135623730951 ** 2.0


# In[16]:


# These operations result in a boolean value.
# Make sure you agree to the values in the six-tuple!

(3.1 == 3.1, 3.1 != 3.1, 3.1 < 3.1, 3.1 > 3.1, 3.1 <= 3.1, 3.1 >= 3.1)


# ## Operations for booleans
# 
# For the order of evaluation see [boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)

# In[17]:


True and False


# In[18]:


True or False


# In[19]:


not True


# In[20]:


3 > 3 and 3 == 3 or 3 >= 3


# In[21]:


123456 % 3 == 0


# In[22]:


12345 % 3 == 0


# In[23]:


1234 % 3 == 0 or 1234 % 2 == 0 


# ## Operations for strings

# In[24]:


# + is append!

'Hello to you, ' + 'vero!'


# In[25]:


# string * int: use + as many time as the number indicates

10 * '-'


# In[26]:


# Make sure you learn about precedence, associativity 
# and the order of evaluation

3 * 'this, and ' + 'that!'


# In[27]:


# string[int] results in the character (string) 
# in the position given by the number.
# The first position is 0.

('this'[0],'this'[1],'this'[2],'this'[3])


# In[28]:


# Negative numbers can be used as positions.

'this'[-1]


# ## Operations for tuples
# 
# The operation ```tuple[int]``` results in the element in the tuple in the position indicated by the number. Positions start with 0. Negative numbers can be used as positions: -1 is the position length of tuple - 1 (the last position in the tuple).

# In[29]:


(3.141592653589793, 'Pi!', True)[0]


# In[30]:


(3.141592653589793, 'Pi!', True)[1]


# In[31]:


(3.141592653589793, 'Pi!', True)[2]


# In[32]:


(3.141592653589793, 'Pi!', True)[-1]


# ## Operations for lists
# 
# Again, selecting the element for a position, same as for strings and tuples.
# 
# But also slicing: ```list[start:end]``` results in a list with the elements at positions ```start``` upto ```end - 1```. The end points of the slice can be omitted, see the examples below.
# 
# ```+``` and ```* int``` as for strings. 
# 
# Finally, list comprehensions (hopefully familiar from math: set comprehensios).

# In[33]:


[1,2,3,4][0]


# In[34]:


[1,2,3,4][-1]


# In[35]:


[1,2,3,4][1:3]


# In[36]:


[1,2,3,4][:3]


# In[37]:


[1,2,3,4][1:]


# In[38]:


[1,2,3,4][:-1]


# In[39]:


[1,2,3,4] + [4,3,2,1]


# In[40]:


10 * [0]


# In[41]:


# Your first list comprehension.
# Read it as:
#      The list of x square for all values x in the list [1,2,3,4]

[x ** 2 for x in [1,2,3,4]]


# In[42]:


# Your second list comprehension.
# Read it as:
#      The list of x in the list [1,2,3,4] if x is even

[x for x in [1,2,3,4] if x % 2 == 0]


# In[43]:


# Your third list comprehension.
# Read it as:
#      The list of x square for x in the list [1,2,3,4] if x is even

[x ** 2 for x in [1,2,3,4] if x % 2 == 0]

