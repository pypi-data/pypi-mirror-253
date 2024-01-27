#!/usr/bin/env python
"""
This scripts illustrates the API of the gaussian/center-of-mass processing
"""

import sys
import numpy
from xsocs.process.fit import PeakFitter, FitTypes, BackgroundTypes

# path to the hdf5 file written by the kmap_2_qspace function
qspace_f = "/path/to/qspace.h5"

# Name of the text file where to store the resuls
result_file = "results.txt"

# List of QSpace indices to process
# This selects sample positions for which QSpace are processed.
# If None, all QSpace are processed
indices = None

# Number of processors to use
# If None, all available cores are used.
n_proc = None

# Set-up the processing for a gaussian fit without background subtraction
fitter = PeakFitter(
    qspace_f,
    fit_type=FitTypes.GAUSSIAN,
    indices=indices,
    n_proc=n_proc,
    roi_indices=None,  # QSpace ROI
    background=BackgroundTypes.NONE,
)

# Run the processing and get the results
results = fitter.peak_fit()

# Check for errors
if fitter.status != fitter.DONE:
    print("Fit process failed")
    sys.exit()

# Prepare columns header and data
# Start with position (x, y) on the sample
headers = ["sample_x", "sample_y"]
values = [results.sample_x, results.sample_y]

# Add one column for each parameter of the fit/COM result
# For each axis of the QSpace
for dimension, axis_name in enumerate(results.qspace_dimension_names):
    # For each fitted/computed parameter of the result
    for parameter_name in results.available_result_names:
        # Add its name to the header and its data to the values
        headers.append(axis_name + "_" + parameter_name)
        values.append(results.get_results(dimension, parameter_name))

# Transpose values from (parameters x points) to (points x parameters)
values = numpy.transpose(numpy.array(values))

# Write results to text file
with open(result_file, "w") as res_f:
    res_f.write("\t".join(headers) + "\n")
    for row_values in values:
        res_f.write("\t".join(str(v) for v in row_values) + "\n")
