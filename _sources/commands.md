# Commands

Commands can be executed.  Commands are formed using assignments, sequences, conditionals, loops and methods This chapter shows you how to use commands.

The book [Introduction to programming in Python](https://introcs.cs.princeton.edu/python/) presents some commands  in [chapter 1.3](https://introcs.cs.princeton.edu/python/13flow/.)

## Expressions vs commands

While expressions have values, commands are instructions, most often to make changes in the program or to do something in the environment for the program: for example printing to standard output, or drawing to the screen or using a file.

We will start from the most elementary command: assignment. For this we need to introduce variables. You might have noticed that the chapter on  expressions did not use variables. Well, actually yes:  in some list comprehensions we did! But this was very much like the use of variables in math. For assignments we need to understand variables as boxes where we can store objects. Assignment is the command for changing the object that is stored in a box.

Variables are identifiers that you can introduce in your program  as you need them:  when you assign them an object for the first time. In Python assignments look as follows:

```variable = expression```

Now you see why we started with expressions: we need them to say what object (value) we want to store in a variable.

```{note}
Notice  that the assignment command has a variable to the left and an expression to the right and is not a comparison between two values.
```

```{warning}
The symbol  ```=``` should not be confused with equality.

In Python equality is an operation and is designated with ```==```.

I tis used with two expressions as in

``` expression == expression ```
```

