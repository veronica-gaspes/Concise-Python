#!/usr/bin/env python
# coding: utf-8

# # Defining functions
# 
# We start by showing how to define functions as you would in mathemtics: to calculate a value given the values of the arguments. The purpose of these functions is to have more ways of building expressions.  
# 
# We will anyway do it for arguments and results that are not only numbers: we will use all the types we learned about.
# 
# For functions that introduce commands, please check [Functions can be commands](#commands)
# 
# 

# ## Our first function
# 
# We want a function that calculates the sum of the first n positive odd numbers. In math we would write the value that we want to calculate using the expression 
# 
# $$\sum_{i = 1}^{i = n}{2i-1}$$
# 
# And we would write the defintion as
# 
# $$ f(n) = \sum_{i = 1}^{i = n}{2i-1}$$
# 
# You can try to calculate the value of $f$ for some values of $n$!
# 
# In our programs we try to name functions with names that say something about what they calculate. We often also write a comment saying what the argument is supposed to be!

# In[1]:


# n is an natural number: indicates the number of positive odds 
# that will be added.
def first_odds_sum(n):
    return sum([2*i-1 for i in range(1, n+1)])


# In[2]:


first_odds_sum(4)


# In[3]:


# here is an expression that uses your function:
first_odds_sum(10) == 10**2


# In programs functions can return values than need not be numbers, for example booleans. The following function will allow us to test a hypothesis: it seems that the sum of the first $n$ odd numbers is $n^2$.

# In[4]:


def hypothesis(n):
    return first_odds_sum(n) == n**2


# In[5]:


hypothesis(25)


# We will not try to prove that the result is true for all values of $n$ (that is something that you can do in math). But, we would like to test the hypothesis in many cases. 
# 
# We can in fact test it with random values for the argument. And we can do this many times. 
# 
# Here is a function that calculates ```True``` if the hypothesis is true for all tested cases and ```False``` if there is a test case that falsifies it.
# 
# 

# In[6]:


# the argument is the number of times we want to test the hypothesis.
import random
def test_hypothesis(times):
    for k in range(times):
        n = random.randrange(0, 1000001)
        if not hypothesis(n): return False
    return True


# In[7]:


# test the hypothesis with 10 random numbers:
test_hypothesis(10)


# The function  ```test_hypothesis``` can seem a little strange; so lets explain it. The result is a truth value (a boolean): either true or false. Given a number that says how many times we want to test the hypothesis, it returns either true or false.
# 
# The first thing to notice is that we needed commands to be able to calculate a result: the body of the function is not just an expression, instead it is a command that calculates a value.  
# 
# The second thing to notice is the use of the ```return``` statement. There is one use inside the ```for-```loop. Every turn of the loop a random number is generated and used to compare the value of  ```first_odds_sum(n)```with ```n ** 2``` (using the function ```hypothesis```). If the hypothesis does not hold for a given number it means we do not need to do any more tests, we know already the result! The return in that place quits not only the ```for-```loop but also the function with value ```False```. If all of the random numbers that were generated in each turn of the loop do not falsify the hypothesis the loop will terminate after all the turns: and then we also know that the result is  ```True```.

# <a id="commands"></a>
# 
# ## Functions can be commands
# 
# We might want to have another function for testing the hypothesis, one that instead of calculating a boolean value prints an informative message to standard output. Here it is.

# In[8]:


def test_hyp(times):
    for k in range(times):
        n = random.randrange(0, 1000001)
        if not hypothesis(n): 
            print('Number',n,'falsifies the hypothesis.')
    print('The hypothesis was not falsified for any of the',times, 'random numbers.')


# In[9]:


test_hyp(10)


# This function is very different from the first one:
# * it does not calculate a value: instead it just prints a message. 
# * it might print many messages: all values that falsify the hypothesis inside the loop will be printed. If we had wanted the function to end after finding the first case we could use a ```return``` without any value after the print.

# ## Functions with lists and strings
# 
# Of course we can also define functions that take lists and / or strings as arguments and return  lists or strings as results.

# In[10]:


# a is a non empty list  of numbers.
def average(a):
    return sum(a) / len(a) 


# In[11]:


average([1,2,3,4,5])


# In[12]:


# s is a number and a is a list of numbers.
# The result is a list of the same length as a 
# with the elements scaled by s

def scale(s, a):
    res = [0] * len(a)
    for i in range(len(a)):
        res[i] = s * a[i]
    return res


# In[13]:


scale(3, [1,2,3,4])


# In[14]:


# n is a non negative integer, s is a string
# The result has added n white spaces to s

def indent(n, s):
    spaces = ' ' * n
    return spaces + s


# In[15]:


indent(3, 'this is it!')


# ## Functions with default arguments
# 
# You have already seen that the command ```print``` can be used with the arguments that are to be printed, but that you can also configure it with values for the separator and ending strings. The way of achieving this is using arguments with default values.  Here we define a version of indent, that we call fill:

# In[16]:


def fill(n, s, val = ' '):
    filler = val * n
    return filler + s


# In[17]:


fill(3, 'this is it!')


# In[18]:


fill(3, 'this is it!', val = '-')


# In[19]:


fill(3, 'this is it!', val = '*')


# In[20]:


# This function is a command: it modifies a list by swaping two elements.
# The arguments are the list a and the two positions for the elements to 
# swap place. 
def swap(a, i, j):
    a[i],a[j] = a[j],a[i]


# In[21]:


lst = [1,2,3,4]
swap(lst,1,3)
lst

