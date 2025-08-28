def seconds_to_minutes(time_in_seconds):
    """
    This function takes a value of time in seconds as an argument and returns the corresponding value of
    time converted to minutes.
    :param (float) time_in_seconds:
    :return (float) time_in_minutes:
    """
    if type(time_in_seconds) == str:
        return "Please enter numeric values."
    else:
        return time_in_seconds / 60


print(seconds_to_minutes(5))
print(seconds_to_minutes("h"))
