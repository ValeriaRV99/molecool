""""
Unit test for the measure module
"""
import pytest
import numpy as np

import molecool

# @pytest.mark.skipif(reason="1==1")
@pytest.mark.slow
def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1.0

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance
