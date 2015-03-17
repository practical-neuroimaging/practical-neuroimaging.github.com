###################################
Script for git tutorial screencasts
###################################

These are the scripts I used for two short screencasts introducing git.

* https://vimeo.com/121579300
* https://vimeo.com/121579601

*****************************************
Script for introduction to git repository
*****************************************

* https://vimeo.com/121579300

In the terms of the `git parable`_, snapshot is the same thing as a commit.

`Our own version of the git parable
<http://practical-neuroimaging.github.io/git_parable.html>`_

::

    git config --global user.name "Matthew Brett"
    git config --global user.email "matthew.brett@gmail.com"

Change to home directory:

::

    cd ~

A git repository consists of a working directory (or working tree) with a
hidden subdirectory containing the files that git uses to store and track
snapshots.

First make the working directory::

    mkdir thrilling_paper
    cd thrilling paper

This is our working directory.

There are no files in the directory at the moment.

Let's start the paper::

    vim nobel_prize.txt

then::

    How the brain works
    -------------------

    It sends electrical messages around and that adds up to everything.

Let's make an analysis script as well::

    import random

    the_number = random.randint(0, 50)
    while the_number != 42:
        print("Oops, try again")
        the_number = random.randint(0, 50)

    print("The answer is", the_number)

Now let's say we're ready to start making snapshots with git.

First we make a git repository to store the snapshots and history::

    git init
    ls

The directory `.git` is hidden::

    ls -a
    ls .git

The directory has various things in it.

In fact we will find that the `refs` directory will store the bookmarks for
our branches and tags, and the `objects` directory will store our file and
directory snapshots.

We haven't taken any snapshots yet, so there is nothing in the objects
directory::

    ls .git/objects

    git status

Notice that the files are 'untracked'.  That means that git has never
previously taken a snapshot of these files, and so far assumes they should not
go into our snapshots.

As you remember from the git parable, before we do a snapshot, we first put
the stuff that will go into the snapshot, into the staging area.   We do that
with ``git add``.

Now let's add nobel_prize.txt to the staging area::

    git add nobel_prize.txt

What just happened?  First, we can see that a snapshot of `nobel_prize.txt` has
gone into the staging area::

    git status

Second, behind the scenes, git has made a copy of the file and put it into its
objects directory::

    ls .git/objects

The file has a filename that comes from its hash.  Don't worry about that for
now.  We can even get git to fetch this stored copy of `nobel_prize.txt` for
us, with git show.  Don't worry about the details of this command::

    git show :nobel_prize.txt

This is the snapshot of the file that has gone into the staging area.

If we now change the file in the working tree, it will be different from the
snapshot version.

Edit nobel_prize.txt::

    I have discovered the electrical impulses in the brain change when I think
    about being famous.

The copy of nobel_prize.txt in the working directory contains a new sentence.
But the snapshot stored copy is the same as it was when we took the snapshot::

    git show :nobel_prize.txt

Now what happens when I do a git status?::

    git status

The green shows the initial snapshot I did of this file, into the staging
area.  The red 'not staged for commit' shows that the file that is in the
working tree is different from the file in the staging area.  The redness of
the red text is warning me that I may want to update my copy in the staging
area.  I'll do that now::

    git add nobel_prize.txt

    git status

Notice that I now have two files in the objects directory - these correspond
to the first snapshot I made of ``nobel_prize.txt`` and the second that I just
made.  This reminds us that git is very careful to make use we don't
accidentally lose our backups.   Even though we probably don't care about the
first version of the file, git will keep it for us for a month or so, in the
'objects' directory, in case we want it.  Eventually though, git will do a
housekeeping clearout, and that backup will disappear, unless it is part of
any of the full snapshots (commits) that will come on to soon.

Now I will also add `analysis_script.txt`::

    git add analysis_script.txt
    git status

So now both files are in the staging area, and the versions in the staging
area are the same as the versions in the working tree.

Of course we now have another file in .git/objects because there is now a
snapshot of analysis_script there.

Notice that git tells us that that these changes in the staging area are ready
to be committed.

A commit, as we remember, is one recorded state of the working tree - a
snapshot of the working tree.

