####################
Cryptographic hashes
####################

Git makes great use of *hashes* because hashes make excellent unique identifiers
for the contents of files.

For background on hashes : `Wikipedia on hash
functions <http://en.wikipedia.org/wiki/Cryptographic_hash_function>`__.

A *hash* is the result of running a *hash function* over a block of
data. The hash is a fixed length string that is the *signature* of that
exact block of data. Let's run this in Python:

.. doctest::

    >>> import hashlib
    >>> sha1_hash_function = hashlib.sha1
    >>> message = "git is a rude word in UK English"
    >>> hash_value = sha1_hash_function(message).hexdigest()
    >>> hash_value
    'fec41478c4f497c1d90fd28610f4272c78a6867e'

Not too exciting so far. However, the rather magical nature of this
string is not yet apparent. Here's the trick:

There is no practical way for you to find another ``message`` that
will give the same ``hash_value``

The ``hash_value`` then is (very nearly) completely unique to that set of bytes.

For example, a tiny change in the string makes the hash completely
different. Here I've just added a full stop at the end:

.. doctest::

    >>> sha1_hash_function("git is a rude word in UK English.").hexdigest()
    '9e87add001f13aa79ed7b42a5effbfc60aa8584e'

So, if you give me some data, and I calculate the hash value, and it
comes out as "fec41478c4f497c1d90fd28610f4272c78a6867e", then I can be
very sure that the data you gave me was exactly the string "git is a
rude word in UK English".
