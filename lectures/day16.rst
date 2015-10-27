******
Day 16
******

Announcements
-------------

- Presentations will be 5 minutes per group on Thursday, November 12
- Focus will shift to projects
- Will table the PCA and linear algebra discussion for now
- BIC tour on Monday, November 23

Lesson plan
-----------

- Continuous integration and coverage testing
- Makefiles
- Slides via `pandoc`
- IPython notebooks are fine to use as you set things up, but I won't look at them
- Code submissions via pull requests
- Pull requests should have at least three participants
- If you have questions, there should be a pull request and use
  `@jarrodmillman`, `@matthew-brett`, and/or `@rossbar`
- Most of your code should be written as a collection of functions
  with tests, then use script calling these functions to perform
  your analysis

New files
---------

::

    $ tree 
    .
    ├── code
    │   ├── Makefile
    │   └── utils
    │       ├── __init__.py
    │       ├── pearson.py
    │       └── tests
    │           ├── __init__.py
    │           ├── test_pearson_1d.py
    │           └── test_pearson_2d.py
    ├── .coveragerc
    ├── data
    │   ├── data.py
    │   ├── .gitignore
    │   ├── __init__.py
    │   ├── Makefile
    │   └── tests
    │       ├── __init__.py
    │       └── test_data.py
    ├── .gitignore
    ├── Makefile
    ├── requirements.txt
    ├── slides
    │   ├── .gitignore
    │   ├── Makefile
    │   ├── progress.md
    │   └── README.md
    ├── tools
    │   └── travis_tools.sh
    └── .travis.yml

Task
----

(Remember to add new code via pull-requests.)

- Add TravisCI and Coveralls.io buttons to your README.md
- Make sure your tests pass, add a new test
