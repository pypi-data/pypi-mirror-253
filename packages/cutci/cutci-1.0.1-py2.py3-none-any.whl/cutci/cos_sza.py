import numpy as np
import cupy as cp
import datetime as dt


def _calc_day_of_year(dt64):
    dt0 = dt64.astype('datetime64[Y]')  # day 1 of the year
    hours = np.array(dt64 - dt0, 'timedelta64[h]').astype(np.float64)
    days = hours / 24.0
    return cp.asarray(days)


# calculate solar declination angle (in degrees)
def calc_solar_declination_angle(dt64):
    # calculate the float number of day in the year
    days = _calc_day_of_year(dt64)
    # Calculates the day angle for the Earth's orbit around the Sun
    day_angle = 2 * cp.pi / 365.25 * days

    sda = (0.006918 - 0.399912 * cp.cos(day_angle) + 0.070257 * cp.sin(day_angle)
           - 0.006758 * cp.cos(2 * day_angle) + 0.000907 * cp.sin(2 * day_angle)
           - 0.002697 * cp.cos(3 * day_angle) + 0.00148 * cp.sin(3 * day_angle)
           )
    return sda * (180 / cp.pi)  # in degrees


# calculate solar hour angle
def calc_solar_hour_angle(dt64, longitude):
    # calculate the float number of day in the year
    days = _calc_day_of_year(dt64)
    # calculate the day angle for the Earth's orbit around the Sun
    day_angle = 2 * cp.pi / 365.25 * days

    # calculate time correction (TC)
    tc = (0.004297 + 0.107029 * cp.cos(day_angle) - 1.837877 * cp.sin(day_angle)
          - 0.837378 * cp.cos(2 * day_angle) - 2.340475 * cp.sin(2 * day_angle)
          )

    dt0 = dt64.astype('datetime64[D]')  # beginning of the day (00:00)
    minutes = np.array(dt64 - dt0, 'timedelta64[m]').astype(np.float64)
    hr = cp.asarray(minutes) / 60.0
    hour_angle = 15.0 * (hr - 12.0) + longitude + tc

    gt_180 = cp.where(hour_angle > 180, True, False)
    lt_m180 = cp.where(hour_angle < -180, True, False)
    hour_angle = cp.where(gt_180, hour_angle - 360, hour_angle)
    hour_angle = cp.where(lt_m180, 360 + hour_angle, hour_angle)

    return hour_angle


# calculate twilight solar hour angle
def calc_twilight_solar_hour_angle(sda, lat):
    sda = sda * (cp.pi / 180)
    lat = cp.where(lat > 89.99, 89.99, lat)
    lat = cp.where(lat < -89.99, -89.99, lat)
    lat = lat * (cp.pi / 180)

    cos_twi_ha = -1 * cp.tan(sda) * cp.tan(lat)
    cos_twi_ha_valid = cp.where((cos_twi_ha >= -1) & (cos_twi_ha <= 1), True, False)

    twi_ha = cp.where(cos_twi_ha_valid,
                      cp.arccos(cos_twi_ha) * (180 / cp.pi),
                      9999)  # 9999 stands for polar days and polar nights
    return twi_ha


# calculate the cosine of solar zenith angle
def calc_cos_sza(sda, lat, sha):
    sda = sda * (cp.pi / 180)
    lat = lat * (cp.pi / 180)
    sha = sha * (cp.pi / 180)

    cos_sza = cp.sin(sda) * cp.sin(lat) + cp.cos(sda) * cp.cos(lat) * cp.cos(sha)

    return cos_sza


# calculate the average value between time steps for cosine of solar zenith angle
def calc_cos_sza_avg(sda, lat, ha_max, ha_min):
    sda = sda * (cp.pi / 180)
    lat = lat * (cp.pi / 180)
    ha_max = cp.where(ha_max - ha_min < 0, 360 + ha_max, ha_max)
    ha_max = ha_max * (cp.pi / 180)
    ha_min = ha_min * (cp.pi / 180)

    cza_avg = cp.sin(sda) * cp.sin(lat) \
              + cp.cos(sda) * cp.cos(lat) * (cp.sin(ha_max) - cp.sin(ha_min)) / (ha_max - ha_min)

    return cza_avg


