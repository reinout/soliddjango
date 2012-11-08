Getting started
###############

We've all been there. You start out building a website that is well-structured
and with clean code, but a looming deadline forces you to make compromises and
take shortcuts. Here is the solution to your problem: Django. Django is
designed to build a website fast *and* right.  Django's motto promises a lot:
"the web framework for perfectionists with deadlines". It delivers with a
structure that makes it easy to create a well-designed website.

In this chapter, first you'll look at Django's structure and how it can help
you. After that, you'll get acquainted with the website you're going to build
over the next several chapters. Finally, you'll install Django and write your
first Django code.


How Django Works
================

Django gives you rapid development and a clean, pragmatic design. By writing
your code to take advantage of Django's design, you will create a natural
structure that fits your web project. Django divides separate concerns into
separate files, helping you write solid code.

A good way to understand Django's design is to compare it to the
model/view/controller (MVC) pattern. Let's look at Django in that light:

Controller

    The controller layer is the heart of the system---it steers everything.
    For a web framework, this means handling requests and responses, setting
    up database connections and loading add-ons. To do this, Django reads a
    *settings file* so that it knows what to load and set up; it also reads a
    *URL configuration file* that tells it what to do with the incoming
    requests from browsers.

Model

    The model layer in Django is the database plus the Python code that directly
    uses it. In Django, tables in the database are represented by Python classes
    called models---you work directly with the models and Django uses them to
    manage the tables.

View

    The view layer is the user interface. Django splits this up into the
    actual HTML pages and the Python code (called *views*) that renders
    them. It also contains an automatic admin interface for editing the models
    in the model layer.

RR: remove settings from the figure IMG HERE
fileref="images/first\_taste/django\_diagram.png"

shows how Django works. Django itself is configured through a settings file. A
browser sends a request with a URL to Django. Django looks up the URL in a URL
configuration file to determine what to do with the request. It can either:

Call the automatic admin interface, which is a web interface for Django's
database content. The admin interface works directly with the model layer.

Render a custom web page. Django separates web pages into an HTML template
language and Python view code.

Underneath it all is the model layer/database integration. The admin interface
shows and edits what's in the database. The views can access the database
data, too.

Let's take a closer look at these parts.

Models: Integrating With a Database
-----------------------------------

Django stores its data in relational databases (SQL) by default. Django helps
you work with those databases by including an *object relational mapper (ORM)*
that transparently maps relational database tables to Python models. When you
use regular Python objects in your code, the ORM translates what you're doing
with those objects (reading, changing, deleting) to SQL commands.

Each model's attributes map to columns in the database table. A model also has
methods to hold your Python code that only deals with the database content (no
user interaction or user interface concerns).  Typically, this code converts,
summarizes, or filters your raw database data into a form that's suitable for
your views. Concerns remain separate in Django; your Python code which
interacts with your data directly stays separate from your view code.

Django's ORM queries the database for you. Writing big SQL queries can be hard
and relatively error-prone; with Django's ORM you can write your queries in
more readable Python code. At the same time, Django optimizes your queries,
saving you valuable time and effort.

Admin Interface: Interacting With the Models
--------------------------------------------

RR: add a screenshot One of Django's strong points is that you automatically
get a browser-based admin interface for your database models. From the luxury
of your browser you can view, edit, add, and delete objects in your database.

The interface is fully customizable. You can choose which fields to include or
to make read-only, which fields to show in the list of objects, and which
models to show. Per-field explanation text, dropdowns, and radio buttons are
all configurable.

Templates: the HTML Part of Showing a Web Page
----------------------------------------------

Django uses both Python code and an HTML template to generate a web page. You
write Python code (the view) to get the data and then the data is rendered
inside an HTML template.

Django's philosophy is to keep a template as dumb as possible. A template
renders data, so it has to have loops and conditions and instructions for
inserting the data into HTML. It also handles formatting and management of CSS
and JavaScript, for instance, but it doesn't include calculations and database
interaction.

The advantage of this philosophy is that the visual HTML aspect of Django is
pretty cleanly separated from the rest of Django. Here you can see Django's
design in action. Contrast this separation of concerns with PHP. You *can*
absolutely write clean and neat PHP code, but you yourself have to ensure
that. PHP mixes everything, including database access, inside the HTML
page. With Django, the separation of concerns is built in; you have to make an
effort to end up with dirty code.

Views: the Python Part of Showing a Web Page
--------------------------------------------

Because the templates are dumb, your Python view code has to do the heavy
lifting. The view handles tasks such as querying the data from the database
models, doing calculations on the data, and interacting with external data
sources like web services.

In practice, this separation between *dumb* templates and *smart* Python code
works well. Django forces you to do more in Python and less in the template
language, which is good as Python code is often the better place to do
things. Why? Embedding programming code within HTML tags is less clean and
harder to read and more error-prone than programming code in an actual Python
file. *a bit awkTODO for HH*

*RR: condense to one or two sentences at the top of the sect1* Note that the
Python view code is separate from the Python code in the database model
layer.\ *what does separate mean?* The character of the Python code in each is
often quite different.\ *rep?* The view code deals with lots of details like
reacting to form parameters or different kinds of users. View code can feel
like a very active bird, flying to and fro. In contrast, model code often
feels like a plow horse, plodding purposefully along.\ *why?* Django
encourages us to separate these two different kinds of Python code.\ *how does
it encourage it?*

URLs: Dispatching The Browser Requests
--------------------------------------

*shouldn't this be the first subsection because it's the first think that
happens?* Django's URL configuration files steer the whole process.  Web
browsers send URLs to Django. Django looks up the request in its URL
configuration file and dispatches it to the appropriate view or admin page.

Sending different URLs to different views or admin pages is a separate,
clearly defined task, so Django separates it out and keeps the URL handling
out of the view code.\ *how? wouldn't this be better in the overview*

Settings: Configuring Django
----------------------------

*maybe this is better just in the overview too, and talk about the details
when you start building something* Django can be configured in detail, which
is done in a *settings file*. Because Django promises rapid development, it
has sensible defaults for most settings. However, you *need* to set which
database to use.

You can use the settings file to add configuration to your own Django
applications. A settings file is just a Python file, so you are free to add
your own configuration. If, for instance, you need to use a developer ID for
Google maps, you can make it configurable by looking for a
``GOOGLE_MAPS_DEV_ID`` in the settings file. Django doesn't mind if you add
extra items to the settings file.

Introducing the Castle Website
==============================

A book like this works best when you've got an example to follow. It gives you
something solid to hold on to. And as you're invited to build the example
yourself, too, you get lots of exercises which help you learn everything.

I picked a fun example, more fun than the number one "let's build a weblog"
example, or building a bookstore or a cookbook website.  We're going to create
a website for a medieval duke's new castle. The anachronism will help you
focus on Django, instead of on the actual example. At least, that's my goal.

Let's start with some background on the duke and the castle website, and a
peek at what the castle website will be when we've finished it.

The Duke's New Castle
---------------------

Duke Folcmar rules over a wooded realm with gentle hills, a river and several
important trade roads. We'd like to say that the welfare of his people is
foremost on his mind. Unfortunately, we can't. He cares for his people
somewhat indirectly. The three things that are most important to Duke Folcmar
are:

PR

The image that he projects. As a medieval lord, reputation is
everything. Tales of his strengths or weaknesses change the way his
not-always-friendly neighbors deal with him. If bards sing songs of his
prowess and praise the might of his army, other lords treat him with respect
and offer tokens of peace. Stories of weakness encourage these same lords to
test Duke Folcmar's mettle with petty wars and skirmishes.

Power

Power relative to his neighbors. Treaties mean nothing, power means
everything. For the surrounding nobility, power is measured best by the size
of the realm you hold. Duke Folcmar has a neighbor that has constructed a
small keep on his border, giving nearby commoners and passing traders the
sense that he, not the duke, is the true lord of the land. Unacceptable.

Trade

Land is one thing, but trade brings in the coin of the realm. Money is
influence, prestige and can pay a mercenary army. Traders don't mind tolls on
their journeys if they are well-protected and can be assured of speedy and
safe travels. After contemplating his coffers, the duke has decided to
proclaim his realm as the duchy of road safety. Funding a campaign to flush
out most brigands and eliminate the two robber barons along the main trade
road will cost the price of a grand tournament, but the increase in trade,
taxes and toll tariffs will offset it in a few years' time.

Duke Folcmar has devised a plan to address all of his concerns. First, he will
build a mighty castle that will be the new ancestral seat of power for his
line: good PR. Second, he will strategically place it near the pesky keep of
that unfriendly neighbor, demonstrating his power.  Third, it will also watch
down over the main road, promoting trade.

Finally, the duke's plan requires a castle website, and he has selected us to
do it. Let's listen to the duke explain it to us:

Good morning. I will build a new castle named *Niederburg*. It will be sited
near the main trade road so that I can protect the merchants. My builders have
found a location in a bend of the river so that the castle will be nigh
unassailable on three sides. The castle assuch will be the envy of all my
opponents. It is, however, not enough that the castle is perfect: people have
to *know and hear* that it is perfect. Therefore, I require a website. You
will build it for me.

Wow, Duke Folcmar, thanks for ordering us to build the website for your new
castle. But, pray, tell us more about what you require of us.

You have rightly noticed that a simple homepage with a photo of the castle is
not what I desire. My goal with the website is twofold. On the one hand I want
good PR. Lots of info on the castle, on my family line, on my history. And on
my mission of protecting trade on the main road.

On the other hand, attracting trade is another goal of the castle's
website. Information on how I protect the road. Monthly statistics on the
amount of highway robbers my armsmen capture and string up. And later I want
the traders to submit their schedule via the website so that I can plan my
armsmen's deployments better. Let me be absolutely clear on this point: I can
not brook any security breaches of the website. I do not want highway robbers
to get a trader's schedule out of my database. If that ever happens I will let
my executioner explain the meaning of *deadline* to you.

Do not worry, Duke Folcmar, we will use Django to make the website. It is a
web framework for perfectionists with deadlines. Django has very good
protection against most common kinds of attacks, just like your new castle.

Do not bore me with technical details. Start coding and show me something by
next week Thursday. Off with you.

The Finished Castle Site
------------------------

RR: remove *is this subsection needed? why does the reader need to know what
will be in the finished site now?* The first two parts of this book teach you
the core of Django. In them, we'll build the full castle website, chapter by
chapter and subject by subject. Here's a taste of what we'll include in the
website: *RR: Review this list after the first two parts of the book are
finished to check if the order is still correct.*

Of course a great look-and-feel including CSS stylesheets, images and
JavaScript.

Information on villages and towns in the area; especially their lodging
facilities. To help traders traveling through our area.

News and statistics on our duke's accomplishments to impress his neighbors and
to deter would-be highwaymen. Making a *consistent* name for himself and
providing *accurate* information help etch that name and those accomplishments
in everyone's mind.

A protected part of the website to allow traders to notify the duke's armsmen
of their travel schedule (really protected, mind you). This should help in
getting maximum efficiency out of the patrols.

For the PR, information on the duke, his illustrious family line and the
castle itself.

A protected part of the site will include data on the personel of the castle,
including the armsmen.

We'll add these parts one by one to the website, keeping it working the whole
time. *RR: condense above list to two sentences*

Django lends itself to iterative development: use that to your advantage. This
is a good way to build any Django website. After you finish this book, you can
use this approach when you build your own projects.

Iterative Development
---------------------

*shoule this be a sect1 so it shows in the TOC? maybe combined with a little
bit from the previous section about iterative?* *RR: sect1* There are many
separate moving parts in a website: the database structure, the visual
look-and-feel, the user interaction, the URL structure. All these parts are
related. What needs to be shown in the user interface determines what has to
be in the database, the look-and-feel depends on the URL structure, the URL
structure depends on the database structure, and so on.

There are basically two main ways to develop. *Big design up front*, where you
try to plan everything beforehand. A big elaborate plan. The other way is
*iterative development*. You take small steps and try to work your way towards
the goal, making small corrections all the way.

A twist on iterative development is tracer bullet development. (Or in Duke
Folcmar's case, *flaming arrows*.) To ensure the iterations stay on target, we
first build the entire system. *no, only part of it* Just a small part of the
entire system, but something that at least goes all the way from the database
all the way to the user interface. There are lots of bits and pieces missing
and you probably have to fake a lot, but you know where you are aiming. You
have a complete system; you *only* have to flesh it out.

The name *tracer bullet development* comes from the analogy of trying to hit a
target at night. You can take a cannon and calculate the correct angle and
elevation based on wind speed, temperature and target location. Fire and hope
your calculation was correct. An alternative is to use a machine gun with
tracer bullets. That means that every tenth bullet is phosphorous: it gives
light. So when you fire, you see a stream of light going exactly where your
bullets are going. Instant feedback, allowing you to adjust iteratively until
you hit the target.

*some repetition in this para* In this chapter, we're starting our own tracer
bullet development. We'll build a simple working example from start to
finish. Even though it will be simple, it will use every part of Django, from
URL handling via views and the admin interface to the model layer. When it's
done, we'll get feedback and we can aim again with another iteration in the
next chapter. Throughout this book we'll build out this simple working example
until we have a completed website.

Installing Django
=================

Next step is to install Django. Whether you use OSX, Linux or Windows; you'll
find handy instructions on how to install Django here. (If you're already
familiar with Python and Python packages, you're invited to read the Python
packaging comments in .)

What You Need
-------------

Here's what you need to set up before you can start trying out Django:

Python

Django is written in Python, so you first need to install Python.
Fortunately, it is often already available.

Regarding Python versions: you need 2.5, 2.6 or 2.7. (Django doesn't work with
version 3 yet.) If you have a choice of versions, pick 2.7.

When programming a Django website and when interacting with Python, some
commands have to be typed in on the *console*. Other familiar terms for the
console are the terminal and the commandline or DOS prompt.

Setuptools

Like many other programming languages, Python comes with its own installer for
extra Python packages, called *setuptools*. (Setuptools is sometimes called
distribute: they're the functionally the same.)

Django itself

Setuptools provides the ``easy_install`` command, which you'll use to install
Django.

This book assumes Django version 1.4 or higher. Django emphasizes backwards
compatibility, so a different version will not be a problem.  If you use a
different version and see a difference between your display and the examples
in this book, check Django's online documentation which is full of helpful
notes like "changed in 1.2" and "added in 1.4".

need a segue here

OSX
---

Python is included with OSX, so you're set. Type ``python`` into your console
prompt and you'll see the version number, which will be 2.6.4 or 2.7.1 or
something similar. To exit the Python prompt, press Ctrl-d (or type ``exit``).

Setuptools (and thus the ``easy_install`` command) comes pre-installed on
OSX. On your console, run the following command: ``sudo easy_install
Django``. ``sudo`` runs ``easy_install`` in system administrator mode; without
it you get a warning that you do not have the necessary permissions.\ *without
it? you mean you have to be logged in as SA?*

Linux
-----

Almost always, Python is already installed for you. Test it by typing
``python`` in your console. If not, use your package manager to install it. On
Debian/Ubuntu, the command is ``sudo apt-get install python``.  You can use
your graphical package manager, too. Make sure you've got a 2.5/2.6/2.7 Python
installed.

Setuptools isn't always installed. Try to run ``easy_install`` on the
console. If it is not available, install it with your package manager.  On
Debian/Ubuntu the command is ``sudo apt-get install python-setuptools``.

Now run ``sudo easy_install Django``. This installs Django globally.

Windows
-------

On Windows, you have to install Python yourself. Go to the `Python download
page <http://python.org/download/>`_, pick the 2.7 Windows installer, download
and install it.

In the console, type ``python`` to make sure Python is installed OK.  You'll
see a version number: 2.7.2 or higher. To exit the Python prompt, press Ctrl-z
(or type ``exit``).

For setuptools, download a `Windows installer
<http://pypi.python.org/pypi/setuptools>`_ that matches your Python version
(look near the bottom of the page) *what page?* and install it.\ *install
what? the installer?*

Afterwards, go to the console and install Django with ``easy_install Django``.

Our current installation process installed Django globally. Globally means
that wherever we open our Python prompt, we'll have Django available. However,
we might need to work with multiple Django versions or might want to keep our
global Python clean. That's all possible and we will dive into just that in .

For this and the next few chapters, the quick global install will serve our
purposes.

Creating Your Django Project
============================

With Django installed, you can now use it to create your basic project
structure. Afterwards you must adjust two settings: one for the database and
one for the list of installed Django applications. Then you can create the
database and start Django. *what is a project?*

Creating the Structure With Startproject
----------------------------------------

*they didn't install the script - it was part of the install. split up
sentence into two* When you installed Django, you also installed a
``django-admin.py`` script, which is how you communicate with Django from the
console when you're not working inside a project. Type ``django-admin.py`` at
the console and you'll get a list of available subcommands. The list of
subcommands is pretty long, but you can always get help on any one of them.

To begin, only one of the subcommands is needed: ``startproject``. Let's look
at the help for startproject. You can get the help in two ways:
``django-admin.py help startproject`` and ``django-admin.py startproject
--help``:

::

            $ django-admin.py startproject --help
            Usage: django-admin.py startproject [options] [projectname]

            Creates a Django project directory structure for the given
            project name in the current directory.


We need to name our project. Since it's a website for the duke's new castle,
the project name *castle* makes the most sense.\ *how do they name it? show
the line of code they need to type in*

Project names have one important restriction: they should be valid Python
names because you need to be able to import them. For instance, if you have a
name with a dash in it, Python treats it as a minus sign.  So it complains
about unknown identifiers when subtracting: ``import project-name.models``.

Likewise, a dot in a name is not a good idea. ``import project.name.models``
*is* possible, but Python treats those dots as separators. Technically, Python
calls ``project.name`` a namespace package. If you come from Plone, a Python
content management system (CMS), you'll be used to namespace packages. But
Django has some restrictions and doesn't really like them. So don't use a dot.

One character is absolutely forbidden: a space. A space separates words.  A
space separates variables. A space separates. ``import project name.models``
gives a syntax error. Using spaces in filenames is second nature to most
people, but when programming Django do not use spaces in filenames.

Underscores are OK. I work on a system called *Lizard* and my packages are
called lizard\_ui, lizard\_map, lizard\_security and so on. If your project's
name really consists of multiple words or if you want a common prefix:
separate the words with underscores.

No more delays.\ *remove - there hasn't been a delay. show the following on a
separate line* Call ``django-admin.py startproject castle``. *RR: command on a
separate line*. The result is anticlimatic, as nothing is printed. So call up
your explorer/finder/file browser to see the results. See .

Startproject created five files for you:

``castle/__init__.py``

A Python requirement. An ``__init__.py`` turns a directory into a Python
module. So if you want to import from something, that something needs an
``__init__.py`` in there.\ *what is a pyton module? why would i import
something?*

``castle/settings.py``

The project's Django settings. This is just Python code, so make sure you
don't make Python syntax errors. We'll look at this file in the next few
pages.

``castle/urls.py``

This file maps incoming URLs to whatever Django itself needs to do. The next
chapter will explain how it works in detail; later on in this chapter you'll
see enough to get Django running.

``castle/wsgi.py``

WSGI (Web Service Gateway Interface) is Python's standard mechanism to run
Python code on a web server. WSGI is lovingly pronounced as "wiskey", by the
way. (We ought to mention that to the duke someday!) We'll look at web server
integration, and WSGI, in a later chapter.

``manage.py``

When you create a project, Django creates a copy of ``django-admin.py`` named
``manage.py``. You'll use ``manage.py`` to communicate with Django from the
console when you're working inside a project. The only difference from
``django-admin.py`` is that your project's Django's main settings module is
configured by default.

We'll use this command throughout the book as this is our way of telling
Django to do things for us: starting the build-in web server, setting up the
database, exporting data, importing data, and more. If you type in
``manage.py`` in the console, you get a long listing of available subcommands:
more than 30. You can always get help on any one of them by typing in
``manage.py help xyz``. Especially handy if you don't remember which of
the---often similarly named---subcommands you have to use.

The examples in this book use Django's 1.4 default project structure. If
you're using an older version you need to adjust in two ways.

Django 1.4 is the first version that puts everything in a subdirectory when
you create a new project. So if you're using an older Django version, you'll
have a flat list of files. The best idea is to adjust your project to the
newer structure by doing it manually, or by downloading the example code for
this chapter.

Before Django 1.4, you needed to set an environment variable
``DJANGO_SETTINGS_MODULE`` pointing at your settings file. The value must be
in Python's *dotted path* notation, in our case ``castle.settings``. In Django
1.4, ``manage.py`` adds the environment variable automatically; it adds a
``os.environ.setdefault`` line in the ``manage.py`` file:

CODE HERE file="code/first\_taste/01/manage.py"

You can either continue setting the environment variable manually, or you can
add the ``os.environ.setdefault`` line to your ``manage.py``.

You need to fill in *configure* two things in the generated
``castle/settings.py``: the database settings and the installed applications.

Configuring the Database Settings
---------------------------------

Django stores its data in an SQL database, so you need to configure one.
Python makes this easy for you, as the `SQLite database engine
<http://www.sqlite.org/>`_ is included with Python.\ *you can use...but we're
going to use SQLite* SQLite is a simple database that is stored in one single
file. It's easy to copy and remove, and handy during development. Django can
talk with many databases, but for the moment we'll stick to SQLite.\ *earlier
in para*

In ``settings.py`` we need to change ``DATABASES`` to use SQLite. This is the
code:

and change that to:

As you saw, Django provides helpful comments in the generated settings file,
but you may want more guidance and explanation. The best course of action is
to search for it online. For the ``DATABASES`` setting, search for *Django
settings databases*. Almost always, `Django's own documentation
<https://docs.djangoproject.com/en/dev/ref/settings/#databases>`_ comes out on
top, and there you'll find a full explanation of all settings.

Configuring the Installed Django Applications
---------------------------------------------

An *application* is Django's term for an extention to core Django.  Django
itself already contains a handful of applications (``django.contrib.*``), so
you can enable and disable parts of Django, like the admin. Most of the
applications are packaged separately from Django. You can add blog apps,
database migration apps, CMS apps and so on. Look at
http://www.djangopackages.com/ to get an idea of what's available. We will see
a number of those applications later on in this book.

You need to enable two applications: your own castle project and Django's
admin interface. The ``INSTALLED_APPS`` setting, as generated, looks like
this:

Place your own castle application at the top of the list. (Technically, it is
a Python *tuple* instead of a Python *list*, but the distinction doesn't
matter here.) Several parts of Django use the order in ``INSTALLED_APPS`` to
allow an application to override templates and icons of applications lower
down, which is why you want your application right at the top.

For the admin interface, uncomment the two lines that Django already provided
for the admin and admindocs. Here's the new version:

Watch out for one Python gotcha: string concatenation. If you forget a comma
at the end of a line here, Python concatenates that line's string with the one
on the next line. Django then complains that it cannot find the
``django.contrib.sessionsdjango.contrib.sites`` application, for instance.

Creating the Database
---------------------

The next task is to tell Django to set up the database tables. You need *to
run?* the ``manage.py`` subcommand *syncdb* to create the database
tables. Answer *yes* when asked to create a superuser: without it you cannot
edit anything in the database.\ *what is this doing? what are the following
tables? when do you naswer yes?* *RR highlight 'yes' line, explain where the
tables come from*

::

            $ bin/python manage.py syncdb
            Creating tables ...
            Creating table auth_permission
            Creating table auth_group_permissions
            Creating table auth_group
            Creating table auth_user_user_permissions
            Creating table auth_user_groups
            Creating table auth_user
            Creating table django_content_type
            Creating table django_session
            Creating table django_site
            Creating table django_admin_log

            You just installed Django's auth system, which means you
            don't have any superusers defined.
            Would you like to create one now? (yes/no): yes
            Username (leave blank to use 'reinout'): admin
            E-mail address: reinout.vanrees@nelen-schuurmans.nl
            Password:
            Password (again):
            Superuser created successfully.
            Installing custom SQL ...
            Installing indexes ...
            Installed 0 object(s) from 0 fixture(s)


You now have a ``castle.db`` (we configured that name in our
``settings.py``). Because we use SQLite as our database, which is a simple
one-file database, Django actually creates the database file for us when we
run syncdb. If you use PostgreSQL or MySQL or another database, you will need
to create the database with your database management tool before Django can
create the tables.

Because it is a one-file database, if something goes wrong, you can always
simply delete and re-create it. It's one of the advantages of using SQLite.

Starting Django
---------------

Your database is now in place. You can see an SQLite database called
``castle.db`` in the project's directory. Now you can start up the site.  Run
``manage.py runserver``:

::

            $ manage.py runserver
            Validating models...

            0 errors found
            Django version 1.4, using settings 'castle.settings'
            Development server is running at http://127.0.0.1:8000/
            Quit the server with CONTROL-C.


Django now runs on port 8000 on your computer! Point your webbrowser at
http://localhost:8000/. You ought to see an "It worked" web page like .

IMG HERE fileref="images/first\_taste/it\_worked.png"

*Reinout: ctrl-c for stopping, restart normally works* Django will keep
running until you press Ctrl-c. Often you do not need to do this yourself,\
*do what yourself? press ctl-c?* however, because Django detects when you make
changes to your project and restarts itself. This is very handy during
development. However in some cases, it cannot reliably restart, for instance
when you make changes to the settings file. If you see that Django fails to
restart, you can stop and restart it yourself.

Working With Databases
======================

Django gives us a handy build-in admin interface for our database data.  It's
a major asset to Django; it's free, customizable, works through the browser,
and you use it to view, edit, add, and delete data. We're going to experiment
with it and then add a simple database table (a *model*) so you can see how
easy it is to use.\ *make this a better intro to the whole section. what is
the Big Point of this section?*

Trying Out the Admin Interface
------------------------------

To see the admin interface, Django needs to be told which URL to use to
display the admin interface. The customary choice is ``/admin/``. The next
chapter explains fully how the URL mechanism works; for now just adjust
``castle/urls.py``.\ *what si the following? what shoudl the reader do?*

CODE HERE file="code/first\_taste/02/castle/urls.py"

RR: remove admindocs, you need to have docutils installed. Move to packaging
chapter.  Follow the suggestions in there and uncomment the admin and
admindocs lines. Note that the admin and admindocs applications are available
since you enabled them in the ``INSTALLED_APPS`` list in ``settings.py`` in
the previous section.

In the ``urls.py`` you have one task left: tie the apps to a URL.\ *what apps?
more mentoring* Modify it like this:

CODE HERE file="code/first\_taste/03/castle/urls.py"

We uncommented the URLS, so Django now sends all URLs starting with ``admin/``
to Django's admin interface. And everything starting with ``admin/doc/`` goes
to the admin documentation.\ *why is this in the database section?*

You can now go to http://localhost:8000/admin/ and log in with the admin
username/password you typed in when creating the database with ``manage.py
syncdb``. See . (In case you forgot your password, you can call ``manage.py
changepassword yourusername`` and change it.)

IMG HERE fileref="images/first\_taste/admin1.png"

*will this be a standard feature?* *RR: move to end of chapter* Exercise: take
ten minutes to add a couple of users, delete some, edit them, and view them,
to acquaint yourself with the admin interface.  (Just don't delete your own
user account.)

Creating a Model
----------------

In we'll take a deep look at Django's database models. In this chapter we only
want to get a first taste of how Django handles database content.

What could be better for our first database content than to add data on our
duke and his ancestors? We need a ``Duke`` table and every ancestor needs a
name. That is enough for now.

In Django, you describe your database tables in models, which are Python
classes that are subclasses of ``django.db.models.Model``. The class's
attributes are columns in the database. You put your models in a file called
``models.py``.\ *provided for you by django install?* Django will read
models.py and build the database. So edit ``castle/models.py`` and add the
following code:

CODE HERE file="code/first\_taste/03/castle/models.py"

``Duke`` subclasses Django's ``Model``; in this way, you tell Django you want
a matching database table and that you want Django to interact with the
database table while you work comfortably with the class. Any attribute (like
``name`` here) that is an instance of a Django database field maps to a column
in the database table.

With the last line, you register your ``Duke`` class with Django's admin
interface. If you don't register it, it won't show up in there. You can now
browse the admin till you get to `the Duke page
<http://localhost:8000/admin/castle/duke/>`_. We get an error there:
``DatabaseError at /admin/castle/duke/, no such table: castle_duke``. The
table doesn't exist yet because we added our model, but didn't tell Django to
modify our database. So call ``manage.py syncdb`` and you'll see the message
``Creating table castle_duke``. Re-visit the admin page and add some dukes;
this gets you even more acquainted with the admin interface. (And it gives you
some sample data to work with in the next section.)

Adding a Web Page: View Plus Template
=====================================

Now that we have looked at *created?* Django's database layer we can switch
our attention to the web pages. We'll create a simple homepage for the castle
first. After that we'll integrate everything by using database content in a
second web page.

Simple HTML-only Template
-------------------------

A web page in Django consists of two parts: some Python code (the view) and an
HTML page with some placeholders (the template). Let's start simple with just
a plain HTML template and a minimal view for the homepage for the
castle. Templates are placed in a ``templates/`` subdirectory, often with an
additional subdirectory in there named after your project.

So create a ``homepage.html`` in ``castle/templates/castle/``:

CODE HERE file="code/first\_taste/04/castle/templates/castle/homepage.html"

The Python code *for the template? how does this all fit together?* goes into
``castle/views.py``. You only have to tell Python to render the
template. Create the file and put this code in to it:

CODE HERE file="code/first\_taste/04/castle/views.py"

The only task left is to tell Django which URL to use.\ *use for what?* You
can use the first example URL in ``castle/urls.py`` that startproject
generated for you and adjust it to your needs. Adjusting the example URL is
easier than typing a line from memory.\ *huh? what's going on?*

Now visit http://localhost:8000 in your browser. You should see your homepage
(see ).

Coupling Our Model With a View Plus Template
--------------------------------------------

We have templates and views on the front end; we have models on the back
end. It is time to link them together so that the dukes from our database
model show up in the template.

You won't need to write your own SQL query: Django's database layer will write
the SQL queries for you. Django handles nearly everything, from simple selects
to complicated joins to geographical queries. Even so, Django still lets you
write your own custom queries, should they be needed.

Add this ``dukes`` view to your ``castle/views.py``:

CODE HERE file="code/first\_taste/05/castle/views.py"

To do the equivalent of ``select * from dukes``, you use
``Duke.objects.all()`` in your Python code. This returns all dukes from the
database. You'll need to pass the list of dukes you get out of that query to
the template. By design, Django templates are not very powerful---Django wants
you to do most of the work in the view. One way Django enforces this is that
the only thing you can pass to a template is a Python dictionary. A dictionary
is a key/value mapping, something also called a *hash table* in other
languages.

In this example, we pass the dictionary to the template at the end of
``dukes``. In Python, you put the key/key value pairs in curly braces, which
is the syntax for a dictionary (like ``{'key1': value1}``). Those key/value
pairs are called the *context* of the template, so Django calls it the
*context dictionary*.

The ``dukes`` view needs a ``templates/castle/dukes.html`` template that loops
through the list of dukes and displays them:\ *is the reader supposed to build
this?*

CODE HERE file="code/first\_taste/05/castle/templates/castle/dukes.html"

*not very mentoring. what about the code you're building* You can get a good
idea of what Django's template language looks like from this template:

The template is clear, valid HTML. The Django-specific items are cleanly
separated, which helps a lot when editing the templates. You can focus on the
HTML structure and the Django-specific items independently from each other.

Django uses ``{% ... %}`` tags, like the for/endfor loop in the ``dukes.html``
template, for Django-specific instructions. For instance instructions for
loops, conditions, inserting snippets of HTML and managing CSS and JavaScript.

You passed a dictionary from the view to the template. The dictionary's items
can be inserted into the HMTL with ``{{ ... }}``.

In your template, you first iterated over the context dictionary's list of
``dukes`` with ``{% for duke in dukes %}``. ``{{ duke.name }}`` then inserted
the name of the duke into the HTML.

We need to hook this view and template up to a URL. To get a page like , add
the following line to ``castle/urls.py``:*and what do they do after they add
the line? how do they run it?*

*the summary section says what's next so you don't need it here too.  just
wrap up this section* We've made two web pages, including one that shows
database content. We saw *something* in our browser, but of course that's
nothing we want to show to his lordship the duke yet. In the next chapter
we'll dive in deeper and learn the most common template techniques. And we'll
learn all we need to know about URLs.

What We Learned
===============

Success: we got a simple website running with Django. We learned how to
install Django and how to give it commands---for instance to start up the
webserver or to create a database---and how to configure Django. We learned
about Django's built-in database admin interface and how to work with database
content ourselves. Lastly, we learned to create simple web pages with views
and templates, including tying it together with URLs.  Our last example
integrated everything from the database to the web page via URLs, a view and a
more elaborate template. *"we" did not learn. you taught. the reader learned*

We will try out URLs, views and templates in detail in the next chapter.  It
is the visible part, the front end, of our web site. It is what the duke will
see first, so that's why we'll concentrate on Django's front end first.

Here are some exercises that can help make you more familiar with what we
learned in this chapter:

Call help on all management commands (``manage.py help dbshell`` and so.) See
if you can understand what they do and how they work.

Add, edit and delete some users to familiarize yourself with the admin
interface. Sort on fields. Try bulk-deleting.\ *??*

Change the homepage view to pass the name of the castle in its context
dictionary. And change the homepage template to show the name from the
context.

Add a link to the dukes page in the homepage template. First do it just in
plain HTML. Second, Google for Django's ``{% url %}`` template tag and see if
you can get the URL in via its name. Hint: we gave the ``dukes/`` URL a name
in our ``urls.py``.



Work in progress TODO stuff
===========================

TODO: from
http://reinout.vanrees.org/weblog/2010/05/25/jan-lehnhardt-keynote.html: On
twitter, @jacobian said I’m pleased to hear @janl talk about the inherent
tension in Django’s “perfectionists with deadlines” slogan. Too true.
