def remove_duplicates(input_string):
    """
    Removes duplicate lines from the input string and returns the resulting string.

    :param input_string: The input string containing multiple lines.
    :return: A string with duplicate lines removed, preserving the order of first occurrence.
    """
    if input_string is None:
        return None
    seen_lines = set()
    result_lines = []

    for line in input_string.splitlines():
        if line not in seen_lines:
            seen_lines.add(line)
            result_lines.append(line)

    return "\n".join(result_lines)