def calc_cos_sza_day(day_str, lons, lats):
    """
    Calculate the cosine of solar zenith angle at a given day
    :param day_str: is the string of the given day with a format of 'YYYYMMDD' [dimentionless]
    :param lons: is longitudes [degree]
    :param lats: is latitudes  [degree]

    :return: cosine of solar zenith angle [dimentionless]
    """
    day_dt = dt.datetime.strptime(day_str, "%Y%m%d").date()
    rows, cols = lats.size, lons.size

    x, y = np.meshgrid(lons, lats)
    day_hr0 = day_dt.isoformat() + 'T00:00'
    next_day_hr0 = (day_dt + dt.timedelta(days=1)).isoformat() + 'T00:00'
    time_dt64 = np.arange(day_hr0, next_day_hr0, dtype='datetime64[h]')  # hour range from 0 to 23 of current day

    num = len(time_dt64)
    cos_sza = cp.zeros((num, rows, cols))

    for k in range(num):
        dtime = time_dt64[k]
        time_1dlyrs = np.repeat(dtime, rows * cols)

        lat_1dlyrs = np.tile(y.reshape(rows * cols), 1)
        lon_1dlyrs = np.tile(x.reshape(rows * cols), 1)

        sda = calc_solar_declination_angle(time_1dlyrs)
        sha = calc_solar_hour_angle(time_1dlyrs, cp.asarray(lon_1dlyrs))

        cos_sza_s = calc_cos_sza(sda, cp.asarray(lat_1dlyrs), sha)
        cos_sza[k] = cos_sza_s.reshape(rows, cols)

    # search grid at night
    cos_sza = cp.where(cos_sza <= 0, 0, cos_sza)

    return cp.asnumpy(cos_sza)


def calc_cos_sza_avg_day(day_str, lons, lats):
    """
    Calculate the average cosine of solar zenith angle at a given day
    :param day_str: is the string of the given day with a format of 'YYYYMMDD' [dimentionless]
    :param lons: is longitudes [degree]
    :param lats: is latitudes  [degree]

    :return: average cosine of solar zenith angle [dimentionless]
    """
    day_dt = dt.datetime.strptime(day_str, "%Y%m%d").date()
    rows, cols = lats.size, lons.size

    x, y = np.meshgrid(lons, lats)
    day_hr0 = day_dt.isoformat() + 'T00:00'
    next_day_hr0 = (day_dt + dt.timedelta(days=1)).isoformat() + 'T00:00'
    time_dt64 = np.arange(day_hr0, next_day_hr0, dtype='datetime64[h]')  # hour range from 0 to 23 of current day

    num = len(time_dt64)
    cos_sza_avg = cp.zeros((num, rows, cols))

    for k in range(num):
        dtime = time_dt64[k]
        time_1dlyrs = np.repeat(dtime, rows * cols)
        time_prev_1dlyrs = time_1dlyrs - np.timedelta64(60, 'm')
        time_next_1dlyrs = time_1dlyrs + np.timedelta64(0, 'm')

        lat_1dlyrs = np.tile(y.reshape(rows * cols), 1)
        lon_1dlyrs = np.tile(x.reshape(rows * cols), 1)

        sda = calc_solar_declination_angle(time_1dlyrs)
        sha_prev = calc_solar_hour_angle(time_prev_1dlyrs, cp.asarray(lon_1dlyrs))
        sha_next = calc_solar_hour_angle(time_next_1dlyrs, cp.asarray(lon_1dlyrs))
        twi_ha = calc_twilight_solar_hour_angle(sda, cp.asarray(lat_1dlyrs))

        # search sunset and sunrise grids
        con_sset1 = cp.where((twi_ha >= -180) & (twi_ha <= 180) & (twi_ha > sha_prev), True, False)
        con_sset2 = cp.where((twi_ha >= -180) & (twi_ha <= 180) & (twi_ha < sha_next), True, False)
        con_srise1 = cp.where((twi_ha >= -180) & (twi_ha <= 180) & (-1 * twi_ha > sha_prev), True, False)
        con_srise2 = cp.where((twi_ha >= -180) & (twi_ha <= 180) & (-1 * twi_ha < sha_next), True, False)

        ha_max = cp.where(con_sset1 & con_sset2, twi_ha, sha_next)
        ha_min = cp.where(con_srise1 & con_srise2, -1 * twi_ha, sha_prev)

        cos_sza_avg_s = calc_cos_sza_avg(sda, cp.asarray(lat_1dlyrs), ha_max, ha_min)
        cos_sza_avg[k] = cos_sza_avg_s.reshape(rows, cols)

    # search grid at night
    cos_sza_avg = cp.where(cos_sza_avg <= 0, 0, cos_sza_avg)

    return cp.asnumpy(cos_sza_avg)
