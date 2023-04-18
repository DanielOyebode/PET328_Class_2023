def calculate_stoiip(area, thickness, porosity, water_saturation, formation_volume_factor, recovery_factor):
    """
    Calculates the Stock Tank Oil Initially In Place (STOIIP) value in barrels for a given reservoir.

    Parameters:
    area (float): area of reservoir in acres
    thickness (float): thickness of reservoir in feet
    porosity (float): porosity of reservoir as a decimal
    water_saturation (float): water saturation of reservoir as a decimal
    formation_volume_factor (float): formation volume factor of reservoir in barrels/cubic feet
    recovery_factor (float): recovery factor of reservoir as a decimal

    Returns:
    stoiip (float): Stock Tank Oil Initially In Place value in barrels
    """
    a = area * 43560 # convert acres to square feet
    h = thickness
    phi = porosity
    sw = water_saturation
    b = formation_volume_factor
    rf = recovery_factor

    stoiip = (7758 * a * h * phi * (1 - sw) * b * rf) / 1000000

    return stoiip
