*****
Lab 4
*****

Stats 159/259 - Lab 4 - 9/28/15

Agenda
++++++

1. Attendance (for quiz) + quiz instructions

2. Quiz 2 (15-25 min)

3. Idiomatic Python

   - What does this term mean?

   - Why is it important

4. Preliminary HW1 notes

5. Individual/Group work

   - Final project OR

   - Numpy examples from Thursday's lecture (arteries example, due Tuesday)

Idiomatic Python
++++++++++++++++

In python, as in all languages, there are often many ways to express the 
semantic idea that you want to convey. We've already seen a prominent example
of this: for-loops vs. list comprehension. When it comes to creating a list
from an iterative kernel, they are functionally equivalent but syntactically
very different.

 - "Idiomatic" -> think idioms in natural language: often-times express with 
   rich semantic meaning that is lost on people who don't get the idiom.

Here's an excerpt I pulled from 
`an article <http://examples.yourdictionary.com/idiom.html>`_ which was focused
on helping people understand idioms in natural languages:

|    Learning a Language with Idioms
|    -------------------------------
|
|    Because of idioms, learning a language can be complicated. After you can
|    conjugate verbs, and know a lot of words, you may still have difficulty
|    speaking the language with native users.
|
|    This is partly due to the use of idioms and would also depend of which
|    region of a country you were in. Idiom usage is not just regional, but
|    also varies according to people’s interests and social groups.
|
|    The best way to pick up on the meaning of certain idioms would be to
|    converse with people and ask them for a clarification of the idiom if you
|    are not clear about the idiom they used. There are also sites on the
|    Internet which will help explain the meaning of idioms.  


Note there is a difference between expression and choosing a different 
algorithm: the difference between merge-sort and bubble-sort is not 
idiomatic because they are different algorithms

Idiomatic python is important to understand because how you express things has
a huge impact on code clarity. Examples in the next section.

Python in Practice - HW1
++++++++++++++++++++++++

Concrete (and very common) examples of non-idiomatic python from HW1. This won't
affect your grade, but that doesn't mean that it should be ignored.

 - for i in range(len(iterable)): vs. for unit in iterable

 - import placement - top-level scope where it will be used; never in 
   function calls

 - Beware of nesting
   
.. figure:: ../figs/pterodactyl.png
   :align: center
   :width: 100%

   Terrible joke of the day. Picture from 
   `here <http://gallerydriver.com/Art/IMG_2290.jpg>`_.
 
   There's a reason pep8 chose four-space indents - it's to
   discourage too much nesting.
   e.g. 
.

   if:
   else:
       if:
       else:
           if:
   vs.

   if:
   elif:
   elif:

 - Beware of `global`
   This isn't so much an idiomatic thing, but global is dangerous because it
   breaks scoping rules. Can lead to some really frustrating bugs
      Rule of Thumb: If you're working on a small, quick project `global` 
      probably won't kill you. If you're working on a bigger project where 
      you're putting a lot of effort into designing, come up with solutions
      that don't use global

 - Eliminate "double-negatives"
   Lots of instances in homework where things were cancelling themselves out.
   One relatively common example: `zip(*(v1, v2))`. This is equivalent to 
   `zip(v1, v2)` and far less readable.

Work on projects or artery notebook
+++++++++++++++++++++++++++++++++++
