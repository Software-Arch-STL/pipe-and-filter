def read_text(input_stream, size=None):
    """
    Reads text from an input stream and returns it as a string, ensuring not to stop in the middle of a line.

    :param input_stream: A file-like object to read text from.
    :param size: The number of lines to read from the input stream. If None, reads the entire stream.
    :return: The text read from the input stream as a string.
    """
    if size is None:
        return input_stream.read()
    if input_stream is None:
        return None
    # Read the specified number of lines
    lines = []
    for _ in range(size):
        line = input_stream.readline()
        if not line:  # Stop if end of file is reached
            break
        lines.append(line)
    
    return ''.join(lines)