###########
Convolution
###########

*****************************
Neural and hemodynamic models
*****************************

In functional MRI (FMRI), we often have the subjects do a task in the scanner.
For example, we might have the subject lying looking at a fixation cross on
the screen for most of the time, and sometimes show a very brief burst of
visual stimulation, such as a flashing checkerboard.

We will call each burst of stimulation an *event*.

We will later want to see if the event has caused a change in the FMRI signal.
In order to do that, we need to be able to predict the change in signal caused
by the event.

The FMRI signal comes about first through changes in neuronal firing, and then
by blood flow responses to the changes in neuronal firing.  In order to
predict the FMRI signal to an event, we first need a prediction (model) of the
changes in neuronal firing, and second we need a prediction (model) of how
the blood flow will change in response to the neuronal firing.

So we have a two-stage problem:

* predict the neuronal firing to the event (make a *neuronal firing model*);
* predict the blood flow changes caused by the neuronal firing (a *hemodynamic
  model*).

Convolution_ is a simple way to create a hemodynamic model from a neuronal
firing model.

The neuronal firing model
=========================

The neuronal firing model is our prediction of the profile of neural activity
in response to the event.

For example, in this case, with a single stimulation, we might predict that,
as soon as the visual stimulation went on, the cells in the visual cortex
instantly increased their firing, and kept firing at the same rate while the
stimulation was on.

In that case, our *neural* model of an event starting at 4 seconds, lasting 5
seconds, might look like this:

.. plot::
    :context:

    import numpy as np
    import matplotlib.pyplot as plt

    times = np.arange(0, 30, 0.1)
    n_time_points = len(times)
    neural_signal = np.zeros(n_time_points)
    neural_signal[(times >= 4) & (times < 9)] = 1
    plt.plot(times, neural_signal)
    plt.xlabel('time (seconds)')
    plt.ylabel('neural signal')
    plt.ylim(0, 1.2)
    plt.title("Neural model for 5 second event starting at time 4")

This type of simple off - on - off model is a `boxcar function`_.

Of course we could have had another neural model, with the activity gradually
increasing, or starting high and then dropping, but let us stick to this
simple model for now.

The hemodynamic model
=====================

The signal we have actually collected in FMRI is not neural signal, but
`blood-oxygen-level dependent`_ signal (BOLD).  The BOLD signal depends on the
changes in blood flow, and responds relatively slowly to changes in neuronal
activity.  For this reason the BOLD response is also often known as the
hemodynamic response.  The BOLD (hemodynamic) signal to a very quick on-off
neural event starting at time 0, looks something like this:

.. plot::
    :context:

    def afni_hrf(t):
        "The hemodynamic response from the AFNI software package"
        return t ** 8.6 * np.exp(-t / 0.547)

    hrf_times = np.arange(0, 20, 0.1)
    hrf_signal = afni_hrf(hrf_times)
    plt.plot(hrf_times, hrf_signal)
    plt.xlabel('time (seconds)')
    plt.ylabel('BOLD signal')
    plt.title('Estimated BOLD signal for event at time 0')

This is the hemodynamic response to a very short neural event.  It is
therefore also called the *hemodynamic response function* (HRF).

We know that the neural signal will be transformed by this slower
hemodynamic effect.  So, how do we use this information to get from a model of
the time course of the neural signal to a model of the BOLD signal?

This is the where convolution_ steps in.

Convolution and the impulse response
====================================

Let's simplify a little by pretending that the event was really short.  Call
this event |--| an *impulse*.  This simplifies our neural model to a single
spike in time instead of a sustained rise (or box-car).

.. plot::
    :context:

    neural_signal = np.zeros_like(times)
    i_time_4 = np.where(times == 4)[0]  # index of value 4 in "times"
    neural_signal[i_time_4] = 1  # A single spike at time == 4
    plt.plot(times, neural_signal)
    plt.xlabel('time (seconds)')
    plt.ylabel('neural signal')
    plt.ylim(0, 1.2)
    plt.title("Neural model for very brief event at time 4")

So, this is our *impulse*.  Above we see the hemodynamic response to a very
short impulse like this.  The HRF is the response in the FMRI signal to a very
brief neural impulse.  In signal processing terms the HRF would be the
response to the impulse, or `impulse response function <impulse response>`_
(IRF).

