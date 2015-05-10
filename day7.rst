#####################################################
Day 7: diagnostics using principal component analysis
#####################################################

4 / 10 / 2015

This class is for us to get an idea of the variation in the FMRI data, and to
start working with images as matrices. We will do this using `principal
component analysis`_ (PCA).

*******
Reading
*******

In the class we will cover what PCA is and how it works.

For this explanation we need some basic ideas from linear algebra, and in
particular, the idea of projecting a vector onto another vector using the dot
product.  This background will also be useful to us later in thinking about
regressors and statistical models.

So the "readings" for this week are some excellent Khan academy videos on
linear algebra.

Basic background on dot products
================================

* `Vector dot product and vector length
  <https://www.khanacademy.org/math/linear-algebra/vectors_and_spaces/dot_cross_products/v/vector-dot-product-and-vector-length>`_
  (9 minutes) (calculating vector length in N dimensions, and the relationship
  to the vector dot product);
* `Proving vector dot product properties
  <https://www.khanacademy.org/math/linear-algebra/vectors_and_spaces/dot_cross_products/v/proving-vector-dot-product-properties>`_
  (11 minutes) (reminding us of - and proving - some mathematical properties
  of dot products on vectors).

Helpful extra background
========================

Optional but highly recommended:

* `Defining the angle between vectors
  <https://www.khanacademy.org/math/linear-algebra/vectors_and_spaces/dot_cross_products/v/defining-the-angle-between-vectors>`_
  (25 minutes) (among other things - why orthogonal vectors have dot product
  of zero);
* `Unit vectors
  <https://www.khanacademy.org/math/linear-algebra/matrix_transformations/lin_trans_examples/v/unit-vectors>`_
  (7 minutes).

Key video on projecting vectors
===============================

The following video is the key homework for the class.  The videos above are
background for this video.

* `Introduction to projections
  <https://www.khanacademy.org/math/linear-algebra/matrix_transformations/lin_trans_examples/v/introduction-to-projections>`_
  (15 minutes);

If you are racing ahead
=======================

If you have extra time on your hands or you are confident you already know
about matrices and projection and want something more advanced, this is
introductory `tutorial on principal component analysis
<http://arxiv.org/abs/1404.1100>`_.  It does assume that you know about
projecting vectors, which you will, after covering the Khan academy videos.

***
Day
***

* Get data from image
* Run PCA;
* Fetch projection matrices, vectors and values;
* Reconstruct data using reduced number of components.
* Investigate and diagnose components;
* Investigate correlation of vectors with data.

*********
Exercises
*********

The usual instructions:

* ``cd pna/pna2015``
* ``git pull``
* ``ipython notebook``

There is a web page listing of the exercise files at
https://github.com/practical-neuroimaging/pna2015/tree/master/day7

.. include:: links_names.inc
