###########################
Day zero : 15 February 2013
###########################

The introduction to the class, what we are going to cover, and why, and how.

The tools you'll need for the later classes, why they are important, how to
choose the right tools.

Introducing the example data set we will use.

Loading brain images and checking for problems.

*******
Summary
*******

* You
* Us
* What you want out of the course

* The benefits of being fluent
* Reliability
* Efficiency
* Creativity

* Getting started

*****
Notes
*****

The problem of incorrect findings
=================================

* Why most published research findings are false:
  http://www.plosmedicine.org/article/info:doi/10.1371/journal.pmed.0020124
* Blog discussion including estimates of false findings in neuroimaging:
  http://www.danielbor.com/dilemma-weak-neuroimaging/ with Nancy Kanwisher's
  lead-off on replication here:
  http://www.danielbor.com/dilemma-weak-neuroimaging/#comment-77
* `Climategate
  <http://en.wikipedia.org/wiki/Climatic_Research_Unit_email_controversy>`_ The
  `HARRY_READ_ME.txt file
  <http://www.anenglishmanscastle.com/HARRY_READ_ME.txt>`_
* Take no-one's word for it - `Nullius in verba
  <http://en.wikipedia.org/wiki/Nullius_in_verba>`_ - motto of the Royal
  Society.
* Python used as main teaching language:
    * `by MIT
      <http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/index.htm>`_
    * `by Berkeley <http://www-inst.eecs.berkeley.edu/~cs61a/sp13/>`_
* Python compared to MATLAB:
    * http://stevetjoa.com/305/
    * http://www.scipy.org/NumPy_for_Matlab_Users

Donoho quote 0:

    "The scientific method’s central motivation is the ubiquity of error–the
    awareness that mistakes and self-delusion can creep in absolutely anywhere
    and that the scientist’s effort is primarily expended in recognizing and
    rooting out error." [donoho2009reproducible]_

Donoho quote 1:

    “In stark contrast to the sciences relying on deduction or empiricism,
    computational science is far less visibly concerned with the ubiquity of
    error. At conferences and in publications, it’s now completely acceptable
    for a researcher to simply say, ‘here is what I did, and here are my
    results.’ Presenters devote almost no time to explaining why the audience
    should believe that they found and corrected errors in their computations.
    The presentation’s core isn’t about the struggle to root out error — as it
    would be in mature fields — but is instead a sales pitch: an enthusiastic
    presentation of ideas and a breezy demo of an implementation. Computational
    science has nothing like the elaborate mechanisms of formal proof in
    mathematics or meta-analysis in empirical science. Many users of scientific
    computing aren’t even trying to follow a systematic, rigorous discipline
    that would in principle allow others to verify the claims they make. How
    dare we imagine that computational science, as routinely practiced, is
    reliable!” [donoho2009reproducible]_

Donoho quote 2:

    “In my own experience, error is ubiquitous in scientific computing, and one
    needs to work very diligently and energetically to eliminate it. One needs a
    very clear idea of what has been done in order to know where to look for
    likely sources of error. I often cannot really be sure what a student or
    colleague has done from his/her own presentation, and in fact often his/her
    description does not agree with my own understanding of what has been done,
    once I look carefully at the scripts. Actually, I find that researchers
    quite generally forget what they have done and misrepresent their
    computations.

    Computing results are now being presented in a very loose, “breezy” way—in
    journal articles, in conferences, and in books. All too often one simply
    takes computations at face value. This is spectacularly against the evidence
    of my own experience. I would much rather that at talks and in referee
    reports, the possibility of such error were seriously examined."
    [donoho2010invitation]_

*********
Practical
*********

We started going through Ariel Rokem's "Introduction to Python" notebook.

* The `IPython notebook`_ is a part of the IPython_ project
* `Introduction to Python raw notebook file
  <https://raw.github.com/jbpoline/bayfmri/master/notebooks/001-Introduction-Python.ipynb>`_
* `Intro to Python notebook displayed as web page <http://nbviewer.ipython.org/urls/raw.github.com/jbpoline/bayfmri/master/notebooks/001-Introduction-Python.ipynb>`_

We ran the notebook by first downloading the raw file (above), then, in the same
directory, running the command ``ipython notebook``

.. [donoho2009reproducible]
   Donoho, David L, et al. 2009. Reproducible research in computational 
   harmonic analysis. *Computing in Science & Engineering* 11, 8--18.
   http://www.stanford.edu/~vcs/papers/ReproducibleResearch20080811.pdf

.. [donoho2010invitation] Donoho, David L. 2010. An invitation to reproducible
   computational research. *Biostatistics* 11, 385--388.
   http://biostatistics.oxfordjournals.org/content/11/3/385.full

.. include:: links_names.inc
