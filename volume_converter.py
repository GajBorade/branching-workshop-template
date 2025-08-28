def liters_to_milliliters(vol_in_liters):
    """
    This function takes a value of volume in liters as an argument and returns the corresponding value of
    volume converted to milliliters.
    :param (float) vol_in_liters:
    :return (float) vol_in_milliliters:
    """
    if type(vol_in_liters) == str:
        return "Please enter numeric values."
    else:
        return vol_in_liters * 1000


print(liters_to_milliliters(5))
print(liters_to_milliliters("h"))