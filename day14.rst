#######################################
Day 14: random effects, choosing models
#######################################

5 / 22 / 2015

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
