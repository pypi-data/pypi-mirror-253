#!/usr/bin/env python

from xsocs.process.qspace import kmap_2_qspace, QSpaceConverter

# ========================
# Files
# ========================
# output HDF5 file name, default is qspace.h5 if not set
output_f = "my_qspace.h5"

# path to the hdf5 "master" file (see id01_spec function)
xsocs_h5 = "/path/to/data.h5"

# ========================
# Conversion parameters
# ========================

# number of "bins" for the qspace cubes
qspace_dims = (28, 154, 60)

# size of median filter window to apply to each frame
medfilt_dims = None  # e.g. (3,3)

# set disp_times to True if you want to output some info in stdout
QSpaceConverter.disp_times = True

# positions (on the sample) to convert to qspace
# if pos_indices will be ignored if rect_roi is provided
# rect_roi = [x_min, x_max, y_min, y_max] (sample positions)
roi = None

# whether to redistribute the intensity to fill the mpx4 gaps
maxipix_correction = False

# data column containing the monitor readings of primary beam intensity
monitor = "cnt1"

# Mask:
# boolean array of equal shape to detector frames to filter out bad pixels
# A non-zero value means that the pixel is masked
mask = None  # numpy.ndarray

# set to true if you want to overwrite the output file
# otherwise an exception will be raised if the file already exists
overwrite = False

# number of processes to use
# If None, will use the number of availble core (see multiprocessing.cpu_count)
n_proc = None

kmap_2_qspace(
    xsocs_h5,
    output_f,
    qspace_dims,
    medfilt_dims=medfilt_dims,
    maxipix_correction=maxipix_correction,
    normalizer=monitor,
    roi=roi,
    mask=mask,
    n_proc=n_proc,
    overwrite=overwrite,
)
