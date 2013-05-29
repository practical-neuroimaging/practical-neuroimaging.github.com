.. _git-homework:

############
Git homework
############

This should take you around 30 minutes.

Some of the time you'll be spending getting set up to have backups of your git
repositories; this is likely to be useful to you for a long time.

Try to get as far as you can.  If you get stuck, please, email me (Matthew) or
the list, and / or come to office hours on Thursday 2-4.

************
Introduction
************

Imagine we are all collaborating on some code.

I've put the current versions of these files somewhere, but there are some bugs.
You want to get the files, find the bugs, fix them, and then ask me to update
the original copies so we can all use the fixed versions.

Here is some practice - I've left a couple of small bugs in the code and I am
hoping you can find them, fix them, and give the fixes back to me, using git and
an online service for git repositories called github_.

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

* Log in to github using your (maybe new) username and password
* Go to the page with my copy of the repository:
  https://github.com/practical-neuroimaging/pna-utils
* Click on the "Fork" button near the top right of the page.  You want to fork
  to your own account
* After a while you should get dumped at your own "fork" of the ``pna-utils``
  repository, like this (for my github username):
  https://github.com/matthew-brett/pna-utils (your username will appear in the
  URL instead of ``matthew-brett``)

***********************************************
"Clone" your forked repository to your computer
***********************************************

A few lines down from the top of the page like
https://github.com/matthew-brett/pna-utils (with your username), you'll see the
URL to paste for doing a ``git clone``.  For me, the URL is:

    https://github.com/matthew-brett/pna-utils.git


So next do::

    cd ~/code
    git clone https://github.com/<your-github-username>/pna-utils.git

If you are on windows, use the git bash shell that got installed with git; on
OSX or Linux, just use the terminal.  Now you have the full copy of all the
history on your machine.

*********************
Find and fix the bugs
*********************

The problem the new code was designed to solve, was to run through the Haxby
dataset, and set the TR and the slice timing value into each image file.

The script to do this is ``fixup_openfmri.py``.  But:

There are two bugs I've left in the code.  One of them causes a test failure.
To find that one, first work out how to run the tests (hint : ``nosetests``).
Fix that one.  The other one makes the script fail if you call it.  Fix that one
too.

********************************
Make a new commit with the fixes
********************************

For each file that you change, when you've finished editing, do::

    git add <name_of_file>

Check what files you've changed with::

    git status

Check the changes you haven't added yet (not in the staging area) with::

    git diff

When you are done, do::

    git commit -m "Message about what you did"

When you do this, you make a new commit on the ``master`` branch.  More
explanation next class.

****************************************
Push the new commit back up to your fork
****************************************

Now you want to let me see the changes so I can add them back.  To do this, you
want to ``push`` your changes back up to github.  To do this::

    git push origin master --set-upstream

This pushes the new changes up to the ``master`` branch in your copy of the
repository on github.

If you've used the default "https" URL above (as I have) github will ask you for
your github username and password when you do this.

**********************
Ask me to fix my stuff
**********************

Now you've fixed the code, you want to share the fixes with everyone else.  So,
make a *pull request*. This is a request for me to take your changes and put
them into my repository.

* Go to the github page for your repo - e.g.
  https://github.com/matthew-brett/pna-utils
* Click on the "Pull request" button on the second from top line towards the
  right on this page.
* Notice that github automatically realizes you probably meant to ask me to add
  the changes because that's where you "forked" from originally.
* Fill in a title and some explanation of the changes
* Click "Send pull request"

Congratulations - you are now a member of the open-source community...

.. _github: http://github.com
