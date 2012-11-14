Introducing Python for Django programmers
#########################################

Understanding the basics of Python is critical for programming in
Django. Fortunately, Python is easy to learn if you already know another
language. This appendix gives you a high level overview to help you understand
Django code if you're new to Python.

First I'll explain Python as an *interpreted and dynamically typed* language,
followed by the main *data types* and *flow control* (loops and
conditions). *Structure within Python files* and *structure between Python
files* are next. To close off the chapter I look at *Python's philosophy*.


Interpreted and dynamically typed
=================================

You don't have to compile Python code every time you make a change.
Python handles compiling and optimization behind the scenes. You can try
out a Python statement, for example a print statement, and see the
results immediately. Run ``python`` (or the full path to Python if
necessary) on your commandline to display a Python prompt (which looks
like ``>>>``)::

    >>> print("Wow, a Python prompt!")
    Wow, a Python prompt!
    >>> exit()  # Or ctrl-d or ctrl-z.

All your regular Python code will be in files with the ``.py`` extension.

Python is a dynamically typed language, so it doesn't perform static type
checks. You do not have to declare your variables or the *type* of your
variables in Python. Assigning a variable is done with a single *equals*
sign::

    >>> greeting = "Hello, variable"
    >>> print(greeting)
    Hello, variable

Just assign variables and use them.


Data in Python
==============

Python uses the same basic data types found in other languages. To
program in Django, you need to understand the difference in how Python
handles that data as opposed to other languages.

Numbers
-------

When you use only whole numbers, Python treats the number as an
*integer* data type. If you use a decimal, the type is a *float*.

Python handles division differently than many other languages. As long
as there's at least one non-integer number, division works exactly as it
would on any calculator in the world. However, when there are only
integers, Python rounds the result to always return an integer.

Type this into your Python prompt for an example of Python's division::

      >>> type(2)
      <type 'int'>
      >>> type(2.0)
      <type 'float'>
      >>> 3/2
      1
      >>> 3.0/2
      1.5
      >>> 3/2.0
      1.5

As you can see in the code, 3 divided by 2 returns 1 when using only
whole numbers. When you add a decimal point to either integer, the
result is 1.5 (which is what we would normally expect). Remember, in
Python, add a decimal to integers to save yourself from strange
calculations.

.. note::

   In Python 3, this slightly weird behaviour will be gone. ``3 / 2`` will
   just be ``1.5`` as you'd expect.


Strings
-------

Strings (a number of characters) are surrounded by double or single quotes in
Python. Either choice is fine. Here's an example::

      >>> ''
      ''
      >>> 'string'
      'string'
      >>> "a book's apostroph"
      "a book's apostroph"
      >>> 'a book\'s apostroph'
      "a book's apostroph"

The last two examples show that you can use single quotes as-is inside a
double quote string (and vice versa) or that you can escape them with a
backslash.

There are two cases where you need something else than a regular string:
for international characters and for regular expressions.

International characters: unicode strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

International characters are those characters outside of the ASCII characters
range. Basically everything except a-z, A-Z, numbers and a few characters like
``-/+:;``. If you use international characters (chinese signs, IKEA product
names), you need to use `unicode <https://en.wikipedia.org/wiki/Unicode>`__
strings. Unicode is the world-wide standard for encoding *all* possible
characters.

Django always gives you unicode strings when you retrieve strings from a web
form or from a database, so you do not have to worry about the local
encodings. To save yourself headaches, you should also always use unicode
strings. Because if you don't, Python will have to do the conversion between
your strings and unicode itself. And which encoding are your strings in? Does
Python have to guess?  `Search online for unicodedecodeerror
<https://duckduckgo.com/?q=unicodedecodeerror>`_ to give you an idea of the
mess you can be in.

Python uses 7 bit ascii for its strings if you don't tell it otherwise. To get
a unicode string, prefix the string with a ``u``::

    >>> 'regular string'
    'regular string'
    >>> u'unicode string'
    u'unicode string'

The ``u``\-prefix is tedious to type all the time. Python 3 uses unicode
strings by default (handy!). To get the same unicode-only behaviour, add a
special import near the top of your files::

.. literalinclude:: /code/python/with_charset.py

When you want to use a non-ascii character in Python code, one way is with a
unicode code::

    >>> print(u'latin small letter e with diaeresis is \u00eb')
    latin small letter e with diaeresis is ë

The last example shows one way to enter non-ASCII characters in Python
code---a ``\u`` followed by the unicode code for the character (which you can
find on the `unicode website <http://unicode.org/charts/>`_)_. ``00eb`` in
this example is the code for an *ë*.

When you're writing Python files, it is easier to tell Python which
character set to use, and let Python handle the conversion to unicode.
You do this with a comment on the first line of the file:

.. literalinclude:: /code/python/with_charset.py

