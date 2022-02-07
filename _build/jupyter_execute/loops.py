#!/usr/bin/env python
# coding: utf-8

# # Loops
# 
# Loops allow us to repeat a command. We will look at two ways of building loops: ```for``` statements and ```while``` statements. The Python documentation has details in [the for statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) and [the while statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement).
# 
# ## The ```for``` statement
# 
# This statement can be used when a given command has to be executed **a given number of times** (instead of **while a condition holds**)
# 
# Here are some examples. 
# 
# We want you to notice 2 things:
# 
# * the command that is repeated has to be written after the ```:``` and indented.
# 
# * the command that is repeated can be formed using all ways of building commands: assignments, sequence, conditionals and other loops!

# In[1]:


# Observe the indentation of print.

for x in range(10):
    print(x, end = ' ')


# In[2]:


import random


# In[3]:


# Ten experiments of flipping a coin.
# Notice that each of the 10 times a sequence of
# an assignment and a conditional is executed.

for x in range(10):
    
    val = random.random()
    # 4 tenths of the times heads, 4 tenths of the times tails
    # 2 tenths of the times standing
    if   val < 0.4 : print('HEADS')
    elif val < 0.8 : print('TAILS')
    else           : print('STANDING')


# For larger experiments we do not want to print the result of the experiment but instead we might want to count.
# 
# In the example notice that printing is done **after the for loop is done**. Indentation is important: if we had written the print statements with the same indentation as the if statement we would see 10000 outputs!
# 
# The program is a sequence of 3 assignments, a for loop and three print statements. In the for loop we also have a sequence: an assignment and an if statement.

# In[4]:


# 10000 experiments

heads = 0
tails = 0
standing = 0
for x in range(10000):
    val = random.random()
    # 49 hundredths of the times heads, 49 hundredths of the times tails
    # 2 hundredths of the times standing
    if   val < 0.49 : heads += 1
    elif val < 0.98 : tails += 1
    else            : standing += 1
print('Heads: ', heads)
print('Tails: ', tails)
print('Standing: ', standing)


# In the following example we use a sequence of a for-loop and a print as the command that has to be repeated 5 times. The print is there to introduce a new line. 

# In[5]:


for x in range(5):
    for y in range(x, 5):
        print('(', x, ', ', y, ')' ,  end = ' ')
    print()


# As you can see, the parts that are printed get separated by a white space. We can also configure this, for example to say that there should be no space:

# In[6]:


for x in range(5):
    for y in range(x, 5):
        print('(', x, ', ', y, ')' , sep = '',  end = ' ')
    print()


# ## The ```while``` statement
# 
# This statement can be used when a given command has to be executed **as long as a condition holds**.
# 
# Here are some examples. 
# 
# We want you to notice 2 things:
# 
# * the command that is repeated has to be written after the ```:``` and indented.
# 
# * the command that is repeated can be formed using all ways of building commands: assignments, sequence, conditionals and other loops!
# 
# The first example is a sequence of an assignment, a print command and a while statement. The command to be repeated (after the : and indented) will be executed as long as the value of n is larger than 1 (when the value of n becomes 1 or less the while loop will terminate). This command that is repetated is a sequence of an if statement and a print command. Observe that each turn of the loop modifies n, though not always to a smaller value! It is unclear whether the loop terminates for any possible value of n! You can check [the Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).

# In[7]:


n = random.randrange(1,50)
print(n)
while n > 1:
    if n % 2 == 0: n = n // 2    # if n is even, divide it by 2
    else         : n = 3 * n + 1 # if n is odd, multiply it by 3 and add 1
    print(n)


# In[ ]:




