# Chat-log-summarizer
## Project Overview
This is a Python-based tool that analyzes chat conversations and generates concise summaries. The tool is particularly useful for quickly understanding the key points of conversations between users and AI (or any two parties) without reading through entire chat logs.

## Core Components and How They Work

1. **Chat Log Parser** (`chat_parser.py`)
   - Reads chat files in a specific format: each line starts with "User:" or "AI:" followed by the message
   - Uses regular expressions to accurately extract the speaker and message content
   - Creates a structured format of the conversation for further analysis

2. **Keyword Analysis** (`keyword_analysis.py`)
   - Implements two methods of keyword extraction:
     - **Basic Method**: Identifies frequently used words, excluding common stop words
     - **TF-IDF Method**: Uses Term Frequency-Inverse Document Frequency to find the most significant words in context
   - Configurable to return a specified number of top keywords (default: 5)

3. **Statistics Generation** (`statistics.py`)
   - Counts total messages in the conversation
   - Tracks message distribution between speakers (User vs AI)
   - Provides basic conversation metrics

4. **Summary Generation** (`summary.py`)
   - Combines statistics and keyword analysis
   - Creates a human-readable summary including:
     - Total number of exchanges
     - Main topics discussed (based on keywords)
     - Message count per speaker
     - Most relevant keywords from the conversation

5. **Main Application** (`main.py`)
   - Handles command-line arguments for flexible usage
   - Supports two key features:
     - Single file analysis
     - Bulk processing of multiple chat files from a directory
   - Allows choice between basic and TF-IDF keyword extraction methods

## Key Features
- Process individual chat logs or entire directories
- Two keyword extraction methods (basic and TF-IDF)
- Clear, structured summary output
- Error handling for invalid files or formats
- Easy-to-understand statistics about the conversation

## Setup
Clone the repository:
```
git clone https://github.com/NiazTahi/chat-log-summarizer-qtec.git
cd chat-log-summarizer-qtec
```
Install dependencies:
```
pip install -r requirements.txt
```
## Example Usage
```bash
# Analyze a single chat file
python main.py chat1.txt basic

# Analyze a single chat file with TF-IDF
python main.py chat2.txt tfidf

# Process all chat logs in a directory
python main.py /path/to/folder tfidf
```
## Sample Output
![Screenshot_1](https://github.com/user-attachments/assets/74a5237c-3080-4224-acd5-eccd3a7db855)
