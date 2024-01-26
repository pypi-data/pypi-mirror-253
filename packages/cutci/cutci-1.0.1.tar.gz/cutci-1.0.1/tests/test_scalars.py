import unittest
import numpy as np
import cutci as ct


class TestCutciScalars(unittest.TestCase):
    """Tests for `cutci` package by scalars."""

    def test_cos_sza_day(self):
        """Test cos_sza_day."""
        lat = np.array([51.0])
        lon = np.array([0])
        day_str = '20210604'
        cos_sza_day = ct.calc_cos_sza_day(day_str, lon, lat)
        # print("cos_sza_day: ", cos_sza_day)
        print(cos_sza_day[12])
        np.testing.assert_almost_equal(cos_sza_day[12, 0, 0], 0.8799, decimal=2)

    def test_cos_sza_ave_day(self):
        """Test cos_sza_ave_day."""
        lat = np.array([51.0])
        lon = np.array([0])
        day_str = '20210604'

        cos_sza_ave_day = ct.calc_cos_sza_avg_day(day_str, lon, lat)
        # print("cos_sza_ave_day: ", cos_sza_ave_day)
        print(cos_sza_ave_day[12])
        np.testing.assert_almost_equal(cos_sza_ave_day[12, 0, 0], 0.8719, decimal=2)

    def test_mrt(self):
        """Test MRT."""
        ssrd = np.array([60000])
        ssr = np.array([471818])
        fdir = np.array([374150])
        strd = np.array([1061213])
        str = np.array([-182697])
        cos_sza = np.array([0.4])

        mrt_c = ct.calc_mrt(ssrd, ssr, fdir, strd, str, cos_sza)
        mrt_k = mrt_c + 273.15
        print('MRT_C: ', mrt_c)  # -3.35089971
        print('MRT_K: ', mrt_k)  # 269.79910029
        np.testing.assert_array_almost_equal(mrt_k, [269.80254479], decimal=2)

    def test_utci(self):
        """Test calc_utci."""
        t2m_c = np.array([21.0])
        dt2m_c = np.array([13.0])
        va_ms = np.array([1.3])
        mrt_c = np.array([22.0])

        utci = ct.calc_utci(t2m_c, dt2m_c, va_ms, mrt_c)
        print('UTCI_C: ', utci)  # 20.89648358
        np.testing.assert_array_almost_equal(utci, [20.89755771], decimal=2)  # compare with thermofeel

