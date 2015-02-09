########
Schedule
########

*******************************
Day 0 : introduction and taster
*******************************

Prior:

Install requirements on your machine |--| see :doc:`installation`.

Day:

* Git clone practical neuroimaging notebooks;
* Numpy / scipy / matplotlib / IPython notebook whirlwind introduction;
* What is an image?
* Loading a 3D image - from :
  http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/loading_images.ipynb
* Getting pixel data
* Text editor intro

**************************
Day 1 : introducing Python
**************************

Prior:

Make a private github account.

Reading: `introduction to Python`_.

Day: Python exercises.

************************************
Day 2: images as arrays and plotting
************************************

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

************************************
Day 3: diagnostics / version control
************************************

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

*****************************************
Day 4: first statistics / version control
*****************************************

Reading:

* Make a branch, edit and commit;
* Merge;
* Push;
* Splitting FMRI time series by slicing;
* Subtracting on blocks from off blocks;
* Visualizing result.

**********************************
Day 5: convolution and correlation
**********************************

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

**********************************************
Day 6: regression and the general linear model
**********************************************

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

*****************************************************
Day 7: diagnostics using principal component analysis
*****************************************************

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

****************************************
Day 8: 1D interpolation and slice timing
****************************************

* Notebook on interpolation and slice timing e.g.
  http://nbviewer.ipython.org/urls/bitbucket.org/matthewbrett/talks/raw/master/processing_i/slice_timing.ipynb

Day:

* Convert notebook to Python module;
* write code to do linear interpolation on example time series;
* write tests;
* use scipy interpolation code;
* investigate splines.

******************************************************
Day 9: optimization, 2D interpolation and registration
******************************************************

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

**********************************************************
Day 10: coordinate systems and cross-modality registration
**********************************************************

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

*************************************
Day 11: registration between subjects
*************************************

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

******************************
Day 12: smoothing and modeling
******************************

Reading:

* Introduction to smoothing: http://perrin.dynevor.org/smoothing_intro.html

Day:

* Smoothing as convolution;
* HRF regressor model on smoothed and unsmoothed data;
* Different smoothing levels;
* single voxel;
* whole brain.

*************************************************
Day 13: testing hypotheses with t and F contrasts
*************************************************

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

***************************************
Day 14: random effects, choosing models
***************************************

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


*****************************
Day 15: statistical inference
*****************************

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

*******************
Possible extra days
*******************

* Using machine learning tools with scikit-learn;
* Introduction to diffusion imaging;
* Introduction to DICOM;
* Data visualization.

.. include:: links_names.inc
