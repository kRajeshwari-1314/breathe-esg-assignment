def normalize_unit(value, unit):
    """
    Convert values into standard units.
    """

    if unit.lower() == 'gallons':
        return value * 3.78541, 'Liters'

    return value, unit


def detect_suspicious(value):
    """
    Simple anomaly detection.
    """

    if value > 10000:
        return True

    return False