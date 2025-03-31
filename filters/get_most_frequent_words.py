def get_most_frequent_words(word_freq_dict, N=10):
    """
    Given a dictionary of words and their frequencies, return the top N most frequent words
    and their frequencies as a dictionary.

    :param word_freq_dict: Dictionary where keys are words and values are their frequencies
    :param N: Number of top frequent words to return
    :return: Dictionary of top N words and their frequencies
    """
    if word_freq_dict is None:
        return None
    # Sort the dictionary by frequency in descending order and take the top N items
    sorted_words = sorted(word_freq_dict.items(), key=lambda item: item[1], reverse=True)[:N]
    # Convert the sorted list of tuples back into a dictionary
    return dict(sorted_words)