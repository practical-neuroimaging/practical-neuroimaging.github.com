##################################
Putting modules on the Python path
##################################

Let's say I have a Python module called ``myfunctions.py``.  I have stored this
in a directory ``/Users/mb312/code``.  So, the full path to the file is
``/Users/mb312/code/myfunctions.py``.

Here is the contents of ``myfunctions.py``::

    """ Some useful functions that I use, usefully
    """

    def add_badly(a, b):
        return a + b + 1

I'm working in some directory ``/Users/mb312/working``
(``/Users/mb312/working`` is my current directory).

I want to be able to start Python, ``import myfunctions``, and then
do something like::

    print(myfunctions.add_badly(10, 3))

and get the expected answer ``14``.

If I start Python and do that::

    $ python
    Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46) 
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import myfunctions
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ImportError: No module named myfunctions

This is because Python does not know where to find ``myfunctions.py``.

When Python is looking for a new module, like ``myfunctions.py``, it searches
a list of directories stored as the ``path`` variable, in the ``sys`` module.

Here is the contents of that variable on my system::

    >>> import sys
    >>> print('\n'.join(sys.path))

    /Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload
    /Users/mb312/Library/Python/2.7/lib/python/site-packages
    /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
    /Library/Python/2.7/site-packages

Notice that ``sys.path`` is a simple list::

    >>> type(sys.path)
    <type 'list'>

When I run the command ``import myfunctions``, Python will look for a file
``myfunctions.py`` [#on-extensions]_ in each of the directories in the list,
starting with the first.  As soon as it finds this file, it stops, and imports
it.  If it does not find the file, I get the ``ImportError`` we saw above.

The ``sys.path`` list of directories is also called the *module search path*.
See https://docs.python.org/2/tutorial/modules.html#the-module-search-path for
more detail.

If we want to be able to ``import myfunctions`` we need to put *the directory
containing the module* into the *module search path*.  In our case we want to
put the directory ``/Users/mb312/code`` onto the module search path.

There are various ways to do this, but the most direct way to do that, is to
change the value of the ``sys.path`` variable after starting Python.

Because ``sys.path`` is a list of strings, I can append my directory
string to the list using standard list methods, so that Python will now search
the new directory.  In my case::

    >>> sys.path.append('/Users/mb312/code')

Now we can import our custom module::

    >>> import myfunctions

.. [#on-extensions] Most Python code is stored in files with the extension
   ``.py``.  You can also write `extensions
   <https://docs.python.org/2/extending/extending.html>`_ for Python, which
   are compiled libraries that Python can also import.  You can define
   functions and classes in these files as you can for Python code in ``.py``
   files.  These files have filename extensions that depend on the platform
   you are running on.  On Linux or OSX the extension is generally ``.so``, on
   Windows, the extension is often ``.pyd``.
