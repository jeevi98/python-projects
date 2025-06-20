import os
import markdown

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }}
        h1, h2, h3 {{ color: #333; }}
        a {{ color: #007acc; }}
        pre, code {{ background: #eee; padding: 4px; border-radius: 3px; }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

def convert_md_to_html(md_file_path, output_path):
    try:
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        html_content = markdown.markdown(md_content)
        title = os.path.splitext(os.path.basename(md_file_path))[0].title()
        full_html = HTML_TEMPLATE.format(title=title, content=html_content)

        with open(output_path, 'w', encoding='utf-8') as html_file:
            html_file.write(full_html)
        
        print(f" Converted: {md_file_path} ➜ {output_path}")
    except Exception as e:
        print(f" Failed to convert {md_file_path}: {e}")

def main():
    input_folder = input("Enter the path to the folder containing markdown files: ").strip()

    if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
        print("Invalid folder path.")
        return

    output_folder = os.path.join(input_folder, "html_output")
    os.makedirs(output_folder, exist_ok=True)

    md_files = [f for f in os.listdir(input_folder) if f.endswith('.md')]

    if not md_files:
        print(" No markdown (.md) files found.")
        return

    for md_file in md_files:
        md_path = os.path.join(input_folder, md_file)
        html_file = os.path.splitext(md_file)[0] + ".html"
        html_path = os.path.join(output_folder, html_file)
        convert_md_to_html(md_path, html_path)

    print(f"\n Conversion complete! HTML files saved in: {output_folder}")

if __name__ == "__main__":
    main()
