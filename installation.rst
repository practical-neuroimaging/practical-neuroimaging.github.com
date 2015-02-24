.. _installation:

#################################
Software to install for the class
#################################

You will need Python and some Python scientific libraries installed.

************************
If you are using Windows
************************

Download and install Python and packages using Python (X,Y)
===========================================================

Go the the `Python(X,Y)`_ website. (If you happen to be following this course
from a country `blocked by Google code`_, download Python(X,Y from the
`Python(X,Y) UK mirror`_).

From the Google code website, click on the Downloads link to take you to the
Downloads page (https://code.google.com/p/pythonxy/wiki/Downloads).

Click on the link for the ConnectMV mirror (it appears to be in Canada, where
the other download links are in Europe).

Download the Python (X,Y) exe file, and double click to install.

Accept all the defaults.

.. _python-xy-pip:

Use pip to install the nibabel package
======================================

Open the ``cmd`` program program by clicking on the Windows Start button and
typing ``cmd`` (Return).

At the prompt, type::

    pip install nibabel

This will cause pip to install the ``nibabel`` package for reading
neuroimaging file formats.

Check the installation has worked
=================================

Download (right-click, save as) this Python script file to your computer:
https://nipy.bic.berkeley.edu/pna/check_pna_install.py

Open the cmd program again.  Change directory to the directory containing the
script file, e.g. ``cd Downloads``.

Run the script with::

    python check_pna_install.py

If you have any problems, follow the printed instructions after you run the
script, and let us know (see :ref:`installation-problems`).

Install git, the version control system
=======================================

Go to http://git-scm.com/

Click on the Downloads for Windows link at the bottom right.

Download the file they propose, with a filename something like
``Git-1.9.5-preview20141217.exe``.

Run the file to start the installation.

We suggest you accept the defaults, except the sceen called "Adjusting your
PATH environment", where we suggest you choose the option "Use git from the
Windows Command Prompt".

********************
If you are using OSX
********************

OSX ships with a version of Python that you will find in ``/usr/bin/python``.
For reasons `explained here
<https://github.com/MacPython/wiki/wiki/Which-Python>`_ you should use another
installation of Python for your own work.

Download and install Python
===========================

Download the latest version of Python 2 from `Python downloads
<https://www.python.org/downloads/>`_.  The current version at the time of
writing is Python 2.7.9.

Install in the usual way, by double clicking the installer, and following the
defaults.

Use pip to install the packages you need
========================================

Open the Terminal program by running ``Terminal.app`` (type command-space to
run spotlight or click on the spotlight icon and type ``terminal`` to find
this if you don't know where it is on your Mac).

At the Terminal.app prompt, type (or copy / paste)::

    pip install numpy scipy matplotlib pandas ipython[notebook,test] nibabel

This will cause pip to install the named packages, including the ``nibabel``
package for reading neuroimaging file formats.

Check the installation has worked
=================================

Download (right-click, save as) this Python script file to your computer:
https://nipy.bic.berkeley.edu/pna/check_pna_install.py

Open the Terminal.app again if it is not already open.  Change directory to
the directory containing the script file, e.g. ``cd Downloads``.

Run the script with::

    python2.7 check_pna_install.py

If you have any problems, follow the printed instructions after you run the
script, and let us know (see :ref:`installation-problems`).

Install git, the version control system
=======================================

If you are on OSX 10.9 (Mavericks) or above
-------------------------------------------

On Mavericks and above, ``git`` comes with the Apple OSX command line tools.

To get these, type ``git`` at the terminal command line.  If git is not
installed already you will get a dialog box like this:

.. image:: images/git_developer_tools.png

Click 'install' to install the OSX developer command line tools, including
git.

If you are on OSX 10.8 (Mountain lion) or below
-----------------------------------------------

Install git from this `git OSX installer`_ page by doing the usual routine of
double clicking the ``.dmg`` file then double-clicking the ``.pkg`` installer.
Check the installation has worked by closing Terminal.app and opening again,
and typing ``git`` at the command line.

The reason we suggest using this installer rather than the more standard git
Snow Leopard ``.dmg`` installer from
http://sourceforge.net/projects/git-osx-installer/files is that `some people
<http://gitforums.org/forum/main-category/main-forum/1264-illegal-instruction-4-when-running-git-on-osx-10-7-5>`_
have reported ``Illegal instruction: 4`` errors when trying to run git from
this standard installer.  Thanks to Ana Navarro Cebrian for tracking this
down.

**********************
If you are using Linux
**********************

If you are using recent Ubuntu or Debian, try the following commands::

    sudo apt-get update
    sudo apt-get install -y python-pip
    sudo apt-get install -y python-dev
    sudo apt-get install -y python-matplotlib
    sudo apt-get install -y python-scipy python-nose python-pandas
    sudo pip install -U pip
    sudo pip install nibabel
    sudo pip install -U ipython[notebook]
    sudo apt-get install -y git

On Fedora or related distros::

    sudo yum install -y make gcc-c++
    sudo yum install -y python-pip
    sudo yum install -y python-ipython-notebook python-matplotlib
    sudo yum install -y python-scipy python-nose python-pandas
    sudo pip install -U pip
    sudo pip install nibabel
    sudo pip install -U ipython[notebook]
    sudo yum install -y git

Check the installation with::

    wget https://nipy.bic.berkeley.edu/pna/check_pna_install.py
    python check_pna_install.py

If you have any problems, follow the printed instructions after you run the
script, and let us know (see :ref:`installation-problems`).

*****************************************************************
If you have already have Python from Anaconda or Enthought Canopy
*****************************************************************

If you already have some large Python packaging system installed, such as the
`Anaconda`, `Enthought Canopy`_ or `Python(X,Y)`_, you will need to install
one extra package - nibabel_.  If you are using Python(X,Y) then go to the
:ref:`python-xy-pip` section for instructions.  Otherwise, please read on.

First make sure you have pip_ (the Python package manager) installed on your
system, by typing pip_ from the command line.  You should see the help for
pip.  Then install nibabel with::

    pip install nibabel

Download (right-click, save as) this Python script file to your computer:
https://nipy.bic.berkeley.edu/pna/check_pna_install.py

Finally, check your installation by opening your command line application,
changing into the directory containing the ``check_pna_install.py`` script,
and running the following command::

    python check_pna_install.py

If you have any problems, follow the printed instructions after you run the
script, and let us know (see :ref:`installation-problems`).

******************************************************
If you don't want to do an install on your machine yet
******************************************************

If you don't want to do this install, or you want to get a feel for the classes
before you commit to the install, or you have missed a few classes and want to
get going with something while you catch up, we also have a virtual machine that
you can download.

The virtual machine is a full version of Linux, provided by our friends at
`NeuroDebian`_.  We have installed all the software you need to get started on
this Linux machine.

We strongly recommend you do install the software on your own computer rather
than using the virtual machine.  A large part of the course is about getting
comfortable with your tools, and this is always harder if you are using a
different system for the course than you use for your other work.

If you do want to use the virtual machine, you can run it using VirtualBox_.

First download the virtual machine image from
http://nipy.bic.berkeley.edu/pna/pna2015.ova.  The file is about 3 gigabytes
large.

Next, install VirtualBox_ on your own machine.

Finally, open the VirtualBox application, and import the ``pna2015.ova`` image
by following `these instructions
<http://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html>`_.

Now start your new virtual machine by selecting the new NeuroDebian virtual
machine and pressing the *Start* button.

In due course virtualbox will open a Linux (Debian) machine desktop with all the
course software installed.

.. _installation-problems:

*********************
Installation problems
*********************

Any problems at all, please come see us in :ref:`office-hours`, or email:

* matthew dot brett at gmail dot com
* jbpoline at gmail.com
* sjvdwalt at gmail dot com

.. include:: links_names.inc
