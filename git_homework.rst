############
Git homework
############

This should take you about 30 minutes.

Most of this time will probably be looking things up on the web.

Some of the time you'll be spending getting set up to have backups of your git
repositories; this is likely to be useful to you for a long time.

************
Introduction
************

Imagine we are all collaborating on some code.
I've put the current versions of these files somewhere, but there are some bugs.
You want to get the files, find the bugs, fix them, and then ask me to update
the original copies so we can all use the fixed versions.

********
Clean up
********

Start by deleting the versions of the files you have already, if you have them.
For OSX or Linux::

    cd ~/code
    rm -rf datacheck

For Windows Powershell::

    cd ~\code
    rm -r -Force datacheck

*********************
Make a Github account
*********************

(You can skip this step if you already have a github account).

Github_ is a popular site for free hosting of git repositories.

You first need to make a (free) account on the github service.

Click on the "Sign up for free" button and follow the instructions.

**************
Set up for git
**************

Now check the github page on `configuring git for
github<https://help.github.com/articles/set-up-git>`_ and follow the
instructions there.

You might want to check your favorite editor is working properly - see
:ref:`git-editor-setup`.

**************************
"Fork" the main repository
**************************

This will make your own personal public copy of the main github repository.  The
copy is on the github servers.

Go to the page with my copy of the repository:





.. _github: http://github.com
