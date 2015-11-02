*****
Lab 9
*****

Stats 159/259 - Lab 9 - 11/2/15

Agenda
++++++

1. A quick discussion about *scope*

2. Structured code review exercise

3. Work on your projects

Scope in Python
+++++++++++++++

First, a couple of definitions:

**Name**: A *name* in python is a reference to a python object. For example::

  # Create an object named a
  a = [1, 2, 3]
  # Create a new NAME for the object named a
  b = a
  # a and b should be equivalent
  a == b
  # Are the two objects exactly the same? (i.e. are 'a' and 'b' just two 
  # different names for the same object?)
  a is b
  # Create a new object that is equivalent to a
  c = [1, 2, 3]
  # a and c are equivalent, but are they the same object?
  a == c
  a is c
   
**Block**: A *block* in Python is a piece of code that is executed as a unit.
Examples of blocks include: the body of a function, modules, class definitions,
and script files.

**Scope**: A *scope* defines the visibility of a *name* in a given *block*. If
an object with a given name is defined within a code block, then the *scope* of
that object includes the given *block*.

Why is any of this important? Misunderstanding scope can cause headaches in some
situations; most commonly when you have several objects that have the same
name in different scopes. For example::

  a = 10
  
  def print_a():
      a = 20
      print a

  # Which number gets printed?
  print_a()

The previous example deals with an issue called *name resolution*, i.e. 
figuring out which object you mean when you use the given name. If a name is
unique, then name resolution is easy, but if there are different objects with
the same name in different scopes, then name resolution is a little more 
involved (although pretty straightforward, once you understand it). 

There is a rule-of-thumb for Python name resolution: the **LEGB** rule. It 
specifies the order of name resolution when there are multiple scopes. It is 
analogous to the order of operations in arithmatic (PEMDAS). The LEGB
rule states the order that scopes are searched for a given name:

  1. **L** ocal 

  2. **E** nvironment

  3. **G** lobal

  4. **B** uiltin

To understand this rule, we should define another term: *environment*. An 
envirnoment is just the set of all scopes that are visible to a given
block. For example, if you define a function within a module (as we do all the
time) then the *environment* for code within that function includes the 
function scope, and the module scope.

Now, back to name resolution: The key thing to remember is that Python will
search through the local scope first, then work it's way outward. If it hasn't
found anything in the environment, it will move on to variables defined with
*global* scope. If it still hasn't found an object with the given name, it 
moves on to it's own set of built-in functions. If at that point it still hasn't
found any object with the given name, it will throw a `NameError` exception.

There is one final term that should be defined here, and that's **namespace**.
A *namepace* is essentially just a lookup table that relates every name to an
underlying object. You can think of a namespace as a python dictionary, where
the key corresponds to the name, and the value is the underlying python object::

  namespace = {"name1":object1, "name2":object2} #...

This helps illuminate how one object can have multiple names: it's just the
same object, stored in the dictionary under multiple keys. The concept of
namespace is useful with regards to naming resolution because all that name
resolution really is is a search through the keys of the namespace
dictionaries. The search 
starts with the *local* namespace; if there is no key in the dictionary 
corresponding to the given name, it moves on to the *environment* namespace,
etc.

In practical terms, name resolution has a couple big implications:

1. You have to be careful what you name things. There are certain built-ins with
   set names and if you name an object with the same name as one of the 
   built-ins, the LEGB rule dictates that the name will now resolve to your
   object rather than the built-in. For example::

     int = 1
     # Try to convert a float to an int:
     int(2.0)

   Another common example: keywordargs::

     from pprint import pprint

     def print_my_type(a):
         print type(a)

     print_me(1)

     def print_my_type(a, type="pretty"):
         """
         Print the type of the input. The type kwarg specifies how to print
         the information.
         """
         if type == "pretty": pprint(type(a))
         else: print type(a)

     print_my_type(1)

     # type is still okay outside the scope of the print_me function
     type(1)

2. Naming different objects with the same name in different scopes. This happens
   all the time, but you just have to be aware of the scope of your objects to
   be able to figure out which object you're referring to (see original 
   example).

That's it for the brief intro to scope. If you're curious and would like to
learn more (scope and name resolution are important features of all computer
languages, not just python), you might want to check out:

`Python's execution model <https://docs.python.org/2/reference/executionmodel.html>`_

You can also check out the wikipedia pages for 
`scope <https://en.wikipedia.org/wiki/Scope_(computer_science)>`_ and
`name resolution <https://en.wikipedia.org/wiki/Name_resolution_(programming_languages)>`_

Exercise: Code Review
+++++++++++++++++++++

In this exercise, you will be critiquing each others' solutions to HW2. This 
may be nervewracking, as it is likely (with the exception of your project work)
the first time you've exposed your code to the critical eyes of others. 
Although it may seem scary, as we've mentioned before, critical code review is
one of if not the best and fastest ways to improve your programming ability.
Learning how to accept and dole-out constructive criticism is a very important
and over-looked skill, so we're going to try to develop it a bit today.

1. Get into your teams (doesn't have to be your project team)

2. One member of your team will create a GitHub repo called 
   code\_review\_practice (or something like that)

3. Everybody else in the team fork that repo and set up your remotes (just like
   the lab6 exercise)

4. Every member of the group should now copy their num.py solutions from HW2
   and put them into the code\_review\_practice repo with a format like
   <your_name>\_num_solutions.py

5. Also add Jarrod's solutions to the repo.

6. As a group, choose three functions from num.py that you will review.

7. Using the GitHub code review model we've been practicing in class, review 
   each of the 3 functions you've selected. It's up to you how you decide to do
   this (you can split up into subgroups etc). When reviewing the functions,
   keep the following characteristics in mind:

   - code clarity / readability

   - brevity

   - code performance (you may want to use ipython's %timeit feature for some
     basic code profiling)

8. At the end of the exercise (~45 min), your group should have analyzed each
   other's (and Jarrod's) solutions to num.py. Share your findings amongst 
   yourselves, with specific reference to the three characteristics above.
   Summarize your thoughts in a `results.md` file. This file could contain, for
   example, a listing of positive and negative examples of code with respect to
   clarity, brevity, and performance.

We won't be "grading" the results.md, but we will look at it to see what you 
came up with and provide our own feedback.

Project work
++++++++++++

The rest of the class time is for you to work on your projects!
