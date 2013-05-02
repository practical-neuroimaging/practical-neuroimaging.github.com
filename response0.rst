.. _response0:

####################
Response to feedback
####################

Full feedback at :ref:`feedback0` and :ref:`feedback1`

First - thanks to all of you who gave feedback - it's very helpful. Here I'm
concentrating on the bad feedback to work out the best way to change.

We haven't said this before, but the course we're trying to teach you is new; we
don't know of anyone else trying to teach course exactly like this, a
combination of programming practice and concepts in neuroimaging.  So please,
bear with us, we are learning too.

**************************
Course too slow / detailed
**************************

    I think the course could move a little more quickly, with more emphasis
    being placed on office hours when catch-up work is required.

    The focus on minute details -- a blessing of the course -- can at times
    become its curse, when lengthy, confusing discussions about obscure coding
    or math issues seem to detract from the big picture.  Getting to the bottom
    of those details is without doubt important, but our time is limited, and
    attention could be better allotted to give priority to the most important
    things. +2

    It may be useful to assign some reading before class introducing the issues
    to be dealt with next. For instance, the MRC webpages put together by
    Matthew and others are a good intro and may help to explain the problem we
    are trying to solve for anyone who doesn't have much fMRI experience. Then,
    before going through the code, we could go over how we will approach the
    problem conceptually (or go over the statistics before they are implemented
    in the code). This way, even if people get lost in the code, they will be
    able to take away a big picture lesson on how to deal with common imaging
    issues in the future. +1

    It would be great if the instructors could point us to good reading material
    about the issues they aren't able to delve deep into. +3

    It would be nice to achieve a couple "big picture" items per class in order
    to keep the necessary attention to minute detail in context.+1

    I'd like to learn a bit more about the pros/cons of various pre-processing
    steps. For instance, how can we test the best parameters to coregister the
    images we may have?

It's clear that:

* We're going too slowly
* There have been various times we've got bogged down in detail
* We need to give a better overall picture of the analysis

We don't want to give up on the - detail - because we want to teach you how to
get down and dirty with the data, and this involves - detail.

But there's some detail needed and some not, and we haven't always got the
balance that we need if we're going to teach you efficiently.  We are going to
try restructuring the rest of the course to be explicit about the big picture of
neuroimaging analysis, and how the work of each class fits into this big
picture.

The reading before the class is a good idea, but, we don't yet have a good grasp
of what reading material would be useful, apart from the MRC web-pages.  We'll
update the MRC pages to match the course better; there is a start here:
https://github.com/fperez/nipy-notebooks

**************************************************
Need more detail on course curriculum and schedule
**************************************************

    It would be helpful to have a course outline at the outset so we know what
    to expect.

The reason we haven't done a course outline is because we didn't know how the
course would evolve, because it has not been done before.  We agree that this is
a problem and it would better both for our planning and yours to have a clear
idea of the curriculum and how each day relates to the curriculum.  We need to
allow ourselves some slack to deal with the newness of the course, but we will
(from now) put up the plan for each week, with reading material as we find it.

******************************
More on data analysis workflow
******************************

    I don't know where we're headed, but it's really important to me that, by
    the end of this course, I know how to write all my own code to move from raw
    data to completed analysis.  As long as the course provides pre-written
    notebooks to get from the beginning to the end, I should be OK -- whatever I
    don't understand by the end of the course I'll review after it's over.

    It's helpful for a python newbie to hear how the data is structured; once we
    have a baseline knowledge of what it is, it would help me to hear your
    workflow of how to handle it. I assume we'll get to that, though.

We do need to get to data organization and analysis workflow, and we plan to get
to that in the next few classes.  We have found it difficult to get the balance
between the convenience of the IPython notebooks and our daily practice of
coding which has to deal - as you've implied - with big directory trees and long
processing pipelines, as well as writing utility functions and analysis scripts.
We'll try and address this better.

**************************************************
Better balance between exercises and demonstration
**************************************************

    It would be nice to have some specific projects/assignments to work on soon
    +3

    It would be nice if you left some Inputs blank so that we could try writing
    a couple of commands ourselves+2

    I like it when we approach a problem as a class, rather than just reading
    code that has already been written (though that is definitely useful as
    well). +1

We've been aware of this problem from early on - it was clear to us and you that
exercises were very helpful, but we haven't found it easy to break the flow of
the notebook for exercises.   We will work harder on this in the next few
classes because we agree this is essential.  Please feel free to annoy us about
this if we don't do a good job.

*************************************************************************
Difficulty of mixing people with different levels of background knowledge
*************************************************************************

    I find that I often get lost on these details as well, and most go over my
    head... as a beginner (with a very basic understanding of Python, that is), I
    feel happy when I understand about 50% of what we've covered. I may be alone in
    this... +1

    I think this course might be better divided into two distinct sections: 1) A
    Python basics section that helps everyone feel competent with running basic
    Python code and using the notebook  2) A fMRI analysis section that gets
    into the higher level topics. I think this format could help with
    attrition.+2

This is a big problem, and we don't know how to handle it yet.  I (Matthew)
learned a great deal by going to courses in which I got nearly completely lost,
but soaked up just enough to be able to think better about it the next time I
heard it.  In fact the course is designed to try and reduce this feeling of
being lost by showing you how it's all done - but it's inevitable that we'll
lose some of you for some of the time, given the mixtures of experience in the
class.  We'd really like to maintain this mixture though.   We're planning how
to provide some background for those who need it; for example, we teach on
`Software Carpentry <http://software-carpentry.org>`_ courses. These can be very
useful for some coverage of the basics of programming, Python, and version
control.  We've heard good things about the `Code Academy Python course
<http://www.codecademy.com/tracks/python>`_.  We'll try and address this better
next time through the course.
