******
Lab 10
******

Stats 159/259 - Lab 10 - 11/9/15

Agenda
++++++

1. Quiz 4

   - Attendance

   - 20 minutes for the 10 question quiz

2. Results of code review/other miscellaneous comments

3. Undoing things in Git

4. Project issues

Quiz 4
++++++

Same deal as qz3:

  - 10 Questions, 5 MC, 5 TF

  - MC questions worth 4 pts each, TF worth 2 pts each (manage time accordingly)

  - 20 min to complete

    - Commit on time or lose points!

Code Review Results
+++++++++++++++++++

Overall I liked what I saw. The most important thing which I was pleased to see
everybody do correctly is that you focused in on the specifics of the code.
The true value of code review is having someone look in-detail at what you've
done and critique specific aspects. Having someone look at your code and give
you general feedback ("Too long, make it shorter") is not really that helpful.

Other thoughts:

 - Assigning values to variables rather than calling the function that 
   produces them (especially in loops)

   - Performance (+), clarity/brevity (=)

 - List-comprehension over creating an empty list and using for + append

   - Performance (=), clarity/brevity (+)

 - Iterators (esp. with loops)

   - Performance (can be +), clarity/brevity (+)

 - Iteration vs. recursive formulations

   - May not be straightforward to recast an iterative approach to a recursive
     formulation

   - Have to be aware of 'recursion depth'

**Aside - Python comments**

Docstrings are very useful and should be used, but really only apply to 
module, function, and class definitions::

  """
  Author: Ross Barnowski (rossbar@berkeley.edu)
  Rev: 0.0.1
  DISCLAIMER: This code is offered without any guarantee it won't completely
  destroy the computer you run it on.

  This is a module docstring. It usually has the author, license/copyright info,
  date, and a general description (plus whatever other metadata).
  """

  class MyClass():
      """
      A docstring for a class
      """

      def __init__(self):
          """
          The more descriptive doc string usually goes here
          """

  def my_func():
      """
      Function docstring
      """

The python syntax for in-line commenting is the #::

  """This is inappropriate for in-line comments"""
  do_someting()

  # THIS is how you inline comment
  do_something_else()



Thoughts on Projects
++++++++++++++++++++

**Don't forget testing!** Several groups have started doing a lot of work on 
their projects and have been doing a great job reviewing each other's code. One
big issue however is that as a result of all of the work they are merging into
their projects, their coverage is decreasing! One way to deal with this issue
is to have two parallel lines of development: a *stable* branch (often master)
and a *dev* branch. The stable branch is the one that you present to the world:
it should be the fully tested, fully documented (including installation 
instructions, examples, how-to's etc) version of your code. Anything that is
to be pull-requested into the stable branch must not only be code-reviewed, but
also have associated tests and documentation. This makes releasing code a lot
easier, but can hinder developers who just want to try out ideas and have them
reviewed by their teammates without worrying about all of the extra work like
writing tests and documentation. This is what the dev branch is for: developers
can pull-request into the dev branch any ideas that they want to try or discuss.
Once the code review is complete, if everyone is satisfied that the idea should
be added to the stable branch, the original developer (or, in the case of large
projects, the testing team and documentation team) have to work on producing 
the extra info for the change. Finally, once the tests and documentation are 
written, another pull-request is opened to get work from dev into stable. There
does not have to be explicit code review at this point, assuming nothing has 
changed except the addition of tests/documentation.

You are not required to follow this model for your projects, but it does help
address a problem that we really want to avoid: having the teams scramble 
during the last week to write tests for the entire code base because you haven't
been doing it as you go along.

Another thing to note is that the beginning of projects where there is a lot of
rapid development and the turnover rate on ideas is so high, it is very 
cumbersome to worry about tests & documentation. It is therefore understandable
if you want to get a more firm codebase laid down before you start worrying 
about the above, but the original caveat stands: don't leave all your test and
documentation writing til the end!

Project Issues
++++++++++++++
I went over your projects last night and for each group, created an/some
issue(s) for you to work on for the remainder of the lab session. You are not
obligated to handle them in any particular way, just something for you to work
on for the remainder of the lab.
