import os
from PIL import Image

def resize_image(image_path, output_path, width, height):
    try:
        with Image.open(image_path) as img:
            resized = img.resize((width, height))
            resized.save(output_path)
            print(f" Resized: {os.path.basename(output_path)}")
    except Exception as e:
        print(f" Resize error for {image_path}: {e}")

def convert_image(image_path, output_path, target_format):
    try:
        with Image.open(image_path) as img:
            rgb_img = img.convert("RGB") if target_format.lower() in ['jpg', 'jpeg'] else img
            rgb_img.save(output_path, format=target_format.upper())
            print(f" Converted: {os.path.basename(output_path)}")
    except Exception as e:
        print(f" Conversion error for {image_path}: {e}")

def main():
    folder = input("Enter the folder path containing images: ").strip()
    if not os.path.exists(folder):
        print(" Folder not found.")
        return

    choice = input("Choose action - resize (r) / convert format (c): ").strip().lower()

    image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp'))]

    if not image_files:
        print(" No image files found in the folder.")
        return

    output_dir = os.path.join(folder, "output")
    os.makedirs(output_dir, exist_ok=True)

    if choice == 'r':
        try:
            width = int(input("Enter new width (px): "))
            height = int(input("Enter new height (px): "))
        except ValueError:
            print(" Invalid width/height.")
            return

        for file in image_files:
            input_path = os.path.join(folder, file)
            output_path = os.path.join(output_dir, file)
            resize_image(input_path, output_path, width, height)

    elif choice == 'c':
        target_format = input("Enter target format (jpg, png, webp, etc.): ").strip().lower()
        for file in image_files:
            file_name = os.path.splitext(file)[0]
            output_path = os.path.join(output_dir, f"{file_name}.{target_format}")
            input_path = os.path.join(folder, file)
            convert_image(input_path, output_path, target_format)
    else:
        print(" Invalid option. Use 'r' for resize or 'c' for convert.")

    print("\n Task completed. Check the 'output' folder.")

if __name__ == "__main__":
    main()
