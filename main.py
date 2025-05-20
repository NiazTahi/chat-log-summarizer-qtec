import sys
import os
from chat_parser import parse_chat_log
from summary import generate_summary

def main():
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = 'chat1.txt'  # Default file
    if len(sys.argv) > 2:
        keyword_method = sys.argv[2].lower()
        if keyword_method not in ('basic', 'tfidf'):
            print("Invalid keyword extraction method. Use 'basic' or 'tfidf'. Defaulting to 'basic'.")
            keyword_method = 'basic'
    else:
        keyword_method = 'basic'

    if os.path.isdir(input_path):
        # Summarize all .txt files in the folder
        txt_files = [f for f in os.listdir(input_path) if f.endswith('.txt')]
        if not txt_files:
            print(f"No .txt files found in {input_path}.")
            return
        for fname in txt_files:
            fpath = os.path.join(input_path, fname)
            try:
                chat_data = parse_chat_log(fpath)
                if not chat_data:
                    print(f"No valid chat messages found in {fname}.")
                    continue
                print(f"\n===== Summary for {fname} =====")
                summary = generate_summary(chat_data, keyword_method=keyword_method)
                print(summary)
            except Exception as e:
                print(f"An error occurred with {fname}: {e}")
    else:
        try:
            chat_data = parse_chat_log(input_path)
            if not chat_data:
                print(f"No valid chat messages found in {input_path}.")
                return
            summary = generate_summary(chat_data, keyword_method=keyword_method)
            print(summary)
        except FileNotFoundError:
            print(f"File not found: {input_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
