========================
 HDF5 input file format
========================

Data dimensions
===============

Raw detector images are stored as a **J** 3D datasets (**N** * **M**, **K**, **L**), where:

- **J** raster scans (with angle or energy varying) consisting of
- **N** scan lines and
- **M** scan columns
- detector images with shape (**K**, **L**) taken for each point

Obviously (**N**, **M**, **K**, **L**) as well as the nominal motor positions need to be equal for all **J** scans.

File structure
==============

Each scan is stored in a separated HDF5 file, all of which are accessible through a "master" HDF5 file.
See :numref:`figure_input_file` below for an example.

Master file root:

- **Scan entry**: **J** entries, one for each raster scan done with som varying motor position or energy (``NXentry``)

  - **instrument** (``NXinstrument``)

    - **detector** (``NXdetector``)

      - **beam_energy**: Beam energy in eV (``float``)
      - **center_chan_dim0**: Pixel of the direct beam when all angles=0 for first image dimension (``float``)
      - **center_chan_dim1**: Pixel of the direct beam when all angles=0 for second image dimension (``float``)
      - **chan_per_deg_dim0**: Pixel per degree in first image dimension (``float``)
      - **chan_per_deg_dim1**: Pixel per degree in second image dimension (``float``)
      - **data**: 3D dataset for this raster scan with shape (**N** * **M**, **K**, **L**), i.e., flattened along scan axes.
      - **image_roi_offset**: Optional.
        Offset for center chan if using only a ROI of the PSD.
        Default: [0, 0] (``[int, int]``)

    - **positioners**: This group contains datasets for all positioners.
      Dataset shape is either (1,) or (**N** * **M**,) (``NXcollection``)

  - **measurement**: Group containing all the scan data with shape (**N** * **M**,) can be used, e.g., for normalization.
    Not mandatory (``NXcollection``)

    - **adcX**: X encoder position (1D array of float)
    - **adcY**: Y encoder position (1D array of float)
    - **adcZ**: Z encoder position (1D array of float)
    - **image** (``NXcollection``)

      - **data**: Link to ``../../instrument/detector/data``
      - **info**: Link to ``../../instrument/detector`` (``NXdetector``)

  - **scan**: Raster scan info

    - **delay**: Exposure time (``float``)
    - **motor_0**: Fast motor name (``string``)
    - **motor_0_end**: Fast motor end (``float``)
    - **motor_0_start**: Fast motor start (``float``)
    - **motor_0_steps**: Fast motor number of points (``int``)
    - **motor_1**: Slow motor name (``string``)
    - **motor_1_end**: Slow motor end (``float``)
    - **motor_1_start**: Slow motor start (``float``)
    - **motor_1_steps**: Slow motor number of points (``int``)

  - **start_time** (``string``)
  - **title**: Scan title (``string``)

Example
=======

.. _figure_input_file:
.. figure:: img/input_file.png
   :align: center

   Example of a X-Socs HDF5 input file structure
