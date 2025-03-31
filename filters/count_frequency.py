def count_frequency(text):
    """
    Counts the frequency of each word in the given string.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary mapping words to their frequency.
    """
    if text is None:
        return None
    word_frequency = {}
    words = text.split()
    for word in words:
        word = word.lower().strip(".,!?\"'()[]{}:;")  # Normalize words
        if word:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency