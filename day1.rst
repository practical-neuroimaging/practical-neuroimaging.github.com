##########################
Day one : 22 February 2013
##########################

************
Introduction
************

Two different modes of working:

* interactive
* building code

Today is interactive. As before we'll be using the `IPython notebook`_.

Next week we'll be building code.

The idea of software carpentry:

* Learning how to use tools.
* Homework for this week: editors.

See :ref:`choosing-editor` for a review of some choices.

**********************
The Python environment
**********************

* Python itself comes with many useful modules in the `Python standard library`_
    * ``os, sys, shutil, glob, tempfile``
    * ``urllib2``, ``HTMLParser``, ``xml``, many other web libraries
    * ``math, decimal`` (very high precision numbers), ``random``
    * ``csv``, database access with ``sqlite3`` and others
    * ``tarfile, zipfile, gzip`` and other compression formats

  Along with debugging, documentation tools, testing tools and much else.

* Numpy_ is a Python library defining arrays of data, with many routines for
  manipulating arrays including basic linear algebra, random number generation
  and Fourier transforms.  Python + Numpy gets you most of what MATLAB can do.

* Scipy_ adds a large library of scientific code built on top of Numpy.
  Including:

    * ``scipy.io``: Read / write of scientific data formats including MATLAB ``.mat`` files
    * ``scipy.ndimage``: processing tools such as smoothing and convolution
    * ``scipy.linalg``: expanded linear algebra tools with interfaces to much of
      the highly optimized LAPACK linear algebra libraries.
    * ``scipy.optimize``: tools for finding optimum values in functions

  Please see the `scipy reference guide`_ for more detail.

* Matplotlib_ provides 2D and some 3D plotting, with an interface modeled after
  MATLAB. See the `matplotlib gallery`_ for a taster of the kind of things you
  can do.

* Cython_: write Python code but with the ability to optimize and compile it
  down to the C level, often giving very large increases in execution speed.

* Sympy_: a library for symbolic mathematics such as defining and solving equations.

* Pandas_: high-level fast data analysis using R-like data frames to hold and
  manipulate data

* scikit-learn_: an extensive machine learning library

* scikit-image_: 2D image processing

* statsmodels_: statistical models

There are many other libraries, including some specific to neuroimaging.  We'll
meet one of those next week, nibabel_.

********************
The Python libraries
********************

* `The Python libraries raw
  <https://raw.github.com/practical-neuroimaging/pna-notebooks/master/python_libraries.ipynb>`_
  notebook file for downloading.
* `The Python libraries web
  <http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/python_libraries.ipynb>`_
  notebook presented nicely as a web page.

**********************
Introduction to python
**********************

Continuing on from last week:

* `Introduction to Python raw
  <https://raw.github.com/practical-neuroimaging/pna-notebooks/master/introduction_to_python.ipynb>`_
  notebook file for downloading.
* `Introduction to Python web
  <http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/introduction_to_python.ipynb>`_
  notebook presented nicely as a web page.

.. include:: links_names.inc
