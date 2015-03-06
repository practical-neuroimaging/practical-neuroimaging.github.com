####################################
Day 2: images as arrays and plotting
####################################

2 / 27 / 2015

.. The students have not so far covered:

    dicts, tuples;
    functions;
    list comprehensions;
    string slicing (apart from minor intro on first day);
    modules and scripts;
    any numpy, scipy, matplotlib.

*****
Prior
*****

These two tutorial pages are from the `scipy lecture notes`_:

* The `numpy array object`_
* `Array operations`_

***
Day
***

Installing scikit-image
=======================

You might want to install scikit-image |--| the image processing toolkit for
Python.  You will need it for the last (and optional) part of the last
exercise today.

* If you have Anaconda, the package is already installed;
* If you have Python(X,Y) on Windows, download and run
  http://nipy.bic.berkeley.edu/pna/archives/scikits.image-0.10.1-7_py27.exe;
* If you have OSX, and do not have Anaconda (for example, if you followed the
  instructions for OSX install for this class) then::

    pip install -U scikit-image

* If you have Linux, first |--| ask your friendly instructor, because Linux
  systems differ more from each other than OSX and Windows.  If we aren't
  around for some reason, then:

    * If you are on Ubuntu or Debian 64-bit, try::

        sudo pip install --no-index -f http://travis-wheels.scikit-image.org scikit-image

    * Otherwise, or if that doesn't work::

        sudo pip install -U six
        sudo pip install -U scikit-image

  As usual, if you have any problems, we are very happy to help.

Introduction to day 2
=====================

To get started
--------------

::

    cd pna2015
    git pull
    cd day2
    ipython notebook

Some new Python stuff
---------------------

* Tuples are immutable lists;
* Mutable and immutable in Python;
* Making a tuple with a single element;
* List comprehensions are short-cut for loops.

Revision from homework
----------------------

* Numpy is a package (and a module);
* Getting help with dot <tab> in IPython and ``np.lookfor``;
* Matplotlib is a package (and a module);
* Showing an array as an image with `imshow`;
* Plotting a line from an array with `plot`;
* Slicing arrays;
* Indexing arrays with masks;
* Numerical operations in numpy;
* ``+ - * / == != > < >= <=`` are always elementwise;
* Transpose
* Reshape

Some useful background resources
--------------------------------

* What is an image? e.g.
  http://nbviewer.ipython.org/urls/bitbucket.org/matthewbrett/talks/raw/master/processing_i/what_is_an_image.ipynb

.. To cover
    Numpy allows creation of arrays
    An image is an array
    An array can be displayed with matplotlib
    An array can be reshaped
    An array can be transposed
    A 3D image is a 3D array
    A 3D array can be reshaped to 1D and back again
    Histograms.
    Operations on 1D (implicit) - mean, min, max
    Operations over axes (explicit) - mean, min, max
    np.lookfor
    Setting the colormap

.. include:: links_names.inc
