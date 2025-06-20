import os
import pandas as pd

def split_csv(file_path, rows_per_file=500):
    if not os.path.exists(file_path) or not file_path.endswith('.csv'):
        print(" Invalid CSV file path.")
        return

    try:
      
        total_rows = sum(1 for _ in open(file_path, encoding='utf-8')) - 1  
        print(f" Total rows (excluding header): {total_rows}")

    
        file_base = os.path.splitext(os.path.basename(file_path))[0]
        output_dir = f"{file_base}_split"
        os.makedirs(output_dir, exist_ok=True)

        chunk_iter = pd.read_csv(file_path, chunksize=rows_per_file)
        for i, chunk in enumerate(chunk_iter):
            output_file = os.path.join(output_dir, f"{file_base}_part{i+1}.csv")
            chunk.to_csv(output_file, index=False)
            print(f" Saved: {output_file}")

        print("\n Splitting completed successfully.")

    except Exception as e:
        print(f" Error while splitting: {e}")

def main():
    print(" Large CSV Splitter\n")
    file_path = input("Enter the full path of the CSV file: ").strip()
    rows_input = input("Enter number of rows per split file (default 500): ").strip()
    rows = int(rows_input) if rows_input.isdigit() else 500
    split_csv(file_path, rows)

if __name__ == "__main__":
    main()
