#!/usr/bin/env python
# coding: utf-8

# # Sequence
# 
# We now start looking at how we can put together statements to build programs.
# 
# The first way of puting together statements is in a sequence. In Python you do this by writing the statements in consecutive lines. 
# 
# A sequence of statements is executed by executing the statements one after the other, accumulating the changes. 
# 
# Here are some examples:

# In[1]:


x = 0
x += 1
x *= 10
x //= 2
x **= 2
x


# ## Writing to standard output
# 
# We take the opportunity to introduce a statement for writing values to standard output. 
# 
# In the example notice that the statement ```print(x)``` that we use several times, writes different values to standard output. It uses the value of ```x``` at the point where the statement is executed, an we change the value of ```x``` with assignments.

# In[2]:


x = 0
print(x)
x += 1
print(x)
x *= 10
print(x)
x //= 2
print(x)
x **= 2
print(x)


# The ```print``` statement can be configured by including what the last string should be. As it is, the last string is a new line character.
# 
# Here we configure it so that it uses a comma and a white space:
# 

# In[3]:


x = 0
print(x, end = ', ')
x += 1
print(x, end = ', ')
x *= 10
print(x, end = ', ')
x //= 2
print(x, end = ', ')
x **= 2
print(x)

