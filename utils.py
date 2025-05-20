def get_stop_words() -> set:
    """
    Returns a set of common English stop words.
    """
    return {
        'the', 'is', 'and', 'a', 'an', 'to', 'of', 'in', 'for', 'on', 'with', 'as', 'by', 'at', 'from',
        'that', 'this', 'it', 'be', 'are', 'was', 'were', 'or', 'but', 'not', 'can', 'if', 'you', 'your',
        'about', 'what', 'how', 'i', 'me', 'my', 'we', 'our', 'us', 'so', 'do', 'does', 'did', 'have',
        'has', 'had', 'will', 'would', 'should', 'could', 'just', 'let', 'more', 'also', 'than', 'then',
        'they', 'them', 'their', 'he', 'she', 'his', 'her', 'it', 'its', 'who', 'whom', 'which', 'when',
        'where', 'why', 'because', 'been', 'being', 'all', 'any', 'each', 'few', 'some', 'such', 'no',
        'nor', 'only', 'own', 'same', 'too', 'very', 's', 't', 'can', 'will', 'don', 'should', 'now'
    }
