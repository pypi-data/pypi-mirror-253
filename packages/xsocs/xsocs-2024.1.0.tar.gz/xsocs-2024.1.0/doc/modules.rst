===============
 API Reference
===============

X-SOCS data processing is implemented in the :mod:`xsocs.process` package.
It provides:

- Merge SPEC+EDF to HDF5: :mod:`xsocs.process.merge`
- Q Space Conversion: :mod:`xsocs.process.qspace`
- Fit/COM: :mod:`xsocs.process.fit`

:mod:`xsocs.process.merge`: SPEC+EDF to HDF5
============================================

.. automodule:: xsocs.process.merge

:func:`~xsocs.process.merge.merge_scan_data`
--------------------------------------------

.. autofunction:: merge_scan_data

Sample Code
-----------

.. literalinclude:: ../src/xsocs/examples/id01_merge.py
   :lines: 31-

:mod:`xsocs.process.qspace`: QSpace conversion
==============================================

.. automodule:: xsocs.process.qspace

:func:`~xsocs.process.qspace.kmap_2_qspace`
-------------------------------------------

.. autofunction:: kmap_2_qspace

Sample Code
-----------

.. literalinclude:: ../src/xsocs/examples/id01_qspace.py

:mod:`xsocs.process.fit`: Fit/COM
=================================

.. automodule:: xsocs.process.fit

:class:`~xsocs.process.fit.PeakFitter`
--------------------------------------

.. autoclass:: PeakFitter

.. autoclass:: FitTypes

.. autoclass:: BackgroundTypes

Sample Code
-----------

.. literalinclude:: ../src/xsocs/examples/id01_peak.py
