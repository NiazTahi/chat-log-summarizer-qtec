import re
from typing import List, Dict, Tuple

def parse_chat_log(filepath: str) -> List[Dict[str, str]]:
    """
    Parses a chat log file and returns a list of dictionaries with 'speaker' and 'message'.
    """
    chat_data = []
    pattern = re.compile(r'^(User|AI):\s*(.*)$', re.IGNORECASE)
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            match = pattern.match(line)
            if match:
                speaker = match.group(1)
                message = match.group(2)
                chat_data.append({'speaker': speaker, 'message': message})
    return chat_data
