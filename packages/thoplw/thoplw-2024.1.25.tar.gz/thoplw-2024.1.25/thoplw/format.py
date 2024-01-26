"""
Formatting functions
"""


def clever_format(x, fmt_str="%6.2f"):
    """
    Convert given value(s) to an appropriate expression.

    Args:
        x       (int or list): Input value(s).
        fmt_str (str)        : Format specifier.
    """
    if isinstance(x, list):
        return [clever_format(value) for value in x]

    # Initialize the unit of the value x.
    unit_idx = 0

    # Update the value and the unit.
    while (x >= 1000) and (unit_idx < 5):
        x /= 1000
        unit_idx += 1

    # Return with unit.
    if   unit_idx == 0: unit = " "  # No unit
    elif unit_idx == 1: unit = "K"  # Kilo
    elif unit_idx == 2: unit = "M"  # Mega
    elif unit_idx == 3: unit = "G"  # Giga
    elif unit_idx == 4: unit = "T"  # Tera
    elif unit_idx == 5: unit = "P"  # Peta
    elif unit_idx == 6: unit = "E"  # Exa
    elif unit_idx == 7: unit = "Z"  # Zetta
    elif unit_idx == 8: unit = "Y"  # Yotta
    elif unit_idx == 9: unit = "R"  # Ronna

    # Returns formatted string and unit.
    return (fmt_str % x) + " " + unit


def format_table(list_of_array, kind):
    """
    Returns formatted table as a string.

    Args:
        list_of_array (str): List of string array.

    Returns:
        (str): String of the output table.
    """
    if   kind == "text": return format_table_txt(list_of_array)
    elif kind == "csv" : return format_table_csv(list_of_array)
    elif kind == "md"  : return format_table_mdn(list_of_array)
    else               : raise ValueError("Unknown table kind: %s" % kind)


def format_table_txt(list_of_array):
    """
    Returns formatted table as a string in a text format.
    This formatting is suitable for displaying to STDOUT.

    Args:
        list_of_array (str): List of string array.

    Returns:
        (str): String of the output table.
    """
    # Compute necessary constants.
    n_array  = len(list_of_array[0])
    idx_last = n_array - 1

    # Initialize a container to store line strings.
    lines = list()

    # 
    for row, values in enumerate(zip(*list_of_array)):

        #
        if (row == 1) or (row == idx_last):
            bars = ["-" * len(value) for value in values]
            lines.append("+-" + "-+-".join(bars) + "-+")

        #
        lines.append("| " + " | ".join(values) + " |")

    #
    return "\n".join(lines)


def format_table_csv(list_of_array):
    """
    Returns formatted table as a string in a CSV format.
    This formatting is suitable for importing to the other software.

    Args:
        list_of_array (str): List of string array.

    Returns:
        (str): String of the output table.
    """
    # Initialize a container to store line strings.
    lines = list()

    # Join values with delimiter ',' and append to line strings.
    for row, values in enumerate(zip(*list_of_array)):

        # Strip elements.
        values = (s.strip() for s in values)

        # Append as CSV line.
        lines.append(",".join(values))

    # Concatenate to one string and return it.
    return "\n".join(lines)


def format_table_mdn(list_of_array):
    """
    Returns formatted table as a string in a Markdown format.
    This formatting is suitable for displaying on GitHub.

    Args:
        list_of_array (str): List of string array.

    Returns:
        (str): String of the output table.
    """
    #
    n_array = len(list_of_array[0])

    # Initialize a container to store line strings.
    lines = list()

    # Join values with delimiter ',' and append to line strings.
    for row, values in enumerate(zip(*list_of_array)):

        #
        if row == 1:
            bars = ["-" * len(value) for value in values]
            lines.append("|:" + ":|:".join(bars) + ":|")

        #
        lines.append("| " + " | ".join(values) + " |")


    # Concatenate to one string and return it.
    return "\n".join(lines)


# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
