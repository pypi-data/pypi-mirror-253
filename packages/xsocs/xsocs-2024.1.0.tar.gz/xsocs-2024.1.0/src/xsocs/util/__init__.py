"""This module miscellaneous convenient functions"""

import warnings
import numpy


def bin_centers_to_range_step(centers):
    """Convert histogram bin centers (as stored in hdf5) to bin range and step

    This assumes sorted bins of the same size.

    :param numpy.ndarray centers: 1D array of bin centers
    :return: Bin edges min, max, step
    :rtype: List[float]
    """
    centers = numpy.array(centers, copy=False)
    nbins = centers.shape[0] - 1
    min_, max_ = numpy.min(centers), numpy.max(centers)
    step = (max_ - min_) / nbins
    return min_ - step / 2.0, max_ + step / 2.0, step


_SQRT_2_PI = numpy.sqrt(2 * numpy.pi)


def gaussian(x, area, center, sigma):
    """Returns (a / (sqrt(2 * pi) * s)) * exp(- 0.5 * ((x - c) / s)^2)

    :param numpy.ndarray x: values for which the gaussian must be computed
    :param float area: area under curve ( amplitude * s * sqrt(2 * pi) )
    :param float center:
    :param float sigma:
    :rtype: numpy.ndarray
    """
    return (area / (_SQRT_2_PI * sigma)) * numpy.exp(-0.5 * ((x - center) / sigma) ** 2)


def project(data, hits=None):
    """Sum data along each axis

    :param numpy.ndarray data: 3D histogram
    :param Union[numpy.ndarray,None] hits:
        Number of bin count of the histogram or None to ignore
    :return: Projections on each axis of the dataset
    :rtype: List[numpy.ndarray]
    """
    if hits is not None:
        tmp = hits.sum(2)
        hits0_sum = tmp.sum(1)
        hits1_sum = tmp.sum(0)
        hits2_sum = hits.sum((0, 1))
    else:
        hits0_sum = hits1_sum = hits2_sum = 1

    tmp = data.sum(2)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        dim0_sum = tmp.sum(1) / hits0_sum
        dim1_sum = tmp.sum(0) / hits1_sum
        dim2_sum = data.sum((0, 1)) / hits2_sum
    # to get smth that resembles the sum rather than the mean,
    # one can here multiply element wise by the summed 2D area

    if hits is not None:
        dim0_sum[hits0_sum <= 0] = 0
        dim1_sum[hits1_sum <= 0] = 0
        dim2_sum[hits2_sum <= 0] = 0

    return dim0_sum, dim1_sum, dim2_sum
