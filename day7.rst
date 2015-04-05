#####################################################
Day 7: diagnostics using principal component analysis
#####################################################

4 / 10 / 2015

This class is for us to get an idea of the variation in the FMRI data, and to
practice our linear algebra by working with images as matrices. We will do
this using `principal component analysis`_ (PCA).

*******
Reading
*******

PCA is useful for our purpose, for two reasons:

#. it is a useful way of investigating the image data in more depth,
   including screening for image artifacts.
#. it is good practice for thinking about the kind of linear algebra that
   comes up a lot in the GLM statistics and other places in image analysis;

To get ready for the PCA, we need some basic linear algebra under our belts,
to get us used to dot products, angles between vectors, and projections.

Khan academy has some excellent tutorials on these subjects.

Here is the basic background on dot products:

* `Vector dot product and vector length
  <https://www.khanacademy.org/math/linear-algebra/vectors_and_spaces/dot_cross_products/v/vector-dot-product-and-vector-length>`_
  (9 minutes) (calculating vector length in N dimensions, and the relationship
  to the vector dot product);
* `Proving vector dot product properties
  <https://www.khanacademy.org/math/linear-algebra/vectors_and_spaces/dot_cross_products/v/proving-vector-dot-product-properties>`_
  (11 minutes) (reminding us of - and proving - some mathematical properties
  of dot products on vectors).

These are good extra background:

* `Defining the angle between vectors
  <https://www.khanacademy.org/math/linear-algebra/vectors_and_spaces/dot_cross_products/v/defining-the-angle-between-vectors>`_
  (25 minutes) (among other things - why orthogonal vectors have dot product
  of zero);
* `Unit vectors <https://www.khanacademy.org/math/linear-algebra/matrix_transformations/lin_trans_examples/v/unit-vectors>`_ (7 minutes).

The last video is the key homework for the class.  The videos above are
background for this video.

* `Introduction to projections
  <https://www.khanacademy.org/math/linear-algebra/matrix_transformations/lin_trans_examples/v/introduction-to-projections>`_
  (15 minutes);

If you have extra time on your hands or feel you already know about matrices
and projection and want something more advanced, this is introductory
`tutorial on principal component analysis <http://arxiv.org/abs/1404.1100>`_.
It does assume that you know about projecting vectors, which you will, after
covering the Khan academy videos.

***
Day
***

* Get data from image
* Run PCA;
* Fetch projection matrices, vectors and values;
* Reconstruct data using reduced number of components.
* Investigate and diagnose components;
* Investigate correlation of vectors with data.

.. include:: links_names.inc