Many code editors also recognize the dash-star-dash pattern on the first
line. This allows you to use non-ASCII characters in your editor instead
of looking up the unicode code (which can be a hassle). The character
set used most is ``utf-8`` (an 8-bit unicode encoding).


Regular expressions: raw strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Django uses `regular expressions
<http://www.diveintopython.net/regular_expressions/>`__ in its URL
configuration, see :ref:`chapter-urls`. You use backslashes a lot in regular
expression syntax. The problem is, Python also uses backslashes to give some
characters in a string a special meaning. For examples::

    >>> print("A string with two newlines.\n\nAnd a second line.")
    A string with two newlines.

    And a second line.
    >>> print("And \ttabs \twork \t\talso.")
    And   tabs    work        also.
    >>> print("And also \b , though you won't see output.")
    And also , though you won't see output.


You see here that Python treats ``\n`` and ``\t`` as newline and tab
characters respectively. ``\b`` is the ancient bell (or beep) signal.

Here you have a problem. A ``\b`` means "whitespace at the start or end of a
word" in a regular expression. To preserve the backslash in the string, you
need to escape it with another backslash::

    >>> print("This \b is not preserved")
    This  is not preserved
    >>> print("This \\b is properly preserved")
    This \b is properly preserved


To retain a backslash in a Python string, you need to put in two
backslashes. If you have an elaborate regular expression with lots of
backslashes, all those double backslashes are error-prone and make the
regular expression harder to read.

Python gives you a special kind of string that preserves all
backslashes: a raw string. Just put an ``r`` in front of the string's
quotes::

    >>> print("The basic solution is a double backslash: \\b")
    The basic solution is a double backslash: \b
    >>> print(r"Alternative: a raw string. \b stays \b")
    Alternative: a raw string. \b stays \b

Remember, you only need a raw string's special treatment of backslash
characters for regular expressions.


Collections: lists, tuples and dictionaries
-------------------------------------------

Python has the most common collection datastructures built in, including
syntax that makes them easy to use.

Dictionary
~~~~~~~~~~

A dictionary is a key/value mapping. It is often called a *hash table*
in other languages. In Python, you create it by using curly braces::

        >>> my_data = {'name': 'Reinout',
        ...            'city': 'Nieuwegein',
        ...            'country': 'The Netherlands'}
        >>> my_data.keys()
        ['city', 'name', 'country']
        >>> my_data['city']
        'Nieuwegein'
        >>> my_data['continent'] = 'Eurasia'
        >>> my_data.keys()
        ['city', 'continent', 'name', 'country']


``my_data`` in the example above starts out as a dictionary with three
keys (name, city and country). You can access the values by asking for
the key in square brackets.

You can always add additional items to a dictionary, like
``my_data['continent'] = 'Eurasia'`` as in the example. Note that a
key's value can be whatever you want: a string, a class, even a list or
another dict.

List
~~~~

A list in Python is a modifiable list of values; you can sort it
in-place and add or remove items. You write it with square brackets::

        >>> my_kids = ['Rianne', 'Floris']
        >>> my_kids.append('Elizabeth')
        >>> my_kids
        ['Rianne', 'Floris', 'Elizabeth']
        >>> my_kids[0]
        'Rianne'
        >>> my_kids[-1]
        'Elizabeth'

Accessing items happens with square brackets just as it does with
dictionaries. A list's index starts at zero, so ``my_kids[0]`` gives you
the first kid. A negative index starts from the end, so ``my_kids[-1]``
gives you the last one.

