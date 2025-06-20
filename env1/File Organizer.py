import os
import shutil

target_dir = input("Enter the full path of the folder to organize: ")


if not os.path.exists(target_dir):
    print("The specified directory does not exist.")
    exit()

extension_map = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.java', '.cpp']
}


def get_folder_name(extension):
    for folder, extensions in extension_map.items():
        if extension.lower() in extensions:
            return folder
    return 'Others' 


for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)

   
    if os.path.isdir(file_path):
        continue

   
    _, ext = os.path.splitext(filename)

  
    folder_name = get_folder_name(ext)


    folder_path = os.path.join(target_dir, folder_name)


    os.makedirs(folder_path, exist_ok=True)

    
    shutil.move(file_path, os.path.join(folder_path, filename))
    print(f"Moved: {filename} --> {folder_name}/")

print("\nFile organization complete!")
