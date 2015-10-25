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
practice visualizations in matplotlib, the (still very relevant) grand-daddy of
python visualization packages.

Visualization Tools
-------------------

Below is a list of some python visualization packages. For packages that I've 
personally used, I've included
a list of (relative) pros and cons. It is impossible to accurately convey 
everything about these packages in the quick blurbs below; we only list packages
here as a starting point for you to go and investigate them yourself!

**General Purpose Visualization**

  - `matplotlib <http://matplotlib.org/>`
    The most ubiquitous of the python visualization packages. Has a massive
    set of features and is relatively easy to use. It is well documented and has
    very active user and development communities. Achieves cross-platform 
    compatibility by implementing several graphics backends.
    
    Pros:

     - Feature-rich: you can create just about any type of visualization in 
       matplotlib. Check out the `gallery <http://matplotlib.org/gallery.html>`
       for examples

     - Straightforward syntax: modeled after MatLab to make the transition easy
       for MatLab users.

     - Quick to learn and use: while it would be very impractical to memorize
       the syntax for every feature, it has a very low learning curve for most
       basic plotting tasks which make it a good candidate for on-the-fly data
       visualization during analysis.

     - Content-rich plotting: while it may be a bit behind aesthetically (see
       below), matplotlib is more than capable of producing clear and content-
       rich plots of publication quality

     - Cross-platform: Has many backends (e.g. Tk, Qt, wx) including several
       native ones that allow matplotlib to create visualizations on just about
       any platform that supports graphics

     - Very mature: the matplotlib foundation has a team of dedicated developers
       ensuring that the project is actively developed and kept stable. The user
       community is huge and very active.

    Cons:

     - Many find the plots aesthetically outdated

     - Animation/interactivity: matplotlib is king at generating static images.
       While it is capable of dynamic images and user interaction, the learning
       curve for these features is significantly steeper than for static
       visualizations

     - Speed: Related to the last bullet point, if you are trying to generate
       high-performance (i.e. high frame-rate) animations, matplotlib is may be
       sufficient, but is probably not the correct package.

     - 3D visualization: Again, matplotlib has some functionality here, 
       especially for relatively simple visualizations, but for complex 3D
       visualization, another package is required.

  - `pyqtgraph <http://www.pyqtgraph.org/>`
    A performance-oriented package capable of 2D and 3D plotting.

    Pros:

     - Performance oriented: If you need fast animations or high-performance
       3D rendering, this is a very capable package.

     - Cross-platform: Relies only on numpy and python bindings for Qt (either
       pyqt or PySide). Once those are installed, no further compilation is
       required: the package is pure python.

    Cons:
     
     - Very steep learning curve: Even basic tasks can be difficult to 
       accomplish. Furthermore, the documentation and example galleries are much
       more terse and less extensive than matplotlib

     - Still in 0.9.8 and a much smaller user community - it is usually 
       possible but much more difficult to figure out how to do what you want to
       do with pyqtgraph

     - Not developed as actively - lead developer left to join the 
       `VisPy project <http://vispy.org/>`

**3D Visualization**

  - `MayaVi <http://docs.enthought.com/mayavi/mayavi/>`
    A package for high-quality 3D visualization

    Pros:

     - Beautiful 3D visualization with relatively high-level interface (compared
       to pyqtgraph for example)

     - Relatively feature rich

     - Cross platform, easy to install

     - Low learning curve for basic functionality
   
    Cons:

     - Very steep learning curve for more advanced functionality

     - Performance: best for static 3D visualizations, can struggle with dynamic
       visualiztions

     - Scalability: Resource-intensive so can struggle with visualizations of
       large data.

  - `yt <http://yt-project.org/>`
    A package for 3D visualization, originally developed for astrophysics

    Pros:

     - Very aesthetically pleasing - produced beautiful images

     - Active user and developer communities

    Cons:

     - Some 3D visualiztion capabilities are not immediately obvious

**Of interest to statistics folks**

  - `ggplot <http://ggplot.yhathq.com/>`
    For those of you used to ggplot2 in R

  - `seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`
    Package designed specifically for statistical visuzlization

**Browser-based visualization tools**

  - `bokeh <http://bokeh.pydata.org/en/latest/>`

  - `plotly <https://plot.ly/>`
