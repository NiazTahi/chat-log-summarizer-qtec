from typing import List, Dict
from statistics import count_messages, count_messages_by_speaker
from keyword_analysis import extract_keywords

def generate_summary(chat_data: List[Dict[str, str]], keyword_method: str = 'basic') -> str:
    """
    Generates a summary of the chat log.
    keyword_method: 'basic' or 'tfidf'
    """
    total = count_messages(chat_data)
    speaker_counts = count_messages_by_speaker(chat_data)
    keywords = extract_keywords(chat_data, method=keyword_method)

    # Nature of the conversation line
    if keywords:
        nature = f"The user asked mainly about {', '.join(keywords[:-1])} and {keywords[-1]}."
    else:
        nature = "The nature of the conversation could not be determined."

    summary_lines = [
        'Summary:',
        f'- The conversation had {total} exchanges.',
        f'- {nature}',
        f'- User messages: {speaker_counts.get("User", 0)}; AI messages: {speaker_counts.get("AI", 0)}.',
        f'- Most common keywords ({keyword_method}): {", ".join(keywords) if keywords else "None"}.',
    ]
    return '\n'.join(summary_lines)
