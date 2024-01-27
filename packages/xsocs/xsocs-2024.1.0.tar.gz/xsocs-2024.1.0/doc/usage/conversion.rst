
.. _conversion_window:

Q space conversion dialog
=========================

.. figure:: img/conversion_dialog.png
   :width: 100%
   :align: center

   Q space conversion dialog

This window lets you configure some parameters for the conversion from images to Q space:

- `Acq. Parameters`_
- `Image Processing Parameters`_
- `Q space Parameters`_

The right panel allows to review the selected region of interest on the sample and the selected scan entries.

Click on **Convert** to start the conversion.

Once the conversion is done, a :ref:`Q space item <qspace_item>` is added to the :ref:`project tree <project_tree>`.
And the result is displayed in the :ref:`Q sspace view <qspace_view>`.

Acq. Parameters
...............

.. list-table::
   :widths: 1 4
   :header-rows: 1

   * - Parameter
     - Description
   * - ``Beam energy``
     - Energy of the beam, in eV
   * - ``Direct beam``
     - Position in pixels of the direct beam on the detector
   * - ``Ch. per deg.``
     - Channels per degree

Image Processing Parameters
...........................

All image processing steps are optional, check the corresponding check box to enable them.

.. list-table::
   :widths: 1 4
   :header-rows: 1

   * - Parameter
     - Description
   * - ``Maxipix correction``
     - Apply Maxipix detector module edges correction
   * - ``Mask``
     - Select a mask image to apply on input images.
       The image MUST have the same size as input detector images.
       Non zero value in the mask image discard the corresponding pixels.
   * - ``Normalization``
     - Select the measurement to use for normalization.
   * - ``Median filter``
     - Set the size (**w**\ idth and **h**\ eight) of the median filter window.

Q space Parameters
..................

.. list-table::
   :widths: 1 4
   :header-rows: 1

   * - Parameter
     - Description
   * - ``Grid dimensions``
     - Number of bins for each dimension of the Q space histogram.
   * - ``Coordinates``
     - Select the coordinate system of the QSpace histogram.
       Either **Cartesian** or **Spherical**.

The conversion from **Cartesian** to **Spherical** coordinates is as follows:

* Radius: :math:`\sqrt(qx^2 + qy^2 + qz^2)`
* Roll (Phi) in degrees: :math:`degrees(\pi/2 - arctan2(qz, qy))`
* Pitch (Theta) in degrees: :math:`degrees(\pi/2 - arccos(qx/radius)`
