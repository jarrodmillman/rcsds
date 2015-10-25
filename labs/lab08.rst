*****
Lab 8
*****

Stats 159/259 - Lab 8 - 10/26/15

Agenda
++++++

1. HW 2 Due today (10/26) @ 21:00

   - Last-minute questions?

2. Getting set up for Tuesday (and beyond)

   - Make sure Mac users have homebrew

   - Install LaTeX and `Pandoc <http://www.pandoc.org/installing.html>`.

3. Visualization in Python

   - Brief intro

   - Group exercise: matplotlib breakout session

Getting Started
+++++++++++++++

   - Who's done with HW 2?

   - How many of you are using MacOS for the course?

     - Of those, how many of you have homebrew installed?

If you are using MacOS, you may have experienced unusual behavior from your
python, especially when using different modules. There are several resources
that I believe we have mentioned in class before, but we'd like to emphasize
again to make sure that everyone is on the same page. Both are from Matthew:
the `first <http://practical-neuroimaging.github.io/installation.html>` 
is a very brief how-to for getting your Mac set up for using 
scientific python. While you should all be well beyond this step at this point
in the course, there is a very nice script in the post that validates that your
system is set up properly. If you are running MacOS, I strongly recommend
checking that post out and running the 
`check_pna_install.py <https://nipy.bic.berkeley.edu/pna/check_pna_install.py>`
script to validate the setup on your system. The 
`second post <https://github.com/MacPython/wiki/wiki/Which-Python>` is relevant
for any MacOS users who have run into the user vs. system python problem. For
instance, I know many of you have had problems where you use pip to install a
package, but then get an import error when trying to use it in an ipython 
session. Matthew has helped many of you with this problem during lecture, but
if you want an overview of how this problem comes about and what to do about it,
check out this post.

Visualization
+++++++++++++

Visualization is obviously an important part of any STEM pursuit. It has
always played an important role in communicating ideas to others, but one of the
main advancements brought about within the last 15 years by interactive data
analysis platforms like MatLab, R, and IPython is the ability to visualize as
you analyze. Thus there are several different domains in which we'd like to 
be able to visualize things: for communication purposes (i.e. "for others"), and
for analytical purposes (i.e. "for ourselves). When generating visualizations
for communication purposes, we'd like tools that create publication-quality, 
content-rich visualizations with expressive, reproducible command-line syntax.
When visualizing during data analysis (e.g. to check our work after applying
some analysis to data), we'd really like tools that are loaded with features,
have simple interfaces/syntax, and are quick and easy to learn and fast to use.
Many toolkits cover both domains reasonably well, though as your visualization
needs get more and more specific (as they inevitably will throughout the course
of any project) you will find that some tools fit your needs better than others.

There are many, many visualization toolkits in python. We will introduce and
briefly discuss some of them, followed by a breakout session where you can 
practice visualizations 
