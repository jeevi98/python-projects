import os
import zipfile
import datetime
import sys

def backup_folder(folder_path):
    
    if not os.path.exists(folder_path):
        print(" Error: Folder does not exist.")
        return
    
    if not os.path.isdir(folder_path):
        print(" Error: Provided path is not a folder.")
        return

    if not os.listdir(folder_path):
        print(" Warning: Folder is empty. Nothing to back up.")
        return

    
    folder_name = os.path.basename(folder_path.rstrip("\\/"))
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"{folder_name}_backup_{timestamp}.zip"
    zip_path = os.path.join(os.path.dirname(folder_path), zip_name)

    try:
     
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
            for folder, subfolders, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(folder, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    backup_zip.write(file_path, arcname)
        print(f" Backup successful: {zip_path}")
    except Exception as e:
        print(f" Error during backup: {e}")


if __name__ == "__main__":
    folder = input("Enter the full path of the folder to back up: ").strip()
    backup_folder(folder)
