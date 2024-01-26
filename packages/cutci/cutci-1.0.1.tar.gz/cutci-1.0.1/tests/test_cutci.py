#!/usr/bin/env python

"""Tests for `cutci` package."""


import unittest
from click.testing import CliRunner

from cutci import cli
import os
import numpy as np
import cutci as ct


def get_file(name):
    return os.path.join(os.path.dirname(__file__), name)


class TestCutci(unittest.TestCase):
    """Tests for `cutci` package."""

    def setUp(self):
        # variables
        vars = np.genfromtxt(
            get_file("testcases.csv"),
            delimiter=",",
            # names=True
            skip_header=1
        )
        # print(vars.shape)
        self.cossza = vars[:, 0]
        self.ssrd = vars[:, 1]
        self.ssr = vars[:, 2]
        self.fdir = vars[:, 3]
        self.strd = vars[:, 4]
        self.str = vars[:, 5]
        self.mrt = vars[:, 6]
        self.t2m = vars[:, 7]
        self.d2m = vars[:, 8]
        self.va_u = vars[:, 9]
        self.va_v = vars[:, 10]
        self.utci = vars[:, 11]
        # print(self.mrt)

        self.va = (self.va_u ** 2 + self.va_v ** 2) ** 0.5

    def test_mrt(self):
        mrt_c = ct.calc_mrt(self.ssrd, self.ssr, self.fdir, self.strd, self.str, self.cossza)
        # print('mrt_c: ', mrt_c)
        np.testing.assert_array_almost_equal(mrt_c, self.mrt, decimal=5)


    def test_utci(self):
        utci_c = ct.calc_utci(self.t2m-273.15, self.d2m-273.15, self.va, self.mrt)
        # print('utci_c: ', utci_c)
        np.testing.assert_array_almost_equal(utci_c, self.utci, decimal=4)


    def tearDown(self):
        """Tear down test fixtures, if any."""


    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cutci.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
