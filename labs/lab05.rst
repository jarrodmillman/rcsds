*****
Lab 4
*****

Stats 159/259 - Lab 5 - 10/5/15

Agenda
++++++

1. Brief discussion of HW1 & qz2

   - Everybody check their grades

   - GitHub issue tracker for grading issues

   - Similarity analysis on reading1.txt

2. Markup Languages

   - What is a markup language?

   - Why are they important?

   - WYSIWYG vs. WYSIWYM and reproducibility

3. Individual/Group work

   - Project proposals (due tonight @ 9:00 PM)

   - `Your homework <http://www.jarrodmillman.com/rcsds/lectures/correlation_each_voxel.html>`_
     due before class tomorrow.

Homework 1
++++++++++

Similarity matrix grading demo --- push results and answer:

   - What is the word count for each reading?

   - What was the most frequently used word? What is the maximum number of 
     times it was used? The minimum?

   - How many times was the word "python" used?

Why we didn't want you to use numpy for hw1 - manual dot product vs. np.dot

Document Processing and Markup Languages
++++++++++++++++++++++++++++++++++++++++

  - Everybody's first document processor?

WYSIWYG - "What you see is what you get"
----------------------------------------

This is a good paradigm for artistic documents or simple documents where there
isn't much formatting. The major drawback of the WYSIWYG paradigm is that 
content and formatting are fused into one interface. This can be detrimental for
STEM pursuits, since publication and peer review is central to the scientific
process.

  - Wrestling with formatting is time consuming and irrelevant in the context
    of publication.

  - Feelings-ball take: having formatting in the same document as the content
    distracts from the true goals of the document; clearly and concisely 
    expressing ideas or results

  - Practical take: journals all have different formats. If a paper is being
    submitted to multiple places you don't want to have to explicitly 
    re-wrangle the document every time just to change the formatting.

  - Having content be separate from the formatting allows for much easier
    re-use of the content. 

      - e.g. you can post pictures from your publication to your website and 
        reuse your paper as a chapter in a thesis, or keep a portion for reuse
        in subsequent publications (e.g. acknowledgements)

Other major drawback of WYSIWYG editors from a reproducible/collaborative 
standpoint is their proprietary/binary formats.

  - Difficult to version control and collaborate on

  - Most document processing tools are trying to address this issue (e.g.
    google docs built-in VC and collaboration)


WYSIWYM - "What you see is what you mean"
----------------------------------------

The WYSIWYM paradigm inherently separates content from formatting. It is 
implemented by relying on **markup languages**. A markup language allows for 
generation of content in plain text, while also maintaining a set of special
syntax to annotate the content with structural information. In this way, the
plain-text or "source" files are human-readable and easy to version control. To
produce the final document, the source files must undergo a *build* or *render*
step where the markup syntax (and any associated style files) are passed to a
tool that knows how to interpret and render the content.

Examples of markup languages:

  - The big one: HTML (hyper text markup language). The markup language of the
    internet

  - XML: very popular for serialization

  - LaTeX: see below

  - markdown: very popular for document production. GitHub will automatically
    render markdown (NOTE: there are many different "flavors" of markdown; the
    GitHub flavor is quite popular)

  - reStructuredText: official recommended markup language for python
    doc strings. There are tools like `Sphinx <http://sphinx-doc.org/>`_ that
    will automatically build a documentation website for your python code
    based on the docstrings (also used for the class website!)

There are many examples of this paradigm, but **LaTeX** is by-far the most
ubiquitous in STEM (and all academia), largely due to its beautiful rendering
of math and the extensibility of the core by tons of open-source packages
(it also has a significant head-start over other WYSIWYM tools). We will be 
using LaTeX for your projects and discussing it in further detail during the
rest of the semester.

Work on projects or correlation exercise
++++++++++++++++++++++++++++++++++++++++
