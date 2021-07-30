import numpy as np


def collect_info(array: np.ndarray):
    shape = f'Shape: {array.shape}; '
    dimensions = f'dimensions: {array.ndim}; '
    length = f'length: {len(array)}; '
    size = f'size: {array.size}'
    return shape + dimensions + length + size
