from typing import List, Dict

def count_messages(chat_data: List[Dict[str, str]]) -> int:
    """
    Returns the total number of messages in the chat.
    """
    return len(chat_data)


def count_messages_by_speaker(chat_data: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Returns a dictionary with the count of messages for each speaker (User and AI).
    """
    counts = {'User': 0, 'AI': 0}
    for entry in chat_data:
        speaker = entry['speaker']
        if speaker in counts:
            counts[speaker] += 1
    return counts
