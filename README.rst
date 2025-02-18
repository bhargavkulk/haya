======
 Haya
======

``haya`` is a static-site-generator written in python. It is powered by ``docutils`` to parse ReStructuredText which ``haya`` uses as its markup language. ``haya`` also supports templating through the ``mako`` templatig engine which allows embedding arbitrary Python code in the template.

``haya`` expect all ``.rst`` files in a folder called ``content``, ``.css`` files in a folder called ``css`` and ``.scss`` files in a folder called ``scss``. You can run ``haya`` by calling::

  haya build

This command will build the static site and place it in a directory called ``docs``.

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

``haya`` comes from the Sanskrit word ``Hayagriva`` (हयगीवा) which is the name of the horse-headed incarnation of the Hindu God Vishnu. Hayagriva is considered as a god of wisdom and **knowledge**, which seems related to websites.
