"Solid django" book project
===========================

You're looking at the source code for my (`Reinout van Rees
<http://reinout.vanrees.org>`_) Django book project. The actual book content
is in the ``doc/source/`` directory, the rest in here is build scripts and so.


License
-------

.. raw:: html

   <a rel="license"
   href="http://creativecommons.org/licenses/by-nc-nd/3.0/"><img alt="Creative
   Commons License" style="border-width:0"
   src="http://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png" /></a><br
   /><span xmlns:dct="http://purl.org/dc/terms/"
   href="http://purl.org/dc/dcmitype/Text" property="dct:title"
   rel="dct:type">Solid Django</span> by <a
   xmlns:cc="http://creativecommons.org/ns#" href="http://reinout.vanrees.org"
   property="cc:attributionName" rel="cc:attributionURL">Reinout van Rees</a>
   is licensed under a <a rel="license"
   href="http://creativecommons.org/licenses/by-nc-nd/3.0/">Creative Commons
   Attribution-NonCommercial-NoDerivs 3.0 Unported License</a>.<br />Based on
   a work at <a xmlns:dct="http://purl.org/dc/terms/"
   href="https://github.com/reinout/soliddjango"
   rel="dct:source">https://github.com/reinout/soliddjango</a>.

Currently, I've licensed it under the `creative commons attribution
non-commercial no-derivs license
<http://creativecommons.org/licenses/by-nc-nd/3.0/>`_.

This means it is open source, but pretty restricted. I want it to be my own
book while I finish it. That's the nature of a good book: one person at the
steering wheel. Once I've finished it I'll make it a less restrictive
license, probably. I'll have to see how it plays out monetary-wise, to be
honest. I want to earn some money with this book (to pay back my study debt)
and I have to reconcile that with my desire to have a less restrictive open
source license. I want to make sure that the book doesn't languish if I move
on from Django (though I'm not planning to). Actually, I'll make the promise
right here that I'll drop the non-commercial and no-derivatives conditions
once I let this book languish. Someone else can take over then, if desired.

One **excemption regarding no-derivatives**: it is OK to fork the project on
github to provide me with spelling corrections. I really don't know if that's
the handiest way. But if it turns out to be handy: feel free. I won't treat
you as a co-owner of the book contents, though :-)


Timeline
--------

I'm writing a book on Django. Preliminary goal: get a very basic version out
by late december 2012, in time for Django 1.5.

After that, continue working on the book until the important parts are
finished. After that, if enough people like the book, continue adding the
not-core parts that I'd like to add.


Example source code
-------------------

I asked a `question on stackoverflow
<http://stackoverflow.com/questions/13296931/using-git-for-managing-a-books-example-source-code-how-to-propagate-changes>`_
on how to use git to manage the example code and got some good tips. So here's
the setup:

- The example project's code is in a separate repository, like a regular
 project.

- The book repository has a bunch of directories per chapter with versions of
  the example project in various stages of progression. These are extracted
  from tags in the code repository.

- I can package up all those examples if I want as a zipfile. Not sure if I
  want to, though.


Internet centric
----------------

This book originally started as a book for a regular publisher, so intended
for an epub/pdf version and a real printed dead tree one.

The deal fell through (=I was too slow). So I'm on my own now. So I'm slowly
building the book and releasing it as it goes. And I'm doing an HTML version
as that's OK with me and handier for lots of people. And it gives more google
juice and exposure, which I'll need even more now that I don't have a
publisher.

Treating the HTML version as the currently main one gives me the possibility
to do some more internet-like tricks:

- Links to github versions of the code.

- Videos. Handy to make it really *me* that writes the book. HTML code is easy
  to copy, but a video is harder to re-make. And coupling videos with a book
  isn't something I've seen yet: I'm looking forward to trying it out.

- Pointing at the official Django documentation! It is very good and there are
  lots of things I won't bother to write down, like a full list of field
  types: just look it up in the official documentation!

Later on I might do a proper PDF and epub version. I'm writing the book with
Sphinx, so technically it is no problem.
