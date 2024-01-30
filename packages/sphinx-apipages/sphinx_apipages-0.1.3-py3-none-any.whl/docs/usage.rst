Usage
=====

In your sphinx_ config file
(e.g. ``docs/conf.py``)
add

.. code-block:: python

    extensions = [
        # ...
        "sphinx_apipages",
    ]

And make sure to not list
``sphinx.ext.autodoc``
and
``sphinx.ext.autosummary``
there,
as those are automatically
added by ``sphinx_apipages``.

For each (sub-)module
you would like to generate API documentation,
add a file with the name of the module
to ``docs/api-src/``
and list the functions/classes
to include with ``autosummary``,
compare :ref:`API documentation example with audb <audb>`.

When building the documentation,
``sphinx_apipages`` will copy all files
from ``docs/api-src/``
to ``docs/api/``,
and generate RST files
for each class and function,
and store them under ``docs/api/``
as well.


Configuration
-------------

The following configurations are possible.

``apipages_src_dir``
    | Folder holding the API source files.
    | Default: ``"docs/api-src"``

``apipages_dst_dir``
    | Folder storing the generated RST files from which the API documentation is build.
    | Default: ``"docs/api"``

``apipages_hidden_methods``
    | List of hidden class methods that should be included in class documentations.
    | Default: ``["__call__"]``


Custom templates
----------------

You can overwrite
how functions and classes are documented
by providing `custom templates`_.
E.g. you can create a file
``docs/_templates/autosummary/class.rst``
to specify how classes are rendered.
You will need to add ``templates_path = ["_templates"]``
to your sphinx_ config file
(e.g. ``docs/conf.py``).
Inside the template you can access the ``apipages_hidden_methods`` list
by ``hidden_methods``.

The default templates for classes is ``autosummary/class.rst``:

.. literalinclude:: ../sphinx_apipages/templates/autosummary/class.rst
    :language: rst

The default template for functions is ``autosummary/function.rst``:

.. literalinclude:: ../sphinx_apipages/templates/autosummary/function.rst
    :language: rst

The default template otherwise is ``autosummary/base.rst``:

.. literalinclude:: ../sphinx_apipages/templates/autosummary/base.rst
    :language: rst


.. _sphinx: https://www.sphinx-doc.org
.. _custom_templates: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#customizing-templates