The idea of convolution is this: we assume that every time there is an impulse
in the *input signal* (in our case, the neural signal), then there will be an
IRF evoked in the *output signal*.

We assume there is no difference in the relationship of the impulse to the
response over time |--| one impulse always generates the same response.  This
is the *time invariant* assumption.

We assume that, if two evoked responses overlap, then we get the resulting output signal by
adding up the evoked responses for each time point.  This is the *linear*
assumption.

If we make both of these assumptions then we have a *linear time-invariant*
system, and this is the system for which convolution can do our work for us.

We will see that the mathematical operation of *convolving* the neural input
signal with the HRF gives us a prediction of the hemodynamic output signal, as
long as we can make the *linear* and *time-invariant* assumptions.

Convolution as adding responses
===============================

The principle of convolution is very simple.  For every impulse in the input
signal, we add a matching copy of the IRF to the output signal.

In the simplest case we might have a very brief neural impulse as in the plot
above.

Convolution will give us one copy of the IRF (HRF) in the output signal,
starting at the position of the impulse.

For now we will do the convolution with the numpy ``convolve`` routine without
further explanation so you can see the output:

.. plot::
    :context:

    bold_signal = np.convolve(neural_signal, hrf_signal)[:n_time_points]
    plt.plot(times, bold_signal)
    plt.xlabel('time (seconds)')
    plt.ylabel('bold signal')
    plt.title('Output BOLD signal predicted by convolution')

The output is exactly the same as if we had added a time-shifted copy of the
HRF to a vector of zeros.

.. plot::
    :context:
    :nofigs:

    n_hrf_points = len(hrf_signal)
    bold_more_simple = np.zeros(n_time_points)
    bold_more_simple[i_time_4:i_time_4 + n_hrf_points] = hrf_signal
    assert np.all(bold_more_simple == bold_signal)

Now let's say we have three impulses, at 4, 10, and 30 seconds:

.. plot::
    :context:

    times_3 = np.arange(0, 50, 0.1)
    n_time_points_3 = len(times_3)
    neural_signal_3 = np.zeros(n_time_points_3)
    i_time_4 = np.where(times_3 == 4)[0]  # index of value 4 in "times_3"
    i_time_10 = np.where(times_3 == 10)[0]  # index of value 10 in "times_3"
    i_time_30 = np.where(times_3 == 30)[0]  # index of value 30 in "times_3"
    neural_signal_3[i_time_4] = 1  # A single spike at time == 4
    neural_signal_3[i_time_10] = 1  # A single spike at time == 10
    neural_signal_3[i_time_30] = 1  # A single spike at time == 30
    plt.plot(times_3, neural_signal_3)
    plt.xlabel('time (seconds)')
    plt.ylabel('neural signal')
    plt.ylim(0, 1.2)
    plt.title('Neural model for very brief events at times 4, 10, 30')

The convolution is the same as taking one HRF offset by 4 seconds, one by 10
seconds and one by 30 seconds, and summing them up:

.. plot::
    :context:

    bold_signal_3 = np.convolve(neural_signal_3, hrf_signal)[:n_time_points_3]
    plt.plot(times_3, bold_signal_3)
    plt.xlabel('time (seconds)')
    plt.ylabel('bold signal')
    plt.title('Output BOLD signal for 3 events predicted by convolution')

Now say that the second event, at 10 seconds has twice the amplitude of the
events at 4 and 30 seconds:

.. plot::
    :context:

    neural_signal_3[i_time_10] = 2  # A bigger spike at time == 10
    plt.plot(times_3, neural_signal_3)
    plt.xlabel('time (seconds)')
    plt.ylabel('neural signal')
    plt.ylim(0, 2.2)
    plt.title('Neural model for larger event at 10 seconds')

Now the convolution is the same as adding:

* the HRF offset to 4 seconds and scaled by 1;
* the HRF offset to 10 seconds and scaled by 2;
* the HRF offset to 30 seconds and scaled by 1;

.. plot::
    :context:

    bold_signal_3 = np.convolve(neural_signal_3, hrf_signal)[:n_time_points_3]
    plt.plot(times_3, bold_signal_3)
    plt.xlabel('time (seconds)')
    plt.ylabel('bold signal')
    plt.title('Output BOLD signal for larger event at 10 seconds')

