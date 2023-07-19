"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np

import molecool

def test_build_bond_list_exception():

    coordinates = np.array([[0,0,0], [0,1,0]])

    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates, max_bond=1, min_bond=1.1)


def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molecool" in sys.modules
