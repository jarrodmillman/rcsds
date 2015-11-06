******
Day 21
******

Announcements
-------------

- Presentations will be 5 minutes per group on Thursday, November 12 (i.e., 1 week from today)
- Draft reports (~6 pages) due on Thursday, November 12 at 21:00
- Quiz on Monday, November 9 will cover hw2 material, scope, plotting, basic linear modeling as covered in Matthew's lectures, basic Git workflow, and possibly some general questions about hypothesis testing.
- BIC tour on Monday, November 23 (during lab time)

Links
-----

Technical writing

- `Technical writing slides <http://www.jarrodmillman.com/rcsds/notes/TechnicalWritingLecture.pdf>`_
- `Appendix to “Stat Labs” by Deb Nolan and Terry Speed  <http://www.jarrodmillman.com/rcsds/notes/StatLabsAppendix.pdf>`_
- `Halmos' “How to write mathematics” <http://www.jarrodmillman.com/rcsds/notes/halmos_1970_howto-write-mathematics.pdf>`_
- `Knuth et al. “Mathematical Writing” <http://www.jarrodmillman.com/rcsds/notes/knuth_mathematical_writing.pdf>`_

Tentative final project rubric

- `Rubric <http://www.jarrodmillman.com/rcsds/notes/rubric.pdf>`_


Reports and presentations
-------------------------

"Seek simplicity, and distrust it."  --- Alfred North Whitehead

#. Briefly describe data (~30s)

   - Paper
   - dsnum from openfmri.org
   - What kind of data is it?

#. Briefly describe what you've done so far (~30s)

   - data fetching/preprocessing
   - initial analysis
   - plots? figures?

#. What is your plan? (~3m)

   - What analysis will you perform?
   - How does it relate to the original data analysis?

     - Will you use all the data?  Why or why not?
     - What model/preprocessing steps will you simplify?

   - What are the problems you face?

     - Try to be explicit about your issues?
     - Suggest potential solutions and/or approaches.
     - What do you need to research more?  Have you found sources?
     - Will you try to make "inferences" from the data?

       - How will you deal with multiple comparisons?
       - How will you attempt to validate your model?     

#. Process (~1m)

   - What was the hardest part of the process so far?

     - Git workflow, Python, fMRI data, all of the above
     - Having an ill-defined assignment?

   - How successful have you been at overcoming these obstacles?
   - What issues have you faced working as a team?  How have you
     been addressing them?
   - What parts of the class have been the most useful?
   - What parts have been the least helpful or most confusing?
   - What do you need to do to successfully complete the project?
   - How difficult are you finding it to make your work reproducible?
     Do you feel confident that you are in a position to make your
     projects reproducible?
   - What would be most helpful for your team in the remaining
     weeks?  Additional lectures?  Structured or unstructured
     group work?
   - What potential topics would be most useful for us to cover?

     - Overview of brain / neuroanatomy?
     - More linear regression (ANOVA)? PCA? The mathematics or the implementation?
     - Machine learning (classification, prediction, cross-validation)?
     - Permutation tests (and maybe bootstrap)?
     - Software tools (Git, Make, Python, statmodels, etc.)
     - Technical writing and scientific visualization?
     - Advanced topics (regularized regression, selective inference)?


Remember
--------

- If you have questions about your projects, there should be a pull request with code
  or text and use `@jarrodmillman`, `@matthew-brett`, `@rossbar`, 
  and\or `@jbpoline`
- Most of your code should be written as a collection of functions
  with tests, then use scripts calling these functions to perform
  your analysis
