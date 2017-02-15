###############
Example dataset
###############

We will be using the `Duncan et al data`_ from the OpenFmri_ project.

This is dataset ``ds107``.

We'll start by looking at the first 15 subjects.

We have copies of subject 1's first functional and structural image in the
`course web directory`_

*******************
Description of data
*******************

Article describing dataset and analysis:

http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2686646/

From the methods section of that article, we find these bits of information:

* Siemens 1.5 T MR scanner
* EPI (functional images)
    * TR = 3000 ms
    * TE = 50 ms
    * FOV = 192 × 192
    * matrix = 64 × 64
    * "notional resolution" 3 × 3 × 3 mm
    * 164 volumes per run
* T1 FLASH (anatomical images)
    * TR = 12 ms
    * TE = 5.6 ms
    * 1 mm3 resolution

Missing information
===================

At least - I couldn't find this information at a quick scan - please correct me
if I'm wrong:

* Slice order (interleaved?  sequential?)
* Volume gap in time (any gap between the last slice from volume N and the first
  slice of volume N+1?)
* Slice width (was there a gap between the slices)

.. include:: links_names.inc
