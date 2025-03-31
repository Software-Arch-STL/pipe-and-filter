def remove_comments(input_string):
    """
    Removes all lines that start with a '#' from the input string.

    Args:
        input_string (str): The input string containing multiple lines.

    Returns:
        str: The resulting string with comment lines removed.
    """
    if input_string is None:
        return None
    lines = input_string.splitlines()
    filtered_lines = [line for line in lines if not line.strip().startswith('#')]
    return '\n'.join(filtered_lines)