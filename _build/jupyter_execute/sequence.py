#!/usr/bin/env python
# coding: utf-8

# # Sequence
# 
# We now start looking at how we can put together commands to build programs.
# 
# The first way of puting together commands is in a sequence. In Python you do this by writing the commands in consecutive lines. 
# 
# A sequence of commands executes the commands one after the other, accumulating the changes. 
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
# We take the opportunity to introduce a command for writing values to standard output. 
# 
# In the example notice that the command ```print(x)``` that we use several times, writes different values to standard output. It uses the value of ```x``` at the point where the command is executed, an we change the value of ```x``` with assignments.

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


# The ```print``` command can be configured by including what the last string should be. As it is, the last string is a new line character.
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

