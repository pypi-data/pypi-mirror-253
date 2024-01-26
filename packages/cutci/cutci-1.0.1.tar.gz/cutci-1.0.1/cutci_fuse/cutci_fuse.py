import numpy as np
import cupy as cp


@cp.fuse()
def td2vp(td):
    e = cp.where(td > 0, cp.exp(34.494 - 4924.99 / (td + 237.1)) / (td + 105) ** 1.57, \
                 cp.exp(43.494 - 6545.8 / (td + 278)) / (td + 868) ** 2)
    vp = e / 100.0  # convert water vapor pressure from Pa to hPa

    return vp


@cp.fuse()
def utci_approx(air_temp, vp, air_vel, mrt):
    ta = air_temp
    pa = vp / 10.0  # use vapour pressure in kPa

    # set upper and lower limits of air velocity according to Fiala model scenarios
    air_vel = cp.where(air_vel < 0.5, 0.5, air_vel)
    va = cp.where(air_vel > 17, 17, air_vel)

    d_mrt = mrt - ta

    # calculate 6th order polynomial as approximation
    utci = ta + \
           (6.07562052e-1) + \
           (-2.27712343e-2) * ta + \
           (8.06470249e-4) * ta * ta + \
           (-1.54271372e-4) * ta * ta * ta + \
           (-3.24651735e-6) * ta * ta * ta * ta + \
           (7.32602852e-8) * ta * ta * ta * ta * ta + \
           (1.35959073e-9) * ta * ta * ta * ta * ta * ta + \
           (-2.25836520e0) * va + \
           (8.80326035e-2) * ta * va + \
           (2.16844454e-3) * ta * ta * va + \
           (-1.53347087e-5) * ta * ta * ta * va + \
           (-5.72983704e-7) * ta * ta * ta * ta * va + \
           (-2.55090145e-9) * ta * ta * ta * ta * ta * va + \
           (-7.51269505e-1) * va * va + \
           (-4.08350271e-3) * ta * va * va + \
           (-5.21670675e-5) * ta * ta * va * va + \
           (1.94544667e-6) * ta * ta * ta * va * va + \
           (1.14099531e-8) * ta * ta * ta * ta * va * va + \
           (1.58137256e-1) * va * va * va + \
           (-6.57263143e-5) * ta * va * va * va + \
           (2.22697524e-7) * ta * ta * va * va * va + \
           (-4.16117031e-8) * ta * ta * ta * va * va * va + \
           (-1.27762753e-2) * va * va * va * va + \
           (9.66891875e-6) * ta * va * va * va * va + \
           (2.52785852e-9) * ta * ta * va * va * va * va + \
           (4.56306672e-4) * va * va * va * va * va + \
           (-1.74202546e-7) * ta * va * va * va * va * va + \
           (-5.91491269e-6) * va * va * va * va * va * va + \
           (3.98374029e-1) * d_mrt + \
           (1.83945314e-4) * ta * d_mrt + \
           (-1.73754510e-4) * ta * ta * d_mrt + \
           (-7.60781159e-7) * ta * ta * ta * d_mrt + \
           (3.77830287e-8) * ta * ta * ta * ta * d_mrt + \
           (5.43079673e-10) * ta * ta * ta * ta * ta * d_mrt + \
           (-2.00518269e-2) * va * d_mrt + \
           (8.92859837e-4) * ta * va * d_mrt + \
           (3.45433048e-6) * ta * ta * va * d_mrt + \
           (-3.77925774e-7) * ta * ta * ta * va * d_mrt + \
           (-1.69699377e-9) * ta * ta * ta * ta * va * d_mrt + \
           (1.69992415e-4) * va * va * d_mrt + \
           (-4.99204314e-5) * ta * va * va * d_mrt + \
           (2.47417178e-7) * ta * ta * va * va * d_mrt + \
           (1.07596466e-8) * ta * ta * ta * va * va * d_mrt + \
           (8.49242932e-5) * va * va * va * d_mrt + \
           (1.35191328e-6) * ta * va * va * va * d_mrt + \
           (-6.21531254e-9) * ta * ta * va * va * va * d_mrt + \
           (-4.99410301e-6) * va * va * va * va * d_mrt + \
           (-1.89489258e-8) * ta * va * va * va * va * d_mrt + \
           (8.15300114e-8) * va * va * va * va * va * d_mrt + \
           (7.55043090e-4) * d_mrt * d_mrt + \
           (-5.65095215e-5) * ta * d_mrt * d_mrt + \
           (-4.52166564e-7) * ta * ta * d_mrt * d_mrt + \
           (2.46688878e-8) * ta * ta * ta * d_mrt * d_mrt + \
           (2.42674348e-10) * ta * ta * ta * ta * d_mrt * d_mrt + \
           (1.54547250e-4) * va * d_mrt * d_mrt + \
           (5.24110970e-6) * ta * va * d_mrt * d_mrt + \
           (-8.75874982e-8) * ta * ta * va * d_mrt * d_mrt + \
           (-1.50743064e-9) * ta * ta * ta * va * d_mrt * d_mrt + \
           (-1.56236307e-5) * va * va * d_mrt * d_mrt + \
           (-1.33895614e-7) * ta * va * va * d_mrt * d_mrt + \
           (2.49709824e-9) * ta * ta * va * va * d_mrt * d_mrt + \
           (6.51711721e-7) * va * va * va * d_mrt * d_mrt + \
           (1.94960053e-9) * ta * va * va * va * d_mrt * d_mrt + \
           (-1.00361113e-8) * va * va * va * va * d_mrt * d_mrt + \
           (-1.21206673e-5) * d_mrt * d_mrt * d_mrt + \
           (-2.18203660e-7) * ta * d_mrt * d_mrt * d_mrt + \
           (7.51269482e-9) * ta * ta * d_mrt * d_mrt * d_mrt + \
           (9.79063848e-11) * ta * ta * ta * d_mrt * d_mrt * d_mrt + \
           (1.25006734e-6) * va * d_mrt * d_mrt * d_mrt + \
           (-1.81584736e-9) * ta * va * d_mrt * d_mrt * d_mrt + \
           (-3.52197671e-10) * ta * ta * va * d_mrt * d_mrt * d_mrt + \
           (-3.36514630e-8) * va * va * d_mrt * d_mrt * d_mrt + \
           (1.35908359e-10) * ta * va * va * d_mrt * d_mrt * d_mrt + \
           (4.17032620e-10) * va * va * va * d_mrt * d_mrt * d_mrt + \
           (-1.30369025e-9) * d_mrt * d_mrt * d_mrt * d_mrt + \
           (4.13908461e-10) * ta * d_mrt * d_mrt * d_mrt * d_mrt + \
           (9.22652254e-12) * ta * ta * d_mrt * d_mrt * d_mrt * d_mrt + \
           (-5.08220384e-9) * va * d_mrt * d_mrt * d_mrt * d_mrt + \
           (-2.24730961e-11) * ta * va * d_mrt * d_mrt * d_mrt * d_mrt + \
           (1.17139133e-10) * va * va * d_mrt * d_mrt * d_mrt * d_mrt + \
           (6.62154879e-10) * d_mrt * d_mrt * d_mrt * d_mrt * d_mrt + \
           (4.03863260e-13) * ta * d_mrt * d_mrt * d_mrt * d_mrt * d_mrt + \
           (1.95087203e-12) * va * d_mrt * d_mrt * d_mrt * d_mrt * d_mrt + \
           (-4.73602469e-12) * d_mrt * d_mrt * d_mrt * d_mrt * d_mrt * d_mrt + \
           (5.12733497e0) * pa + \
           (-3.12788561e-1) * ta * pa + \
           (-1.96701861e-2) * ta * ta * pa + \
           (9.99690870e-4) * ta * ta * ta * pa + \
           (9.51738512e-6) * ta * ta * ta * ta * pa + \
           (-4.66426341e-7) * ta * ta * ta * ta * ta * pa + \
           (5.48050612e-1) * va * pa + \
           (-3.30552823e-3) * ta * va * pa + \
           (-1.64119440e-3) * ta * ta * va * pa + \
           (-5.16670694e-6) * ta * ta * ta * va * pa + \
           (9.52692432e-7) * ta * ta * ta * ta * va * pa + \
           (-4.29223622e-2) * va * va * pa + \
           (5.00845667e-3) * ta * va * va * pa + \
           (1.00601257e-6) * ta * ta * va * va * pa + \
           (-1.81748644e-6) * ta * ta * ta * va * va * pa + \
           (-1.25813502e-3) * va * va * va * pa + \
           (-1.79330391e-4) * ta * va * va * va * pa + \
           (2.34994441e-6) * ta * ta * va * va * va * pa + \
           (1.29735808e-4) * va * va * va * va * pa + \
           (1.29064870e-6) * ta * va * va * va * va * pa + \
           (-2.28558686e-6) * va * va * va * va * va * pa + \
           (-3.69476348e-2) * d_mrt * pa + \
           (1.62325322e-3) * ta * d_mrt * pa + \
           (-3.14279680e-5) * ta * ta * d_mrt * pa + \
           (2.59835559e-6) * ta * ta * ta * d_mrt * pa + \
           (-4.77136523e-8) * ta * ta * ta * ta * d_mrt * pa + \
           (8.64203390e-3) * va * d_mrt * pa + \
           (-6.87405181e-4) * ta * va * d_mrt * pa + \
           (-9.13863872e-6) * ta * ta * va * d_mrt * pa + \
           (5.15916806e-7) * ta * ta * ta * va * d_mrt * pa + \
           (-3.59217476e-5) * va * va * d_mrt * pa + \
           (3.28696511e-5) * ta * va * va * d_mrt * pa + \
           (-7.10542454e-7) * ta * ta * va * va * d_mrt * pa + \
           (-1.24382300e-5) * va * va * va * d_mrt * pa + \
           (-7.38584400e-9) * ta * va * va * va * d_mrt * pa + \
           (2.20609296e-7) * va * va * va * va * d_mrt * pa + \
           (-7.32469180e-4) * d_mrt * d_mrt * pa + \
           (-1.87381964e-5) * ta * d_mrt * d_mrt * pa + \
           (4.80925239e-6) * ta * ta * d_mrt * d_mrt * pa + \
           (-8.75492040e-8) * ta * ta * ta * d_mrt * d_mrt * pa + \
           (2.77862930e-5) * va * d_mrt * d_mrt * pa + \
           (-5.06004592e-6) * ta * va * d_mrt * d_mrt * pa + \
           (1.14325367e-7) * ta * ta * va * d_mrt * d_mrt * pa + \
           (2.53016723e-6) * va * va * d_mrt * d_mrt * pa + \
           (-1.72857035e-8) * ta * va * va * d_mrt * d_mrt * pa + \
           (-3.95079398e-8) * va * va * va * d_mrt * d_mrt * pa + \
           (-3.59413173e-7) * d_mrt * d_mrt * d_mrt * pa + \
           (7.04388046e-7) * ta * d_mrt * d_mrt * d_mrt * pa + \
           (-1.89309167e-8) * ta * ta * d_mrt * d_mrt * d_mrt * pa + \
           (-4.79768731e-7) * va * d_mrt * d_mrt * d_mrt * pa + \
           (7.96079978e-9) * ta * va * d_mrt * d_mrt * d_mrt * pa + \
           (1.62897058e-9) * va * va * d_mrt * d_mrt * d_mrt * pa + \
           (3.94367674e-8) * d_mrt * d_mrt * d_mrt * d_mrt * pa + \
           (-1.18566247e-9) * ta * d_mrt * d_mrt * d_mrt * d_mrt * pa + \
           (3.34678041e-10) * va * d_mrt * d_mrt * d_mrt * d_mrt * pa + \
           (-1.15606447e-10) * d_mrt * d_mrt * d_mrt * d_mrt * d_mrt * pa + \
           (-2.80626406e0) * pa * pa + \
           (5.48712484e-1) * ta * pa * pa + \
           (-3.99428410e-3) * ta * ta * pa * pa + \
           (-9.54009191e-4) * ta * ta * ta * pa * pa + \
           (1.93090978e-5) * ta * ta * ta * ta * pa * pa + \
           (-3.08806365e-1) * va * pa * pa + \
           (1.16952364e-2) * ta * va * pa * pa + \
           (4.95271903e-4) * ta * ta * va * pa * pa + \
           (-1.90710882e-5) * ta * ta * ta * va * pa * pa + \
           (2.10787756e-3) * va * va * pa * pa + \
           (-6.98445738e-4) * ta * va * va * pa * pa + \
           (2.30109073e-5) * ta * ta * va * va * pa * pa + \
           (4.17856590e-4) * va * va * va * pa * pa + \
           (-1.27043871e-5) * ta * va * va * va * pa * pa + \
           (-3.04620472e-6) * va * va * va * va * pa * pa + \
           (5.14507424e-2) * d_mrt * pa * pa + \
           (-4.32510997e-3) * ta * d_mrt * pa * pa + \
           (8.99281156e-5) * ta * ta * d_mrt * pa * pa + \
           (-7.14663943e-7) * ta * ta * ta * d_mrt * pa * pa + \
           (-2.66016305e-4) * va * d_mrt * pa * pa + \
           (2.63789586e-4) * ta * va * d_mrt * pa * pa + \
           (-7.01199003e-6) * ta * ta * va * d_mrt * pa * pa + \
           (-1.06823306e-4) * va * va * d_mrt * pa * pa + \
           (3.61341136e-6) * ta * va * va * d_mrt * pa * pa + \
           (2.29748967e-7) * va * va * va * d_mrt * pa * pa + \
           (3.04788893e-4) * d_mrt * d_mrt * pa * pa + \
           (-6.42070836e-5) * ta * d_mrt * d_mrt * pa * pa + \
           (1.16257971e-6) * ta * ta * d_mrt * d_mrt * pa * pa + \
           (7.68023384e-6) * va * d_mrt * d_mrt * pa * pa + \
           (-5.47446896e-7) * ta * va * d_mrt * d_mrt * pa * pa + \
           (-3.59937910e-8) * va * va * d_mrt * d_mrt * pa * pa + \
           (-4.36497725e-6) * d_mrt * d_mrt * d_mrt * pa * pa + \
           (1.68737969e-7) * ta * d_mrt * d_mrt * d_mrt * pa * pa + \
           (2.67489271e-8) * va * d_mrt * d_mrt * d_mrt * pa * pa + \
           (3.23926897e-9) * d_mrt * d_mrt * d_mrt * d_mrt * pa * pa + \
           (-3.53874123e-2) * pa * pa * pa + \
           (-2.21201190e-1) * ta * pa * pa * pa + \
           (1.55126038e-2) * ta * ta * pa * pa * pa + \
           (-2.63917279e-4) * ta * ta * ta * pa * pa * pa + \
           (4.53433455e-2) * va * pa * pa * pa + \
           (-4.32943862e-3) * ta * va * pa * pa * pa + \
           (1.45389826e-4) * ta * ta * va * pa * pa * pa + \
           (2.17508610e-4) * va * va * pa * pa * pa + \
           (-6.66724702e-5) * ta * va * va * pa * pa * pa + \
           (3.33217140e-5) * va * va * va * pa * pa * pa + \
           (-2.26921615e-3) * d_mrt * pa * pa * pa + \
           (3.80261982e-4) * ta * d_mrt * pa * pa * pa + \
           (-5.45314314e-9) * ta * ta * d_mrt * pa * pa * pa + \
           (-7.96355448e-4) * va * d_mrt * pa * pa * pa + \
           (2.53458034e-5) * ta * va * d_mrt * pa * pa * pa + \
           (-6.31223658e-6) * va * va * d_mrt * pa * pa * pa + \
           (3.02122035e-4) * d_mrt * d_mrt * pa * pa * pa + \
           (-4.77403547e-6) * ta * d_mrt * d_mrt * pa * pa * pa + \
           (1.73825715e-6) * va * d_mrt * d_mrt * pa * pa * pa + \
           (-4.09087898e-7) * d_mrt * d_mrt * d_mrt * pa * pa * pa + \
           (6.14155345e-1) * pa * pa * pa * pa + \
           (-6.16755931e-2) * ta * pa * pa * pa * pa + \
           (1.33374846e-3) * ta * ta * pa * pa * pa * pa + \
           (3.55375387e-3) * va * pa * pa * pa * pa + \
           (-5.13027851e-4) * ta * va * pa * pa * pa * pa + \
           (1.02449757e-4) * va * va * pa * pa * pa * pa + \
           (-1.48526421e-3) * d_mrt * pa * pa * pa * pa + \
           (-4.11469183e-5) * ta * d_mrt * pa * pa * pa * pa + \
           (-6.80434415e-6) * va * d_mrt * pa * pa * pa * pa + \
           (-9.77675906e-6) * d_mrt * d_mrt * pa * pa * pa * pa + \
           (8.82773108e-2) * pa * pa * pa * pa * pa + \
           (-3.01859306e-3) * ta * pa * pa * pa * pa * pa + \
           (1.04452989e-3) * va * pa * pa * pa * pa * pa + \
           (2.47090539e-4) * d_mrt * pa * pa * pa * pa * pa + \
           (1.48348065e-3) * pa * pa * pa * pa * pa * pa
    return utci

