##################################
Practical neuroimaging, the sequel
##################################

.. Berkeley dates

    Spring semester: http://registrar.berkeley.edu/stucal.html

    Semester begins 13 January 2015;
    Instruction begins 20 January;
    Final exams May 11-15;
    Semester ends May 15.

    15 Fridays 30 January through 8 May.

***********************
Who is this course for?
***********************

The course is designed for people starting or doing neuroimaging, with some
programming experience (for example, writing MATLAB or Python scripts).

We have designed the course to help you:

* Understand the basic concepts in neuroimaging, and how they relate to the
  wider world of statistics, engineering, computer science;
* Be comfortable working with neuroimaging data and code, so you can write
  your own basic algorithms, and understand other people's code;
* Work with code and data in a way that will save you time, help you
  collaborate, and continue learning.

************
Requirements
************

* Reasonable knowledge of programming in any language;

**********
Background
**********

    That which I cannot build, I do not understand (Feynman)

* Practical workflow for continuous learning;
* Relevant concepts in mathematics / statistics / engineering;
* FMRI analysis steps.

We aim to teach you to work efficiently, so that you can in due course forget
about your tools and think about the ideas.  We aim to make things simple,
rather than easy, so that you can reach a stage where things are both simple
and easy.

Practical workflow
==================

* Version control (we teach git);
* Extensible text editor (see below);
* Versatile programming language (we teach Python);
* Testing code;
* Collaborating with code.

Relevant concepts
=================

* convolution (hemodynamic modeling, smoothing);
* interpolation (slice time correction, image resampling);
* optimization (registration, advanced statistics);
* basic linear algebra (statistics);

FMRI analysis steps
===================

* Diagnostics;
* slice timing;
* motion correction;
* registration within and between subject;
* smoothing;
* statistical estimation with multiple regression;
* statistical inference.

*********************
Format of the classes
*********************

* Prior reading / homework for each week of approx 30 minutes;

* Class is 2 hours:

    * 10 minutes debrief from previous class
    * 30 minutes talk introduction + questions;
    * 60 minutes problems;
    * 10 minutes review of problems;

For each day there will be a short teaching point on one of:

* version control;
* text editing;
* code collaboration.

***************
General reading
***************

* `Nature article on Python in science
  <http://www.nature.com/news/programming-pick-up-python-1.16833>`_
* `Essay by Peter Norvig <http://norvig.com/21-days.html>`_.  `Peter Norvig
  <http://en.wikipedia.org/wiki/Peter_Norvig>` is director of research at
  Google.
* Greg Wilson's article on scientific computing: Wilson, Greg, et al. "Best
  practices for scientific computing." PLoS biology 12.1 (2014): e1001745.
* Donoho reproducibility article : Donoho, David L. 2010. An invitation to
  reproducible computational research. Biostatistics 11, 385–388.
  http://biostatistics.oxfordjournals.org/content/11/3/385.full

************
Text editors
************

* vim;
* emacs;
* TextMate;
* sublime text;
* Notepad++.

You can use any other text editor, but we'll be doing text editor challenges
through the course to teach ourselves speed and shortcuts for our editors.

The list of editors comes from
http://www.rackspace.com/blog/text-editor-madness-bracket-vote-for-your-favorite
with the edition of TextMate (because we know at least one extremely efficient
coder who uses it).

Your teachers use Vim (x2) and Emacs (x1).

***********************
General teaching points
***********************

* Proceed by iterating through a single subject analysis;
* balance of IPython notebook and Python modules.

********
Schedule
********

Day 0 : introduction and taster
===============================

Prior
-----

Install requirements on your machine

* git;
* Python;
* pip;
* scipy-stack (numpy, scipy, matplotlib, IPython, pandas);
* nibabel.

Make a private github account.

Installation instructions will be a version of
http://practical-neuroimaging.github.io/installation.html

Possible reading:

* Class introduction - e.g http://practical-neuroimaging.github.io/day0.html
* Numpy universe package summary - e.g.
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/python_libraries.ipynb
* Choosing a text editor - e.g.
  http://practical-neuroimaging.github.io/choosing_editor.html

Day:

* Git clone practical neuroimaging notebooks;
* Numpy / scipy / matplotlib / IPython notebook whirlwind introduction;
* What is an image?
* Loading a 3D image - from :
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/loading_images.ipynb
* Getting pixel data
* Text editor intro

Day 1 : introducing Python
==========================

Prior
-----

* Make sure your Python environment installed on day 0 still works
* Finish first Python Module on Codecademy: http://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1


Day:

* variables, math
* flow control (conditional statements, loops)
* basic data structures (lists and dictionaries)
* importing modules
* reading and parsing text files (basic)

Day 2: images as arrays and plotting
====================================

Reading:

* Numpy introduction TBA
* Matplotlib introduction TBA
* What is an image? e.g.
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/what_is_an_image.ipynb

Day:

* Loading a 4D image (e.g.
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/loading_images.ipynb)
* Mean, standard deviation, variance over time
* Text editor competition.

Day 3: diagnostics / version control
====================================

Reading:

* Workflow e.g.
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/workflow.ipynb
* Git basics: http://matthew-brett.github.io/pydagogue/curious_git.html

Day:

* Refresher on Python modules and packages;
* Transfer notebook code into text files;
* Add to git;
* Time series diagnostics;
* Make an edit and commit and push;

Day 4: first statistics / version control
=========================================

Reading:

* Make a branch, edit and commit;
* Merge;
* Push;
* Splitting FMRI time series by slicing;
* Subtracting on blocks from off blocks;
* Visualizing result.

Day 5: convolution and correlation
==================================

Reading:

* Something on hemodynamic modeling;
* Notebook on convolution - an edited version of
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/convolution.ipynb

Day:

