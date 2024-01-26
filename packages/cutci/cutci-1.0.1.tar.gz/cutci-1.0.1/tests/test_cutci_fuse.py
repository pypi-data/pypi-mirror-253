import unittest
import numpy as np
import cupy as cp
import cutci_fuse as ctf


class TestCutciFuse(unittest.TestCase):
    """Tests for `cutci_fuse` package by scalars."""

    def setUp(self):
        print('TestCutciFuse')


    def test_td2vp(self):
        """Test td2vp."""
        dt2m_c = np.array([13.0])
        vp = ctf.td2vp(cp.asarray(dt2m_c))
        print('vp: ', vp)  # [14.98083604]


    def test_utci_approx(self):
        """Test utci_approx."""
        t2m_c = np.array([21.0])
        vp = np.array([14.98083604])
        va_ms = np.array([1.3])
        mrt_c = np.array([22.0])

        utci = ctf.utci_approx(cp.asarray(t2m_c), cp.asarray(vp), cp.asarray(va_ms), cp.asarray(mrt_c))
        print('UTCI_C: ', utci)  # 20.89648358

    def test_utci(self):
        """Test utci"""
        t2m_c = np.array([21.0])
        dt2m_c = np.array([13.0])
        va_ms = np.array([1.3])
        mrt_c = np.array([22.0])

        utci = ctf.calc_utci(t2m_c, dt2m_c, va_ms, mrt_c)
        print('UTCI_C: ', utci)  # 20.89648358