def calc_utci(t2m_c, dt2m_c, va_ms, mrt_c, mask=None):
    """
    Calculate Human Thermal Comfort Index (UTCI) by cutci_fuse
    :param t2m_c: is 2m temperature [Degrees Celsius]
    :param dt2m_c: is dew point temperature [Degrees Celsius]
    :param va_ms: is wind speed at 10 meters [m/s]
    :param mrt_c: is mean radiant temperature [Degrees Celsius]
    :param mask: is mask array. If the type of the preceding parameters is numpy.ma.masked_array, mask should NOT be None

    :return: UTCI [Degrees Celsius]
    """
    t2m_vals = cp.asarray(t2m_c)
    dt2m_vals = cp.asarray(dt2m_c)
    va_vals = cp.asarray(va_ms)
    mrt_vals = cp.asarray(mrt_c)

    VP = td2vp(dt2m_vals)
    if mask is None:
        # print('utci_approx, no mask')
        utci = utci_approx(t2m_vals, VP, va_vals, mrt_vals)
        utci_np = cp.asnumpy(utci)
    else:
        # print('utci_approx, mask')
        mask_cp = cp.asarray(mask)
        cp.putmask(t2m_vals, mask_cp, 1)
        cp.putmask(VP, mask_cp, 1)
        cp.putmask(va_vals, mask_cp, 1)
        cp.putmask(mrt_vals, mask_cp, 1)

        utci = utci_approx(t2m_vals, VP, va_vals, mrt_vals)
        cp.putmask(utci, mask_cp, 1)
        utci_np = np.ma.masked_array(cp.asnumpy(utci), mask)
    return utci_np