* Creating the convolution kernel;
* Extracting time series (slicing in 4th dimension);
* Convolution the dumb way;
* Convolution the scipy way;
* Correlating the convolved time course with the data.

Day 6: regression and the general linear model
==============================================

Reading:

* Poline and Brett 2012 : http://matthew.dynevor.org/_downloads/does_glm_love.pdf
* Notebook on GLM / contrasts - at: http://perrin.dynevor.org/glm_intro.html

Day:

* Load time course;
* rebuild convolved regressor;
* set up matrices;
* run estimation;
* visualize result;
* replicate subtraction analysis from previous day with dummy regressors;
* visualize result;
* (relationship of correlation and regression).

Day 7: diagnostics using principal component analysis
=====================================================

This day is for us to practice working with matrices, and to get an idea of
the level of underlying variance in data.

Reading:

* Notebook on diagnostics:
  http://nbviewer.ipython.org/urls/bitbucket.org/matthewbrett/talks/raw/master/processing_i/diagnostics.ipynb
* A tutorial on principal component analysis: http://arxiv.org/abs/1404.1100

Day:

* Get code from notebook;
* Run PCA;
* Fetch projection matrices, vectors and values;
* Reconstruct data using reduced number of components.
* Investigate and diagnose components;
* Investigate correlation of vectors with data.

Day 8: 1D interpolation and slice timing
========================================

* Notebook on interpolation and slice timing e.g.
  http://nbviewer.ipython.org/urls/bitbucket.org/matthewbrett/talks/raw/master/processing_i/slice_timing.ipynb

Day:

* Convert notebook to Python module;
* write code to do linear interpolation on example time series;
* write tests;
* use scipy interpolation code;
* investigate splines.

Day 9: optimization, 2D interpolation and registration
======================================================

Reading:

* Notebook on optimization for registration:
  http://nbviewer.ipython.org/urls/bitbucket.org/matthewbrett/talks/raw/master/processing_i/optimizing_space.ipynb

(Add subtracted image after registration).

Day:

* Convert optimization notebook to Python module;
* Run;
* Try different cost functions;
* Try different optimization methods;
* Local minima with a 180 degree rotation;
* Investigate and run FSL motion correction.

Day 10: coordinate systems and cross-modality registration
==========================================================

Reading:

* Tutorial on coordinate systems at:
  http://nipy.org/nibabel/coordinate_systems.html
* Mutual information : e.g.
  http://nbviewer.ipython.org/urls/bitbucket.org/matthewbrett/talks/raw/master/processing_i/mutual_information_example.ipynb

Need to fix this up.

Day:

* Load EPI;
* Load anatomical;
* Reslicing using coordinate transforms;
* Scipy ndimage and affine_transform;
* FSL coregistration;
* SPM coregistration.

Day 11: registration between subjects
=====================================

Reading:

* Localization paper at http://matthew.dynevor.org/_downloads/location.pdf
* Tutorial on inter-subject registration (spatial normalization). Yet to be
  written.  Some material at:

  * http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/ANTS_normalization.ipynb
  * http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/template_registration.ipynb
  * http://nipy.org/dipy/examples_built/syn_registration_2d.html#example-syn-registration-2d
  * http://nipy.org/dipy/examples_built/syn_registration_2d.html#example-syn-registration-3d

Day:

* Affine registration using scipy;
* Affine registration using FSL;
* Warping in 2D using dipy regtools;
* Diagnosing the warp using the deformation mesh;
* Affine plus warping using FSL;
* Thinking about what makes a good registration.

Day 12: smoothing and modeling
==============================

Reading:

* Introduction to smoothing: http://perrin.dynevor.org/smoothing_intro.html

Day:

* Smoothing as convolution;
* HRF regressor model on smoothed and unsmoothed data;
* Different smoothing levels;
* single voxel;
* whole brain.

Day 13: testing hypotheses with t and F contrasts
=================================================

Reading:
    * Notebook on t / F - version of :
      http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/GLM_t_F.ipynb

Day:

* Block (on / off model) F contrasts;
* Motion parameters as confounds;
* t contrasts for motion;
* F contrasts for motion;
* FSL contrasts;
* SPM contrasts.

Day 14: random effects, choosing models
=======================================

Reading:

* random versus fixed effect in neuroimaging litterature
  ftp://193.62.66.20/spm/data/face_rfx/RFXabstract.pdf
  http://www.fil.ion.ucl.ac.uk/spm/doc/books/hbf2/pdfs/Ch12.pdf

* a simple tutorial on cross validation
  http://www.autonlab.org/tutorials/overfit.html

Day:

* Recall t and F tests: what are they doing exactly.  Where does my variability come from?
   - example within run (from previous course)
   - example random effect (between subjects).

* Wait a second: What is a model exactly ?

* I am chosing a very wrong model: Consequences on the results of t/F tests.

* How do I know my model is - is not very wrong? the good, the bad, the ugly (reverse order)
   - the ugly: p-hacking. Let's try it.
   - the bad: use R2.
   - the good: model validation

* Model validation: Principle.  Example of "random effect" model testing the effect of "grumpiness".


Day 15: statistical inference
=============================

Reading:

* Bonferroni correction : e.g.
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/bonferonni_notes.ipynb
* Random fields : e.g. http://perrin.dynevor.org/random_fields.html
* FDR: http://nbviewer.ipython.org/github/practical-neuroimaging/pna-notebooks/blob/master/FDR.ipynb

Day:

* Generate map of T
* correct using Bonferroni;
* correct using random fields;
* correct using FDR;

Possible extra days
===================

* Using machine learning tools with scikit-learn;
* Introduction to diffusion imaging;
* Introduction to DICOM;
* Data visualization.

.. to discuss:

    * Not enough introduction to numpy / matplotlib?
    * Role of testing?
