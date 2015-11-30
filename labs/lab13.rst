******
Lab 13
******

Stats 159/259 - Lab 13 - 11/30/15

Agenda
++++++

1. Quiz 5

2. Quick talk on Latex

3. Work on your projects

   - Drafts of final report are due tonight by 9:00 PM if you want feedback
     from Jarrod, Matthew, JB, and I. You are *very strongly* encouraged to
     take advantage of this!

Quiz 5
++++++

Same deal as qz4:

  - 10 Questions, 5 MC, 5 TF

  - MC questions worth 4 pts each, TF worth 2 pts each (manage time accordingly)

  - 20 min to complete

    - Commit on time or lose points!

LaTeX
+++++

You should all have used LaTeX (or some other markup language + pandoc to 
convert to LaTeX) for this class, but we never gave you any specific lectures
about it. Since you will likely be doing a lot of writing for your reports in
the near future, I figured I would give you a high-level overview of some
practical things that may not be clear from the template we gave you.

If you want a more detailed and methodical introduction to LaTeX or are an
absolute beginner, you might want to check out *Introducton to LaTeX* on the
`berkeley SCF tutorials page <http://statistics.berkeley.edu/computing/training/tutorials>`_.

N.B. The following notes are derived from Chapter 20 of 
`Effective Computation in Physics <http://shop.oreilly.com/product/0636920033424.do>`_.
I know I've plugged it before, but this really is a fantastic book for the 
stuff that we cover in this class. If you are planning on doing computation in
the future, especially if you're going to (or are currently in)
graduate school, I strongly recommend checking this book out!

A LaTeX document is built from several different types of files:

 - *.tex*: This is the main document file and is the only one that is absolutely
   necessary to create a document. In order to take full advantage of
   LaTeX, you will likely have other source files as well, perhaps 
   including:
 - *.cls*: Class files. These specify top-level document classes. There are 
   many by default (e.g. article, letter, book) but a really nice thing is
   that many journals provide class files for articles that are 
   compliant with their publication requirements.
 - *.sty*: Style files. These specify many things about the overall design and
   formatting of a document.
 - *.bib*: A file containing bibliography entries and information. Various 
   different tools will automatically compile a bibliography from the
   source material contained in the .bib file

When you build a LaTeX document from source files, a bunch of other files are
generated in the build process, such as *.aux*, *.log*, *.bbl*, and other types
of files. These files are generated in the build process, and thus should NOT
be tracked by version control --- they are merely there to record and help
debug the document building process. After a successful build, they can be
removed without affecting the document itself: it is very common to add these
files to .gitignore, as well as have a target for a Makefile called *clean* that
will automatically remove these types of files.

**Latex Environments**

LaTeX builds off the idea that the content you are trying to present generally
falls into some kind of category, which may have some additional features
associated with it. For example, a figure may have attributes such as a
caption, and some formatting information (like "make this figure 
left-justified"). LaTeX handles these categories by having
the user specify *environments*. In fact, the first (and only required) 
environment in any document is the document environment, which is specified as
follows:

.. code-block:: latex

  % Note the '%' sign denotes comments in LaTeX source files
  \begin{document}              % Start the document environment
  Document content goes here
  \end{document}                % End the document environment

LaTeX environments are all specified in the same manner, with a *\begin{}* and
*\end{}* to delimit them. Other common environments include *enumerate* for 
numbered lists, *itemize* for bulleted lists, *table* for formatted tables,
*figure* for graphics, and *equation* for numbered equations.

N.B. --- the user can specify their own environment and environments may be
slightly different between document types!

**General structure of a LaTeX document**

Here is a skeleton LaTeX document that shows a common layout for article/report
documents created in LateX:

.. code-block:: latex

  % The top non-comment line specifies the type of the document. The format for
  % the command that does this is \documentclass[options]{class_type}
  \documentclass[11pt]{article}

  % Before we even get to the content, there is usually a list of packages that
  % are being used to build the given document. This is analogous to 
  % import statements in a python script --- you are specifying which tools
  % you will be using for the current document
  \usepackage{graphicx}      % For including figures
  \usepackage{amsmath}       % Ability to align equations and other math helpers
  \usepackage{amssymb}       % An extended list of math symbols

  % Next comes some metadata about the document, often called the preamble.
  % The preamble includes things like the author(s), title, date, etc.
  % Note that this is *metadata* so it is not automatically rendered into the
  % final document. The \maketitle command, if called within the document
  % environment, will collect this metadata and add it to the content of the
  % document
  \author{Ross B.}
  \title{On Using \LaTeX~}

  % Now we FINALLY get to the actual document
  \begin{document}
  
  % Take all the metadata above and convert it into a pretty title for our
  % document
  \maketitle

  % Document structure
  % Any document is usually broken up into subparts. For example, articles are
  % broken up into sections, subsections, subsubsections etc. while books are
  % broken up into chapters. Depending on the document class, we can break up
  % our document accordingly. For example, since we used the article class:
  \section{Intro}
  \section{Theory}
  \section{Methods}
  \section{Results}
  \section{Conclusion}
  \section{Acknowledgements}

  % Our template is finished, so we end the document
  \end{document}

That's a nice layout for a scientific article. A couple notes: by default, the
sections and subsections will be numbered: to suppress the numbering, you can
add a '*' to the section commands, like so:

.. code-block:: latex

  \section*{Intro}

Now what about content? The simplest thing to do would just be to add the 
content directly to the main *.tex* file. Using the last example:

.. code-block:: latex

  \section{Intro}
  Once upon a time, Seiji Ogawa discovered blood oxygen level dependent
  contrast...

This works just fine; however, another option is to but the latex source in a
separate file, and use another LaTeX command to add it to the main document.
For example, we could create a file called *intro.tex* that has the content for
the introduction in it and do the following:

.. code-block:: latex

  \section{Intro}
  \input{intro}

For non-trivial documents, this is the preferred method as it further separates
formatting from content (now the main *.tex* file deals with only the
layout of the document) and increases the reusability of the content.

**Math in LaTeX**

The rendering of mathematical equations and concepts is so central to LaTeX that
it has its own special syntax for doing so. I will not cover that syntax here,
but I do want to specify how to get into *math mode*. The simplest way is to
use '\$'. LaTeX will treat anything between two '\$'s as mathematical input:

.. code-block:: latex

  For example, if you want to render some math in the current line without any
  special breaks, you can do something like $\frac{1}{r**{2}}$

The single '\$' notation works for inline equations, allowing you to pop into 
the math environment in the middle of a line of text. If you want to make an
equation stand out, you can use two '\$\$' instead. Better yet, you can use the
*equation* environment and add a *\label* to reference that equation later:

.. code-block:: latex

  Here are arguably the most famous equivalancies in the history of physics

  \begin{equation}
  \label{newton2law}
  F = ma
  \end{equation}

  \begin{equation}
  \label{einstein}
  E = mc**2
  \end{equation}

There are many, many other things we could talk about, but with this basic
intro to environments, document structure, and math, you should be able to at
the very least navigate a LaTeX document.

Rest of Lab
+++++++++++
Work on your projects, with special emphasis on the draft to be handed in later
today.
