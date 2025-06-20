import os
import re
from collections import Counter

def clean_and_tokenize(text):
  
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = text.split()
    return words

def analyze_words(words):
    total_words = len(words)
    unique_words = len(set(words))
    word_freq = Counter(words)
    return total_words, unique_words, word_freq

def word_counter(file_path, top_n=10):
    if not os.path.exists(file_path) or not file_path.endswith(".txt"):
        print(" Invalid file path.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        words = clean_and_tokenize(content)
        total, unique, freq = analyze_words(words)

        print("\n Word Count Summary")
        print(f" Total words: {total}")
        print(f" Unique words: {unique}")
        print(f"\n Top {top_n} most frequent words:")
        for word, count in freq.most_common(top_n):
            print(f"{word}: {count}")

    except Exception as e:
        print(f" Error reading file: {e}")

def main():
    print(" Word Counter CLI\n")
    file_path = input("Enter the path to the .txt file: ").strip()
    top_n_input = input("Show how many top frequent words? (default 10): ").strip()
    top_n = int(top_n_input) if top_n_input.isdigit() else 10

    word_counter(file_path, top_n)

if __name__ == "__main__":
    main()
