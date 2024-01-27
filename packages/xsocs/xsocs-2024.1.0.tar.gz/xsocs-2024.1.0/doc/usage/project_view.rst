
.. _project_tree:

Project tree view
-----------------

Once a project is loaded, the main window displays its content as a tree with different groups.

.. |intensity_plot_button| image:: img/intensity_plot_button.png
.. |qspace_view_button| image:: img/qspace_view_button.png
.. |fit_results_button| image:: img/fit_results_button.png
.. |export_fit_button| image:: img/export_fit_button.png

.. figure:: img/project_tree.png
   :align: center
   :width: 50%

   Project tree view

Acquisition group
.................

The ``Acquisition`` group contains the raw (merged) data.

Intensity group
...............

The ``Intensity`` item represents the cumulated acquired intensity.

You can open the :ref:`intensity view <intensity_view>` by clicking on the |intensity_plot_button| button on the same row.

QSpace group
............

The ``QSpace`` group contains the results of all Q space conversions.

Once a Q space has been created from the :ref:`intensity view <intensity_view>` it is accessible from here.

.. _qspace_item:

QSpace item
***********

The ``QSpace`` item represents a single Q space.
It contains:

* An ``Infos`` node, which gives you the parameters that were used when converting images to Q space.

* A :ref:`fits group <fit_group>` that contains all the fit results for this Q space.

You can open the :ref:`qspace view <qspace_view>` by clicking on the |qspace_view_button| button on the same row.

Q space items can be deleted by selecting them and pressing the delete key.
They can be renamed by double clicking on them (the actual file is not renamed).
To reset the name just set its name to an empty string.

Q space items also provides a context menu.

.. _fit_group:

Fits group
..........

The ``fits`` group contains results for all fits or center of mass run on a given Q space.

Once a fit has been performed from the :ref:`qspace view <qspace_view>` it is accessible from this group.

.. _fit_item:

Fit Item
********

The ``Fit`` item represents fit or center-of-mass results.

You can open the :ref:`fit results <fit_view>` view by clicking on the |fit_results_button| button on the same row.

You can also export the results to a CSV file by clicking on the |export_fit_button| button on the same row.

As for :ref:`Q space items <qspace_item>`, Fit items can be deleted by selecting them and pressing the delete key.
They can be renamed by double clicking on them (the actual file is not renamed).
To reset the name just set its name to an empty string.

Fit items also provides a context menu.
