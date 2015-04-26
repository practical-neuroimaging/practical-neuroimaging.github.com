######################################################
Day 9: optimization, 2D interpolation and registration
######################################################

4 / 24 / 2015

*******
Reading
*******

The reading for this weeks class is a notebook in the `pna2015` repository::

    cd pna2015
    git pull
    ipython notebook

The main notebook is ``day9/optimizing_space.ipynb`` - but you'll see a couple
of other notebooks there that the main notebook links to.

Here are the notebooks generated as non-interactive web pages, for reference:

* `main notebook on spatial registration
  <http://nbviewer.ipython.org/github/practical-neuroimaging/pna2015/blob/master/day9/optimizing_space.ipynb>`_;
* `background on Python functions
  <http://nbviewer.ipython.org/github/practical-neuroimaging/pna2015/blob/master/day9/functions_are_objects.ipynb>`_;
* `background on global variable scope
  <http://nbviewer.ipython.org/github/practical-neuroimaging/pna2015/blob/master/day9/global_scope.ipynb>`_.

You may also want to have a look at :doc:`rotation_2d`.

***
Day
***

* Convert optimization notebook to Python module;
* Run;
* Try different cost functions;
* Try different optimization methods;
* Local minima with a 180 degree rotation;
* Investigate and run FSL motion correction.
