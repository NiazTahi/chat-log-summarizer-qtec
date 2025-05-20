from typing import List, Dict
from collections import Counter
import re
from utils import get_stop_words

def extract_keywords(chat_data: List[Dict[str, str]], top_n: int = 5, method: str = 'basic') -> List[str]:
    """
    Extracts the top N most frequent keywords from the chat messages, excluding stop words.
    """
    if method == 'tfidf':
        return extract_keywords_tfidf(chat_data, top_n)
    # Basic method
    stop_words = get_stop_words()
    words = []
    for entry in chat_data:
        # Tokenize and normalize
        tokens = re.findall(r'\b\w+\b', entry['message'].lower())
        words.extend([word for word in tokens if word not in stop_words])
    most_common = Counter(words).most_common(top_n)
    return [word for word, count in most_common]


def extract_keywords_tfidf(chat_data: List[Dict[str, str]], top_n: int = 5) -> List[str]:
    """
    Extracts the top N keywords using TF-IDF from the chat messages, excluding stop words.
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    import nltk
    nltk.download('stopwords', quiet=True)
    from nltk.corpus import stopwords

    stop_words = set(stopwords.words('english')).union(get_stop_words())
    # Combine all messages into a single document
    documents = [entry['message'] for entry in chat_data]
    if not documents:
        return []
    vectorizer = TfidfVectorizer(stop_words=list(stop_words), token_pattern=r'\b\w+\b', lowercase=True)
    tfidf_matrix = vectorizer.fit_transform([' '.join(documents)])
    feature_array = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]
    # Get top N indices
    top_indices = tfidf_scores.argsort()[-top_n:][::-1]
    return [feature_array[i] for i in top_indices if tfidf_scores[i] > 0]