Let's do the commit.

I'm first going to do the commit as I would normally do it::

    git commit

Git opened my text editor for me and shows me some helpful information about
what is going into this commit.

I then type a message about this commit to remind me (and any else looking at
this later) what this commit is for.

Then git will save this message with the record of this snapshot, along with
my name and email address, from the configuration we did at the start of this
video.

But in this case, I'm not going to do what I normally do, and I'm going to
close this without saving.

I'm doing this so you can follow along.  When you first get started with git,
you may not have your favorite text editor set up to work with git, and so you
may get an error or some confusing text editor opening up to type the message.
You will then need to set up your text editor properly.  Google is your
friend.

So, just to show you how it works, if your text editor isn't set up right,
I'll use the `-m` flag to pass the message, so git doesn't open the editor::

    git commit -m "First snapshot of my files"

Git helpfully tells us what went into the snapshot.

Now I can look at the short history of the project::

    git log


************************************************
Script for video on git history and git branches
************************************************

* https://vimeo.com/121579601

The next step in understanding git is understanding how git connects commits
together with the commit parents, and how git stores branches and tags as
bookmarks.

First let's look at branches.

You can see from the commit message that git seems to be on a "branch" called
"master".

"master" is the default branch, the branch that git creates by default.

We can see which branch we are on using ``git branch``::

    git branch

At the moment we only have one branch "master"

As we saw in the git parable, a "branch" is just a label that points to a
particular snapshot.  Remember a snapshot is a "commit" in git terminology.

Remember that git log showed us the identifier for the commit - the commit
hash::

    git log

We can also see which commit the branch is pointing at by using the ``-v``
flag::

    git branch -v

As you can see the output tells us that the "master" branch is pointing to the
git commit that starts with 'd839074' - the same hash reported by git log.

In the git parable, we stored the branch positions in a text file, and git
does something very similar.  Git records the current position of each branch
in a tiny text file in the ``.git/refs/heads`` directory.  Here is the current
contents of ``.git/refs/heads/master`` - the current position of the master
branch::

    cat .git/refs/heads/master

As you can see it points to the commit (snapshot) hash we see in the output
from ``git log`` and from ``git branch -v``.

Now let's make a new commit.

I'll now make some edits to ``nobel_prize.txt``. First I delete the last
sentence.  Now I add::

    I am starting to feel famous while I write this paper.

I do git status to show me what has changed between the working tree and the
staging area::

    git status

Sure enough, the ``nobel_prize.txt`` paper has new changes that the staging
area does not know about.

Remember that the staging area always starts off the contents of the last
commit.

In fact, we can ask git to tell us exactly what changes there are in the
working tree, compared to the staging area, with the ``git diff`` command::

    git diff

Git diff only works well on simple text files like the files in our working
tree.  The new lines are in green with a plus.  Any deleted lines are in red
with a minus sign preceding.

OK - I am happy to add these changes to the staging area for the new commit::

    git add nobel_prize.txt
    git status

All seems ready.

Let's make the new commit::

    git commit -m "More inspiring thoughts"

Let's look at the history of our project now::

    git log

The project has two commits, the commit we have just done, and the first
commit.

The first line for each commit gives the SHA1 hash (unique identifier) for
this commit.

Our new commit points back to the first commit to record the history, that
our latest commit follows on from the first commit.

We can see that by using the ``--parents`` flag to git log::

    git log --parents

We still have the hash of our commit at the beginning of the first line.
After that, for our second commit, we have the "parent" of this commit.  The
parent is the first commit.  You can see the parent of the second commit is
the same as the hash for the first commit.  This is how git records the line
of history between the commits.

How about the branch?  Remember that the position of the branch should move
when we make a commit.  The branch position moves from pointing to the
previous commit, to point to the current commit.  As we remember, the current
commit is::

    git log

Here is the position of the 'master' branch now::

    git branch -v

You can see that the branch position has moved to point to the latest commit.

You won't be surprised to see that git stored this information in the
``.git/refs/heads/master`` file::

    cat .git/refs/heads/master

You now know most of the important things you need to know to understand git.

.. include:: links_names.inc
