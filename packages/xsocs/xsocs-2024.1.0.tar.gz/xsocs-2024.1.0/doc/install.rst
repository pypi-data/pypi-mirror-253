
Installation
============

*X-SOCS* supports `Python <https://www.python.org/>`_ versions >= 3.7.

To install *X-SOCS* with minimal dependency (to use from scripts)::

    pip install xsocs [--user]

or with conda::

    conda install -c conda-forge xsocs-base

To install *X-SOCS* with its graphical user interface dependencies::

    pip install xsocs[gui] [--user]

or with conda::

    conda install -c conda-forge xsocs


To install the current development version::

    pip install --pre --find-links https://kmap.gitlab-pages.esrf.fr/xsocs/wheels/ xsocs[gui] [--user]

.. note::
   The ``--user`` optional argument installs X-SOCS for the current user only.

Dependencies
------------

The dependencies of *X-SOCS* are:

* `Python <https://www.python.org/>`_ >=3.7.
* `numpy <http://www.numpy.org>`_
* `h5py <http://www.h5py.org/>`_
* `fabio <https://pypi.org/project/fabio/>`_
* `silx <https://pypi.org/project/silx>`_
* `xrayutilities <https://xrayutilities.sourceforge.io/>`_
* `scipy <https://pypi.python.org/pypi/scipy>`_
* `PyOpenGL <http://pyopengl.sourceforge.net/>`_
* `matplotlib <https://matplotlib.org/>`_
* `PyQt5 <https://riverbankcomputing.com/software/pyqt/intro>`_
* `setuptools <https://pypi.org/project/setuptools/>`_

In addition, OpenGL 2.1 is required for the 3D view of the QSpace.

Installing from source
----------------------

Clone the source `repository <https://gitlab.esrf.fr/kmap/xsocs.git>`_::

    git clone https://gitlab.esrf.fr/kmap/xsocs.git

Or download the source as a `zip file <https://gitlab.esrf.fr/kmap/xsocs/-/archive/main/xsocs-main.zip>`_ and unzip it.

Then go into the xsocs directory::

    cd xsocs

And install xsocs either with minimal dependency (to use from scripts)::

    pip install . [--user]

or with all graphical user interface dependencies::

    pip install .[gui] [--user]


Developping xsocs
-----------------

First clone the repository (see `Installing from source`_).
Then install X-SOCS in "editable" mode with its development dependencies with::

    pip install -e .[dev]

Running the tests
+++++++++++++++++

Once *X-SOCS* is installed, run its tests with::

    python -c "import sys, xsocs.test; sys.exit(xsocs.test.run_tests(verbosity=3))"

Generating the documentation
++++++++++++++++++++++++++++

From the project's directory with the same version of *X-SOCS* installed, run::

    sphinx-build doc/ build/html
