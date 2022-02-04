#!/usr/bin/env python
# coding: utf-8

# # Assignment
# 
# An assignment is a command to replace the value stored in a variable with a value specified as an expression. In Python variables are introduced wherever you need them, there is no need to declare them or state what type of values they can store. Here follow some examples of assignments. 

# In[1]:


x = 2 ** 32


# As you can see, when we use this code there is no result! In fact, most commands do not have a value. We will see later that in Python there are commands that aslo calculate a value. 
# 
# In order to see what has happened we need to use ```x```.
# 
# By the way, variables can also be used in expressions. When we use a variable in an expression, it is its current value that contributes to the value of the expression.

# In[2]:


x


# In[3]:


x = 3


# In[4]:


x


# In the next assignment to ```x``` we use the value of ```x``` before the assignment in the expression used to calculate the value we will assign. 
# 
# Make sure that you understand that when the value of the expression 
# 
# ```x + 2 ** 4```
# 
# is calculated, the value stored in ```x``` is ```3```. 

# In[5]:


x = x + 2 ** 4
x


# ## Quiz
# 
# What happens if you run the code from the previous cell again? Can you explain what happened?

# ## Abbreviations
# 
# While we are at assignments of integer values, you should know that there are some abbreviations for assignments where the expression to the right is just a binary operation involving the variable as one of the operands.
# 
# For example, to increment the value of a variable with ```1``` you would write
# 
# ```x = x + 1 ```
# 
# There is an abbreviation for this:
# 
# ```x += 1```
# 
# where we use ```+=``` instead of ```=```. Then we avoid writing the ```x``` in the expression to the right!
# 
# Here are some more examples:

# In[6]:


z = 0
z


# In[7]:


z += 1
z


# In[8]:


z *= 10
z


# In[9]:


z /= 2
z


# In[10]:


z **= 2
z


# ## Quiz
#    
# If you have a variable, say ```x_0```
# 
# *(yes, identifiers can use an underscore _ and numbers in them! They can even start with an underscore (but not with a number)!)*
# 
# and say you want to modify the value stord in the variable so that is it the double of the value currently stored in the variable. What assignment abbreviation would you use? 

# ## Swapping values
# 
# You can swap the values stored in two variables doing the two assignments in one:
# 
# ```a, b = b, a```
# 
# For example:

# In[11]:


a = 10
a


# In[12]:


b = 20
b


# In[13]:


a,b = b,a

(a,b)


# ## Assignments and lists
#  
# You can use variables to store values of any type. Here are some examples with strings and lists.

# In[14]:


sentence = 'Hi, there!'


# In[15]:


small_cubes = [x ** 3 for x in range(10)]


# In[16]:


(sentence, small_cubes)


# There are two things we want you to be aware of regarding variables that store **lists**. 
# 
# First, the places (positions) in a **list**  are also variables that can be assigned to. 
# 
# Here are some examples:

# In[17]:


small_cubes[-1] = 0
small_cubes


# In[18]:


small_cubes[0] = 729
small_cubes


# Second, look at what happens when we assign the value of an expression to a list:

# In[19]:


a = [1,2,3,4]
a


# In[20]:


b = [1,2,3,4]
b


# In[21]:


a[0] = -1
(a,b)


# When we change
# ```a```
# we do not change ```b``` (of course!)
# 
# **BUT!** look at this:

# In[22]:


c = [1,2,3,4]
c


# In[23]:


d = c
d


# In[24]:


c[0] = -1
(c,d)


# The assignment 
# 
# ```d = c ```
# 
# did not build another object to assign to ```d```, instead, both variables share the same object (the same list). That is why, when we change the list stored in ```c``` we see the change also when we use ```d```.
# 
# Now lets look at one more thing:

# In[25]:


c = [6,7]
(c,d)


# What we did now was to assign to ```c``` another object. ```d``` still stores the object that was assigned to it. 

# ## Quiz
# 
# Try modifying the string in  ```sentence```, for example:
# 
# ```sentence[-1] = '?'```
# 
# You will get an error message. Do you understand it?
