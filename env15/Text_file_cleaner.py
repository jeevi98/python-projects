import os
import re
from nltk.corpus import stopwords

def clean_text(text):
   
    text = text.lower()

    text = re.sub(r'[^a-z\s]', '', text)


    words = text.split()
    filtered_words = [word for word in words if word not in stopwords.words('english')]

    return ' '.join(filtered_words)

def clean_text_file(input_path, output_path):
    if not os.path.exists(input_path) or not input_path.endswith(".txt"):
        print(" Invalid input file path.")
        return

    try:
        with open(input_path, "r", encoding="utf-8") as infile:
            content = infile.read()

        cleaned = clean_text(content)

        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write(cleaned)

        print(f" Cleaned text saved to: {output_path}")

    except Exception as e:
        print(f" Error: {e}")

def main():
    print(" Text File Cleaner\n")
    input_file = input("Enter the path to the input text file: ").strip()
    output_file = input("Enter path for cleaned output file (e.g., cleaned.txt): ").strip()
    clean_text_file(input_file, output_file)

if __name__ == "__main__":
    main()
