def mps_to_kph(mps):
    """
    Converts mps to kph using well know conversion factor.
    :param mps: (meters per second)
    :return: kph (kilometers per hour)
    """
    kph = mps * 3.6
    return kph