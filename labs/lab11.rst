******
Lab 11
******

Stats 159/259 - Lab 11 - 11/16/15

Agenda
++++++

1. Organize groups for "field trip" to fMRI lab next Monday

2. Git tips 'n tricks

3. Quick discussion of a couple python packages

   - Pandas

   - Scikit-learn

4. Project work

Field Trip
++++++++++

 - Two groups: 11-12PM and 12-1PM.

 - Need a 50/50 split so some people from the afternoon lab will have to move
   to the 11-12 slot

Making Collaboration and Git Easier
+++++++++++++++++++++++++++++++++++

Many of you identified git and, more generally, collaborating as one of the 
primary challenges for your projects. In light of that feedback, I wanted to
cover a few git topics. First, several groups mentioned that they were using
facebook chat to communicate or were otherwise having trouble getting everyone
in the same room at one time. There are a couple tools you should be aware of
that could help with the general communication issues:

 - `Slack <https://slack.com/>`_ is a popular messaging/organization app for
   team-based projects. If you are having trouble getting everyone on the same
   chat (not everyone uses facebook) or your schedules are such that it's very
   challenging to meet in person as often as you'd like to, you may want to 
   investigate this tool

 - `Gitter <https://gitter.im/>`_ is another popular messaging app for 
   github-based coding projects. One of the things that's really nice about it
   is it integrates with GitHub (for instance you can add a button to your
   README.md to link to your gitter page, just like you do for TravisCI and 
   coverage). Again, if you're having trouble with real-time communication as 
   a group, this might be a tool worth investigating.

Now, on to things specific to git. Let's start with a few quick and easy things
to make life easier:

 - git_ps1: Info about your repos in the bash prompt

 - git alias: just like bash alias - can make "shortcuts" for commands you 
   might use frequently, e.g.

   - git unstage

   - git hist

The scripts I use to configure my Linux environment contain specific examples
for these two topics: `https://github.com/rossbar/UbuntuInstallScripts`_;
specifically the bash_color and configure_git scripts.

GitHub is loaded with scripts that people use to configure their computing
environment, so if you don't like these ones, feel free to try to find others
by searching GitHub.

**Undoing things in git -- git reset**

Many people have had questions both in lab and office hours relating to how do
you *undo* things in git. There is a 
`whole section <https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things>`_ on
this topic in the pro git book. 

As an aside, if you are planning on continuing computational work and using git,
I very strongly recommend you take the time to read the 
`pro git <https://git-scm.com/book/en/v2>`_ book. It's free online, and is where
I learned 90% of the things that I know about git.

Back to undoing things... Let's follow along with a section in the pro git book:
`reset demystified <https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified>`_.

Python Packages you've Expressed Interest In
++++++++++++++++++++++++++++++++++++++++++++

From the feedback in your presentations, there were a couple packages that 
teams expressed interest in and I figured I'd just touch on them here. First:

**Pandas**

Pandas is a library that intends to make working with data easier. At it's core,
it's really nothing more than a high-level wrapper over numpy arrays. That's not
to say it isn't useful however! I've only used pandas sparingly as I prefer to
work with numpy arrays directly, but from my experience, one of the biggest 
advantages of using pandas is it's ability to deal with imperfect, typed data
with relative ease. For example, if you have multi-field data where each value
in a row has a specific meaning (for example, col1 = timestamp, col2 = stock
price, col3 = purchases/hour), the pandas *dataframe* object handles this data
well. Of course, you can deal with data like this in numpy as well with 
np.dtype, but the real advantage of pandas comes in the ability to add fields
(for example, say you wanted to add a col4 that represented the temperature)
and for dealing with missing or irregular data.

In my opinion, you're much better off using pure numpy arrays for dealing with
the fMRI data as it is largely numerical in nature.

**scikit-learn**

Many groups have asked/started using scikit-learn. The scikit-learn library has
many, many tools for both supervised and unsupervised learning, including a ton
of built-in tools for regression and classification.

For your projects, you may be interested in some of the 
`regression tools <http://scikit-learn.org/stable/modules/linear_model.html>`_.
Let's get your feet wet with a super simple exercise.

scikit-learn exercise
+++++++++++++++++++++

 - Load the "digits" dataset that comes with scikit learn

 - Use imshow to visualize a couple of images from the digits dataset. Can you
   tell what numbers they represent? (use the "target" array to check your
   answer).

 - Use the train_test_split() helper function from sklearn to split the digits
   dataset into a training and test set. Use 2/3 of the dataset to train on.

 - Once you've trained your classifier, use it's .predict() method to look at a
   couple specific examples in your test set.

 - Use the .score() method of your classifier to see how well it performs on the
   entire test set.

In all, this example should take very few lines of code, but your classifier
may not be very good. At this point, if you are interested, you can continue
following through scikit-learn examples to improve your classifier. For 
instance, you may be interested in using 

Project work
++++++++++++
As of your presentations, several groups seemed to have a good start on 
preprocessing their data, but with the exception of a couple of groups, there
was very little in the way of preliminary analysis. We will have more specific
feedback Tuesday in class, but the general theme is: get going with your
analyses!