Convolution rephrased
=====================

The general principle of the convolution is this:

* Start with a output vector that is a vector of zeros
* Iterate over each index in the *input vector* (in our case, the neural
  signal);
* Take the value of the input at this index, and multiply by the IRF (in our
  case, the HRF) |--| call this the *scaled IRF vector*.
* Add the scaled IRF vector to the output vector, with the first value in the
  the scaled IRF vector added at the current index, the next at the next index
  and so on.

Imagine the input vector has N elements, and the IRF has M elements.

Notice that, when the iteration gets to the last index of the *input vector*
(index == N-1), the scaled IRF vector will, as ever, be M points long.  If the
output vector is the same length as the input vector, we can add only the
first point of the new scaled IRF vector to the last point of the output
vector, but all the subsequent values of the scaled IRF vector have no
corresponding index in the output.  The way to solve this is to extend the
output vector by the necessary M-1 points, so the output vector from a default
convolution is N + M - 1 elements long:

.. plot::
    :context:
    :nofigs:

    default_convolved = np.convolve(neural_signal_3, hrf_signal)
    assert len(default_convolved) == n_time_points_3 + n_hrf_points - 1
    assert len(default_convolved) == len(neural_signal_3) + len(hrf_signal) - 1

The algorithm for convolution is clearer in actual code:

.. plot::
    :context:

    # The output is N + M - 1 long
    n_output = n_time_points_3 + n_hrf_points - 1
    output = np.zeros(n_output)
    for i in range(n_time_points_3):
        neural_value = neural_signal_3[i]
        scaled_irf = neural_value * hrf_signal
        output[i:i+n_hrf_points] = output[i:i+n_hrf_points] + scaled_irf
    corresponding_times = np.arange(n_output) * 0.1
    plt.plot(corresponding_times, output)

Notice that this last plot has the same values as the previous plot, but with
a 20 (-0.1) second tail at the end, caused by the M-1 extension in the output.

What happens with a box-car instead of an impulse?
==================================================

We started off with a neural model where the nerves turned on at time == 4
seconds and stayed on at the same level for 5 seconds.

What would convolution to this signal?

You can now predict what it will do, but here is what it looks like:

.. plot::
    :context:

    neural_signal_5s = np.zeros(n_time_points)
    neural_signal_5s[(times >= 4) & (times < 9)] = 1
    bold_signal_5s = np.convolve(neural_signal_5s, hrf_signal)[:n_time_points]
    neural_signal_impulse = np.zeros(n_time_points)
    neural_signal_impulse[(times == 4)] = 1
    bold_signal_impulse = np.convolve(neural_signal_impulse, hrf_signal)[:n_time_points]
    plt.plot(times, bold_signal_5s, label='5 second event signal')
    plt.plot(times, bold_signal_impulse, label='impulse event signal')
    plt.xlabel('time (seconds)')
    plt.ylabel('bold signal')
    plt.title('Output BOLD signal for event 5 seconds long')
    plt.legend()

How did this happen?  The algorithm says that when the convolution gets to
the position of time == 4 in the input, it finds a value 1, so adds an HRF to
the output at that position.  It then moves one index along (corresponding to
0.1 seconds) finds another value 1 and adds another HRF to the output and so
on until the end of the event, at the time corresponding to 9 seconds - 0.1.
So the output is the result of adding 50 HRFs, each offset by 0.1 seconds from
the next.

Put another way, the convolution says that you will get the same output from
two events 0.1 seconds apart as you will from one event lasting 0.2 seconds.
In the case of the 5 second event we are saying that the 5 second event will
cause the same signal as 50 events all 0.1 seconds apart.  This is the linear
time invariant assumption.

When we use convolution we have to keep these assumptions in mind, because
they may not be reasonable in some situations.

More reading on convolution
===========================

We can unpack this algorithm a further to show it can be done more efficiently
in code, and how convolution can be implemented with matrix multiplication
|--| see this `notebook on convolution
<http://nbviewer.ipython.org/urls/raw.github.com/practical-neuroimaging/pna-notebooks/master/convolution.ipynb>`_

.. include:: links_names.inc
