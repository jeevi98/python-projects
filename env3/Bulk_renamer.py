import os

def bulk_rename(folder_path, base_name, extension_filter=None, add_numbering=True):

    if not os.path.exists(folder_path):
        print(" Error: Folder does not exist.")
        return
    
    if not os.path.isdir(folder_path):
        print(" Error: Not a folder.")
        return

 
    files = sorted(os.listdir(folder_path))
    if extension_filter:
        files = [f for f in files if f.lower().endswith(extension_filter.lower())]

    if not files:
        print(" No files found to rename.")
        return

    print(f" Found {len(files)} file(s) to rename.")

   
    count = 1
    for old_name in files:
        old_path = os.path.join(folder_path, old_name)
        ext = os.path.splitext(old_name)[1]
        new_name = f"{base_name}_{str(count).zfill(3)}{ext}" if add_numbering else f"{base_name}{ext}"
        new_path = os.path.join(folder_path, new_name)

        try:
            os.rename(old_path, new_path)
            print(f" Renamed: {old_name} ➜ {new_name}")
            count += 1
        except Exception as e:
            print(f" Could not rename {old_name}: {e}")

    print("\n Renaming complete!")


if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    pattern = input("Enter base name (e.g., Image, File, Doc): ").strip()
    ext_filter = input("Filter by extension (e.g., .jpg) or leave blank for all: ").strip()
    numbering = input("Add numbering? (yes/no): ").strip().lower() == 'yes'

    bulk_rename(folder, pattern, ext_filter if ext_filter else None, numbering)
