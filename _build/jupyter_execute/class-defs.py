#!/usr/bin/env python
# coding: utf-8

# # Defining classes
# 
# Classes are the mechanism Python has for defining new data types. In a class we collect all the methods for the new data type. Methods are defined as functions. They all have an extra argument for the object on which they work on and they can all use instance variables (as well as the arguments and local variables). 
# 
# Here we provide a couple of examples. We start with the type for counters: a counter can be created, incremented and read. The explanations come after each of the program parts.

# In[1]:


class Counter:
    def __init__(self):
        self._value = 0
        
    def inc(self):
        self._value += 1
        
    def read(self):
        return self._value


# Notice the use of ```class Counter:``` that starts the definition: all that comes indented after the ```:``` is the definition of the class. 
# 
# When you define a class you have a new data type (before this definition there was no data type for counters, now there is!). 
# 
# But there are no literals! Instead you need to use the name of the class to create an object of this type. And the code that gets called is the function called ```__init__``` that has to have at least one argument for the object that gets constructed.  This function will not be used outside the class but needs to be there to be used. 
# 
# Here you see how to create an object of type ```Counter```. What you see as a value is a way of presenting a reference (pointer) to the object.

# In[2]:


Counter()


# If we want to use an object of type ```Counter``` we need to assign the object we create to a variable and then use this variable: otherwise, every time we use ```Counter()``` we create a new object!

# In[3]:


c = Counter()
c


# In[4]:


print(c)


# Now we can use ```c```:

# In[5]:


print(c.read())
c.inc()
print(c.read())
c.inc()
print(c.read())


# In the definition of the class you can see that both ```__init__``` and the methods for incrementing and reading use a variable called ```_value```. You could have given this value any name. It is a so called instance variable and every object that you create has its own ```_value```. A convention in Python is that variables that should only be used in the definition of the class are named with an underscore at the start.  
# 
# In the example below we create a new Counter and do some operations to illustrate the fact that each of them has its own instance variable.

# In[6]:


d = Counter()
print(c.read(), d.read())
d.inc()
print(c.read(),d.read())
c.inc()
print(c.read(), d.read())


# We redefine the class counter so that we can create a Counter starting with a given value and we add a method for reset. We also define the method ```__str__``` to generate a string version of the Counter.

# In[7]:


class Counter:
    def __init__(self, start = 0):
        self._value = start
        
    def inc(self, increment = 1):
        self._value += increment
        
    def read(self):
        return self._value

    def reset(self):
        self._value = 0
        
    def __str__(self):
        return 'Counter with value ' + str(self._value)


# In[8]:


c = Counter(10)
print(c) # print  uses __str__!


# In[9]:


c.reset()
print(c)


# In[10]:


c.inc(3)
print(c)


# In[11]:


d = Counter() # the argument for the constructor has a default value 
              # for start! 
print(d)


# In[ ]:




