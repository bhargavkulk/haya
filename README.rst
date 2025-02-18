======
 Haya
======

``haya`` is a static-site-generator written in Python. It is powered by ``docutils`` to parse ReStructuredText which ``haya`` uses as its markup language. ``haya`` also supports templating through the ``mako`` template engine which allows embedding arbitrary Python code.

``haya`` expects all ``.rst`` files in a folder called ``content``, ``.css`` files in a folder called ``css`` and ``.scss`` files in a folder called ``scss``. You can run ``haya`` by calling::

  haya build

This command will build the static site and place it in a directory called ``docs``.

Installation
============

I have not come around to publishing this to PyPI, so you can install ``haya`` by running::

 pip install git+https://github.com/bhargavkulk/haya.git#egg=haya

An example on how to use ``haya`` with GitHub Actions can be seen `here <https://github.com/bhargavkulk/bhargavkulk.github.io/blob/main/.github/workflows/static.yml>`__.

Features
========

``haya`` supports:

- html templating
- scss compilation
- indexing folders (useful to make blogs)

Indexing
--------

Folders to be indexed should start with an underscore(e.g. ``_blog``). Each file in the index should follow the following format: ``YYYY-MM-DD_name.rst``. A ``_blog`` dictionary will be available in non indexed files, with the primary key being the date on the file name. Indexed files will be parsed written to html before non-indexed files.

Future Features
---------------

- Allow indexing through ``_index.toml`` files.
- Footnotes
- Bibliography generation through ``BibTex`` files
- Config file to change how ``haya`` works.

The Name
========

``haya`` comes from the Sanskrit word ``Hayagriva`` (हयग्रीवा) which is the name of the horse-headed incarnation of the Hindu God Vishnu. Hayagriva is considered as a god of wisdom and **knowledge**, which seems related to websites.
