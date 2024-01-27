.. role:: bash(code)
   :language: bash

Starting X-SOCS
===============

Once installed, you can run X-SOCS from the command line with:

.. code-block:: bash

   xsocs

or, alternatively with ``python -m xsocs``.

This will open X-SOCS main window, with no project loaded.

.. figure:: img/main_view.png
   :align: center

   Main Window

You can then either:

- :ref:`Create a new project <create_project>`, or
- :ref:`Load an existing one <load_project>`.

Command line options
--------------------

Some options are available from the command line:

.. program-output:: python -m xsocs help

Graphical User interface
++++++++++++++++++++++++

.. program-output:: python -m xsocs help gui

Dataset concatenation
+++++++++++++++++++++

.. program-output:: python -m xsocs help concat
