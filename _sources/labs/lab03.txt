*****
Lab 3
*****

Lesson Plan - Stats 159/259 - Lab 3 - 9/21/15

Agenda
++++++

1. Working with git remotes

2. A couple python notes

   - modules \& \_\_name\_\_

   - High-level vs. low-level - what does this mean and how does it work? 

3. Working on HW 1

4. Before class on Tuesday:
   `NumPy Lock 'n Load <http://mentat.za.net/numpy/intro/intro.html>`_.

Working with (git) Remotes
++++++++++++++++++++++++++

 - What are the two ways to set up a project to work on in git?

 - `git clone` is like an `git init` + `git pull` + `git remote add`

 - Git workflows: forking, cloning, push/pull permissions with remotes.

    - **Centralized model**
      Often used for small (potentially private) projects
      where all the collaborators know each other. A single central repo is used
      as the "main" repo and every collaborator has read/write (i.e. pull/push)
      access to the main repo.

      .. figure:: ../figs/centralized_collab_model.png
         :align: center
         :width: 100%

         A simple cartoon of the centralized collaboration model. For more
         information, see the ProGit book `section 5.1`_.

    - **Integration-manager model**
      This collaboration model takes full advantage of the distributed nature
      of git. It is a very common model for contributing to open-source 
      projects ranging in size from very small (100's of lines) to very large
      (10's of thousands of lines). In this model, everyone has read (pull)
      access to the main project repository, but only a few people (called
      integration-managers, or sometimes lieutenants) have write (push)access.
      Any (potential) collaborator may pull down a local copy of the project
      and contribute locally. They can also `fork` to create their own remote
      copy of the repository that they can push to. However, to get your 
      contributions into the "main" (or "blessed") repository, you have to 
      **request** that one of the integration managers **pull** your changes
      into the blessed repo. This is where the concept of a *pull request*
      comes from.

      .. figure:: ../figs/integration_manager_model.png
         :align: center
         :width: 100%

         A simple cartoon of the integration-manager collaboration model. For
         more information, see the ProGit book `section 5.1`_.

.. _section 5.1 : https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows


Python Pontification
++++++++++++++++++++

 - Reading 3 stressed python's "high-level syntax with low-level capability".
   Many of you latched on to this concept, but it seems there may have been some
   confusion as to what this means. To start, let's take a look at what python
   actually is by looking at its `source code <https://github.com/python/cpython>`_.

 - Don't worry! You aren't expected to understand the source or know anything
   about it. However, looking at it should emphasize a couple things:

    - An example (in all it's gory detail) of what it means to be "open source"

    - More importantly, this is in large part how python gives programmers
      access to "low-level capabilities" - The interpreter itself is written
      in a "low-level" language: C! This is also contributes to python's 
      description as a "glue language" - it is possible for developers to use
      various tools (e.g. cython, SWIG, ctypes, other API's) to build wrappers
      around or bridges to code that was written in other languages.

 - Quick demo on scope: what is \_\_name\_\_?

   - Python objects' special attributes: *dunders*

Work on HW 1 or Numpy Lock N' Load
++++++++++++++++++++++++++++++++++