You can change the list by appending or removing items (the latter
sounds a bit harsh when you're talking about kids).

Tuple
~~~~~

A tuple is like a list, only immutable. Once created, it cannot be
changed. This is handy for configuration; in a Django settings file,
you'll see tuples rather than lists. If you want to add something, you
need to create a new tuple. You create one by using regular parentheses
and at least one comma::

        >>> my_parents = ('Alie', 'Herman')
        >>> my_parents[0]
        'Alie'

Like lists, you access tuple items with an index between square
brackets.

You must watch out with those parentheses that indicate a tuple.  Parentheses
are also used for grouping, like ``(1 + 2) * 3``. What makes a tuple a tuple
is that there is at least one comma between the parentheses. So
``('reinout')`` is the string ``'reinout'``, but ``('reinout',)`` is a
one-item tuple.

.. _section-python-boolean:

Boolean and nothing
-------------------

``True`` and ``False`` are Python's boolean values. ``None`` is used as
*no value*.

In your Python code, you often want to test whether something is empty
or whether something exists. For instance, *if* an address field is
empty *then* print a warning. Python treats the following as False:
``None``, an empty string, zero, an empty list, empty tuple, or an empty
dictionary.


Flow control and indentation
============================

To control data, Python has conditions and loops like other languages,
but it also has *list comprehensions*, a friendly and modern way to work
without using a loop. To use any of these, you first need to understand
Python's indentation rules.

Indentation
-----------

The indentation in Python confuses many programmers when they are first
learning the language. Most programming languages use something like curly
braces to group statements, such as the blocks within an "if/else". Here is a
JavaScript example:

.. code-block:: javascript

      if (kind === "2") {
          map_type = G_PHYSICAL_MAP;
      } else {
          map_type = G_NORMAL_MAP;
      }


You see the indentation in the JavaScript, but it's not mandatory. It
just helps humans read the code. Python, on the other hand, makes the
indentation mandatory. The beginning and end of a block of code isn't
indicated by curly braces but by the start and end of indentation::

      if kind == 2:
          map_type = G_PHYSICAL_MAP
      else:
          map_type = G_NORMAL_MAP


This looks less cluttered. Since all Python code has the same indentation
rules, reading code is easy and predictable. Python code should always be
indented in steps of *four spaces*; never use tabs. Any good editor for Python
will use four spaces because `Python's style guide
<http://www.python.org/dev/peps/pep-0008/#tabs-or-spaces>`__ *strongly*
recommends it.

Conditions
----------

Python handles conditions with ``if``. If you have more than one
condition, you can add one or more ``elif`` statements. And ``else``
gives you a catch-all at the end. Here is an example:

.. literalinclude:: /code/python/if_statements.py

``==`` and ``!=`` test for equality and inequality. Everything that results in
a boolean value can be used as a condition. See also
:ref:`section-python-boolean`. You can combine conditions with ``and`` and
``or`` and negate with ``not``.

Loops
-----

Python has ``for`` and ``while`` loops. You'll almost exclusively see
``for`` loops:

.. literalinclude:: /code/python/for_loops.py
   :end-before: Nieuwegein

Two useful tricks are ``range`` and ``enumerate``. The first is for
iterating a fixed number of times. ``range(10)`` produces
``0, 1, 2, .., 9``. The second is for looping over a set of values and
for numbering them. You recieve both an index (zero-based) and the
actual value.

Dictionaries are common in Python, so you also often have to loop over
the keys or the values (or both) of dictionaries:

.. literalinclude:: /code/python/for_loops.py
   :start-after: Prints '0 Reinout'

If you loop over a dictionary without any methods, you really loop over the
dictionary's keys, just like you would when using ``.keys()``. Use
``.values()`` if you want to loop over the values instead. You may loop over
both keys and values with the ``.items()`` method, this returns ``(key,
value)`` tuples.


List comprehensions
-------------------

You often write small loops to modify lists. You can loop over the list
to remove empty items or calculate a new value for each of the list's
items. Python has an alternative to writing these small loops: list
comprehensions. With a list comprehension you can filter and/or modify a
list in one line of code instead of using a loop to do the same work.
The best way to show you is with an example:

.. literalinclude:: /code/python/comprehensions.py
   :emphasize-lines: 23

The example takes a string with a couple of empty lines and filters out the
empty lines. First, it uses a *for* loop by checking if a line is not empty
and, if not, by appending it to the result. After that it does the same with a
simple one-line list comprehension, which takes the form ``[new for old in
list if condition]``. Once you get used to the syntax, a list comprehension is
much shorter and easier to read than a loop.

Structure within files
======================

Within a single ``.py`` Python file, you can have variables and
functions. Python is also an object oriented language, so you can have classes
as well.

You are not required to use classes; simple variables and functions are
fine. Django itself uses all three. Django models are always classes, a
URL configuration uses only functions, and Django views can be either
functions or classes.

Functions and arguments
-----------------------

Python functions are defined with ``def`` like this:

.. literalinclude:: /code/python/functions.py

The last two functions contain arguments. Python has two kinds of
arguments: positional arguments and keyword arguments. A positional
argument only has a name; a keyword argument has a name and default
value.

Positional arguments are passed in exactly the order they are written.
The position, literally, must match the order you want them passed.
Positional arguments cannot be optional. When you have a limited number
of arguments with a clear order, positional arguments work well.

In all other circumstances, you'll probably want to use keyword
arguments. A keyword argument has the following advantages:

- Every keyword argument has a default value.

- The order in which the keyword arguments are passed doesn't matter.
  ``your_method(a='aa', b='bb')`` is the same as ``your_method(b='bb',
  a='aa')``.

- Your functions are easier to evolve. If you decide to add a positional
  argument, you need to update all the places where you call your function. A
  keyword argument has a default value, which means you can leave most calls
  to your function alone.

For flexibility, keyword arguments are best. You should restrict
positional arguments to those arguments that are absolutely essential to
the function and will never change.

Classes
-------

Python supports object oriented programming. You can define classes.
Here is an example of defining, instantiating, and using a class:

.. literalinclude:: /code/python/classes.py

The example shows two ways to create a class. Both use the ``class``
statement. The first way subclasses from Python's base ``object`` class.
The second way subclasses from an existing class.

A class, like in any object oriented language, contains variables and
functions. To be consistent with object oriented terminology, Python calls the
variables in a class *attributes* and the functions *methods*.

You instantiate a class by calling it, like in the example. When you call the
class, Python calls the class's specially-named ``__init__()`` method. If
``__init__()`` accepts arguments, you can pass them. In the example, you pass
the name of the author as an argument when creating the class; this ends up as
the ``name`` argument on the ``__init__()`` method.

By the way, every method must start with a mandatory first argument
called a ``self`` argument. When you call a method on an object, Python
automatically passes the object as this first argument.

Structure between files
=======================

Python files have the extension ``py`` and you can group them in
directories (*packages* in Python-speak). You can use ``py`` files from
the same or another package with *importing*.

Django is split up into many different packages by design because
grouping similar code in cohesive packages helps keep Django's code neat
and organized. You can do likewise with your own code by grouping
related code into its own package.

Modules and packages
--------------------

Python uses specific terminology for Python files and directories. A
single Python file is a *module* and several modules grouped into a
directory is a *package*.

Python does not treat every directory with modules as a package though, it
wants you to explicitly mark it as a package by adding a ``__init__.py`` file
to the directory. The file can be empty, though I always add a ``# Package``
comment in those otherwise-empty files, it can help you when you need to
manually merge code from patches.

Packages can be nested by adding subdirectories. Each subdirectory
should have its ``__init__.py`` to mark it as a package.

Importing modules and packages
------------------------------

Different Python files in different directories also means you need to be able
to refer to them in some way so that you can use them. In Python this is
called *importing*. You import modules and packages with the ``import xyz`` or
``from abc import xyz`` statement:

.. literalinclude:: /code/python/imports.py

With the ``import xyz`` style you import a whole package or module with
its full path. For instance, importing ``os`` makes everything inside
that package available using the ``os`` name, like ``os``, ``os.path``
and ``os.path.exists``.

With the second style, ``from abc import xyz``, you import something
specific without needing to use the full path. In the example, you can
just use ``exists`` because you imported it specifically; in this case
you do not need to use the full ``os.path.exists`` path name.

In both cases, you use Python's *dotted path notation*. In this
notation, every dot steps deeper into the package/module tree; for
example ``os.path.exists`` calls the ``exists`` function in the ``path``
module in the ``os`` module.


The core philosphy of Python
============================

Philosophy is build into Python. No really. And as I know you're not
ready to believe me on my word yet: fire up Python and type ``import
this`` at the prompt::

    $ python
    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Sure, there are some jokes in there, but most of the lines are for real and
several are often quoted in Django discussions! Let me highlight three:

Explicit is better than implicit
    Sometimes it is handy to automatically make something happen. Add a
    specially-named file to your project and everything in there is
    automatically registered as a URL or so. The problem is that you need to
    know all the special magic rules.

    Explicit is often clearer. Django's configuration file has a
    ``ROOT_URLCONF`` parameter, pointing at a specific Python file with a
    URLconf in it. This itself is an explicit list of which URLs match
    what. There can be no confusion over which URL matches what because
    everything is explicit.

Readability counts
    Simply keeping this one in mind will help you a lot. Single-character
    variable names are no good. Don't abbreviate too much. Use naming to help
    you. You yourself will read your own code again in half a year's time: can
    you still understand it then? Does ``dh = sgst * 1.4`` still make sense
    then? Would ``dike_height = suggested_height * SAFETY_FACTOR`` be clearer?
    Don't skimp on names. They don't have an 8-character restriction.

    And look at Python's use of indentation. Couple that with *flat is better
    than nested*. If you go too deep and use too many loops and if statements,
    Python's mandatory indentation will show you that you went too far. Python
    helps you to keep your code clean this way. It comes with a build-in
    suggestion to split up your code a bit.

Now is better than never
    A good example is Django's configuration. It is simply a Python file, so
    you can do everything you want with it. Import other files, read in
    configuration from a text file, you name it. It is not the most elegant
    solution, but when Django got made, they needed a pragmatic solution.

    Why spend years arguing? Why sink a lot of effort in finding something
    that can take all use cases? You'll be waiting forever. A good enough
    solution now is preferable to something perfect that might never come.


What we learned
===============

We learned the most common Python language elements. Enough to get started
with Django and enough to understand the example code througout this
book.

For exercises, I'll keep it simple: learn more about Python. Try it out. The
best place to start is `dive into Python <http://www.diveintopython.net/>`_,
it will take you through Python in a gentle way. For lots of exercises, look
at `learn Python the hard way <http://learnpythonthehardway.org/>`_.
