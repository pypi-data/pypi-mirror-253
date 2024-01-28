import numpy as np
import delayedarray as da
import math
import pytest

from utils import simulate_SparseNdarray


class _ChunkyBoi:
    def __init__(self, shape, chunks):
        self._shape = shape
        self._chunks = chunks

    @property
    def dtype(self):
        return np.dtype("float64")

    @property
    def shape(self):
        return self._shape


@da.chunk_shape.register
def chunk_shape_ChunkyBoi(x: _ChunkyBoi):
    return x._chunks


def test_choose_block_shape_for_iteration():
    x = np.random.rand(100, 10)
    assert da.choose_block_shape_for_iteration(x, memory=200) == (2, 10)
    assert da.choose_block_shape_for_iteration(x, memory=800) == (10, 10)

    # Not enough memory. 
    assert da.choose_block_shape_for_iteration(x, memory=0) == (1, 1)
    assert da.choose_block_shape_for_iteration(x, memory=40) == (1, 5)

    x = _ChunkyBoi((100, 200), (20, 25))
    assert da.choose_block_shape_for_iteration(x, memory=4000) == (20, 25)
    assert da.choose_block_shape_for_iteration(x, memory=40000) == (100, 50)
    assert da.choose_block_shape_for_iteration(x, memory=80000) == (100, 100)


def _dense_sum(position, block):
    ss = block.sum()
    if ss is np.ma.masked:
        ss = 0
    return position, ss


@pytest.mark.parametrize("mask_rate", [0, 0.2])
def test_apply_over_dimension_dense(mask_rate):
    x = np.ndarray([100, 200])
    counter = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] = counter
            counter += 1

    if mask_rate:
        mask = np.random.rand(*x.shape) < mask_rate 
        x = np.ma.MaskedArray(x, mask=mask)

    output = da.apply_over_blocks(x, _dense_sum, block_shape=(3, 7))
    assert len(output) == math.ceil(x.shape[0]/3) * math.ceil(x.shape[1]/7)
    assert x.sum() == sum(y[1] for y in output)
    assert output[0][0] == [(0, 3), (0, 7)]
    assert output[-1][0] == [(99, 100), (196, 200)]

    # Same results with the default.
    output = da.apply_over_blocks(x, _dense_sum)
    assert x.sum() == sum(y[1] for y in output)


@pytest.mark.parametrize("mask_rate", [0, 0.2])
def test_apply_over_dimension_sparse(mask_rate):
    x = simulate_SparseNdarray((100, 200), mask_rate=mask_rate)

    expected = 0
    for v in x.contents:
        if v is not None:
            subtotal = v[1].sum()
            if subtotal is not np.ma.masked:
                expected += subtotal

    output = da.apply_over_blocks(x, _dense_sum, block_shape=(3, 7))
    assert len(output) == math.ceil(x.shape[0]/3) * math.ceil(x.shape[1]/7)
    assert np.allclose(expected, sum(y[1] for y in output))
    assert output[0][0] == [(0, 3), (0, 7)]
    assert output[-1][0] == [(99, 100), (196, 200)]

    # Now activating sparse mode.
    def _sparse_sum(position, block):
        assert isinstance(block, da.SparseNdarray)
        total = 0 
        if block.contents is not None:
            for v in block.contents:
                if v is not None:
                    subtotal = v[1].sum()
                    if subtotal is not np.ma.masked:
                        total += subtotal
        return position, total

    output = da.apply_over_blocks(x, _sparse_sum, block_shape=(3, 7), allow_sparse=True)
    assert len(output) == math.ceil(x.shape[0]/3) * math.ceil(x.shape[1]/7)
    assert np.allclose(expected, sum(y[1] for y in output))
    assert output[0][0] == [(0, 3), (0, 7)]
    assert output[-1][0] == [(99, 100), (196, 200)]
