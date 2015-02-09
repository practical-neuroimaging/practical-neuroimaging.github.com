.. _installation:

#################################
Software to install for the class
#################################

* A text editor to edit python code - see :ref:`choosing-editor`
* Python and the Python scientific libraries installed - see below.

If you already have some large Python packaging system installed, such as the
`Enthought Python Distribution`_, you can stick with that, it should provide the
dependencies you need.  To make sure, see :ref:`check-installation`. If you
don't have something like that (most of you won't), please read on...

************************
If you are using Windows
************************

It is not very difficult to install on Windows, but I've written more verbose
instructions on Windows because the installation is more unfamiliar to Windows
users than OSX or Linux users.

Download and install Python
===========================

Download the latest version of Python 3 from `Python downloads
<https://www.python.org/downloads/>`_.  The current version at the time of
writing is Python 3.4.2.

The default download is the 32-bit version.  This works on any copy of
Windows.  If you click on the "Downloads" link and then the "Windows" link,
you will see other downloads for Windows.  Here you can choose the 64-bit
installer if you prefer; either will work for the course.

Run the installer.  When you get the set of install options, scroll down to
the end, where you will see a currently disabled option to put Python on the
Windows path. Enable this and continue the install using all the defaults.

You now should have Python installed, and a new folder on your ``C:\`` drive
``C:\Python34``.

Check that the Python command is on your path
=============================================

Open the ``cmd`` Windows shell (click on the Start button, type ``cmd``, press
return).  Type ``python`` (then return) at the command prompt to confirm that
Python is on your Windows path.  If it is not, run this command from the cmd
shell::

    setx PATH "%PATH%;C:\Python34;C:\Python34\Scripts"

then close the cmd shell and start it again to check you can now run
``python`` from the cmd prompt.

Upgrade the Python package manager, pip
=======================================

You now need to upgrade the Python package manager, ``pip``.

Go to the `pip installation page
<https://pip.pypa.io/en/latest/installing.html>`_.

Download (right click, save as) the ``get-pip.py`` Python script from the link
on that page.

Open up the Windows cmd shell (click the Start menu, type ``cmd``, press
Return).

Change directory to the directory you downloaded ``get-pip.py`` - e.g. (in
cmd): ``cd Downloads``.

Use Python to run the ``get-pip.py`` script, as in (cmd shell again)::

    python get-pip.py

Check you have the right pip version with (cmd shell)::

    pip --version

This should give you a version >= 6.0.8. If not, come to use at office hours
to sort it out for you.

Use pip to install the packages for the course
==============================================

Open the ``cmd`` program again. At the prompt, type::

    pip install -r https://nipy.bic.berkeley.edu/pna/pna_requirements.txt

This will cause pip to read the file at the given URL, identify the packages
you will need, and download, install them.  The installation will take several
minutes, longer if you are on a slow internet connection.

Check the installation has worked
=================================

Download (right-click, save as) this Python script file to your computer:
https://nipy.bic.berkeley.edu/pna/check_pna_install.py

Open the cmd shell.  Change directory to the directory containing the script
file, e.g. ``cd Downloads``.

Run the script with::

    python check_pna_install.py

If you have any problems, follow the printed instructions after you run the
script, and let us know.

Install git, the version control system
=======================================

Go to http://git-scm.com/

Click on the Downloads for Windows link at the bottom right.

Download the file they propose, with a filename something like
``Git-1.9.5-previeww20141217.exe``.

Run the file to start the installation.

I suggest you accept the defaults, except the sceen called "Adjusting your
PATH environment", where I suggest you choose the option "Use git from the
Windows Command Prompt".

********************
If you are using OSX
********************

Download and install Python
===========================

Download the latest version of Python 3 from `Python downloads
<https://www.python.org/downloads/>`_.  The current version at the time of
writing is Python 3.4.2.

Install in the usual way, by double clicking the installer, and following the
defaults.

Now open a terminal by running ``Terminal.app`` (command-space, to run
spotlight and type ``terminal`` to find this if you don't know where it is on
your Mac).

Check that the Python3 command is on your Path
==============================================

Check you have the right version of Python by typing ``which python3``
(Return) at the terminal.  Note the ``3`` at the end of ``python3``.  You
should get something like ``/usr/local/bin/python3``.  If not, let us know.

Check you have ``pip``, the Python package manager, by typing ``pip`` at the
terminal prompt.  You should get the help for ``pip``.  If not, let us know.

Use pip to install the packages for the course
==============================================

Install the packages you need with the following command from the terminal::

    pip install -r https://nipy.bic.berkeley.edu/pna/pna_requirements.txt

Check the installation has worked
=================================

Download (right-click, save as) this Python script file to your computer:
https://nipy.bic.berkeley.edu/pna/check_pna_install.py

Open the terminal again if it is not already open.  Change directory to the
directory containing the script file, e.g. ``cd Downloads``.

Run the script with::

    python3 check_pna_install.py

If you have any problems, follow the printed instructions after you run the
script, and let us know.

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

Install git from the `Git snow-leopard installer
<http://sourceforge.net/projects/git-osx-installer/files/git-2.2.1-intel-universal-snow-leopard.dmg/download>`_
by doing the usual routine of double clicking the ``.dmg`` file then
double-clicking the ``.pkg`` installer.  Check the installation has worked by
closing Terminal.app and opening again, and typing ``git`` at the command
line.

**********************
If you are using Linux
**********************

If you are using recent Ubuntu or Debian, please set up `NeuroDebian`_ using
the instructions on the NeuroDebian website.  Then::

    sudo apt-get install ipython3-notebook python3-matplotlib python3-pillow
    sudo apt-get install python3-scipy python3-nose
    sudo apt-get install python3-pandas
    sudo apt-get install python3-skimage
    sudo apt-get install python3-pip
    sudo pip3 install nibabel sympy
    sudo pip3 install statsmodels
    sudo pip3 install numexpr
    sudo pip3 install scikit-learn
    sudo pip3 install scikit-image
    sudo pip3 install dipy
    sudo pip3 install -U ipython[notebook]
    sudo apt-get install git

    sudo apt-get install ipython-notebook python-matplotlib python-pillow
    sudo apt-get install python-scipy python-nose
    sudo apt-get install python-pandas
    sudo apt-get install python-skimage
    sudo apt-get install python-pip
    sudo pip install nibabel sympy
    sudo pip install statsmodels
    sudo pip install numexpr
    sudo pip install scikit-learn
    sudo pip install scikit-image
    sudo pip install dipy
    sudo pip install -U ipython[notebook]
    sudo apt-get install git

On Fedora or related distros::

    sudo yum install python3-ipython-notebook python3-matplotlib python3-pillow
    sudo yum install python3-scipy python3-nose
    sudo yum install python3-scikit-image
    sudo yum install python3-scikit-learn
    sudo yum install make gcc-c++
    sudo yum install python3-pip
    sudo pip-python3 install nibabel sympy
    sudo pip-python3 install statsmodels
    sudo pip-python3 install numexpr
    sudo pip-python3 install scikit-learn
    sudo pip-python3 install scikit-image
    sudo pip-python3 install dipy
    sudo pip-python3 install -U ipython[notebook]
    sudo yum install git

Check the installation with::

    curl -O https://nipy.bic.berkeley.edu/pna/check_pna_install.py
    python3 check_pna_install.py

*********************
Installation problems
*********************

Any problems at all, please come see us in :ref:`office-hours`, or email:

* matthew dot brett at gmail dot com
* jbpoline at gmail.com
* sjvdwalt at gmail dot com

.. include:: links_names.inc
