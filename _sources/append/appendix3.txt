Shell Customization
===================

There will come a time when some modification of the shell
environment will be desired. Fortunately, in bash this is very
easily done.

**Table C-1. Bash Configuration File**

===================   =========================
File                  Description
===================   =========================
*/etc/profile*        System login environment
*/etc/bashrc*         System environment
*~/. bash\_profile*   User login environment
*~/. bashrc*          User environment
*~/. bash\_logout*    User logout script
===================   =========================

If no .bash\_profile, then .bash\_login, then, profile.  

::

  # global airc binaries
  if [ "$UID" != "0" ]; then
    export FSLDIR=/usr/fmri/lib64/fsl/4.1.4
    export PATH=$PATH:/usr/fmri/bin:/usr/fmri/bin/afni:/usr/fmri/bin/caret/bin_linux:/usr/fmri/lib64/matlab/2007a/bin:${FSLDIR}/bin
    export FREESURFER_HOME=/usr/fmri/lib64/freesurfer/4.4.0
    source $FREESURFER_HOME/SetUpFreeSurfer.sh > /dev/null
    source ${FSLDIR}/etc/fslconf/fsl.sh
  
    alias matlab-spm2='(PATH=/usr/fmri/lib/matlab/2007a/bin:$PATH ; matlab -nojvm -arch=glnx86)'
  fi

**Table C-2. Prompt String Customization**


========  =========================================================
Command   Meaning
========  =========================================================
*\\d*      The date in "Weekday Month Day" format
*\\H*      The hostname
*\\h*      The hostname up to the firlst "."
*\\n*      A carriage return and line feed
*\\T*      The current time in 12-hour HH:MM:SS format
*\\t*      The current time in HH:MM:SS format
*\\@*      The current time in 12-hour am/pm format
*\\u*      The username of the current user
*\\w*      The current working directory
*\\W*      The basename of the current working directory
*\\#*      The command number of the current command
*\\!*      The history number of the current command
*\\$*      If the effective UID is 0 print a #, otherwise print a $
*\\\\*     Print a backslash
========  =========================================================


.. Tip::  Don't use editor, use :ref:`command-echo`  and command editing
