import os
import subprocess
import sys

def run_command(command, cwd=None):
    try:
        subprocess.check_call(command, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f" Command failed: {command}\n{e}")
        sys.exit(1)

def create_django_project(project_name, app_names, base_path):
    project_path = os.path.join(base_path, project_name)

    if os.path.exists(project_path):
        print(" Error: Project folder already exists.")
        return

    print(f" Creating Django project '{project_name}'...")
    run_command(f"django-admin startproject {project_name}", cwd=base_path)

    manage_py_path = os.path.join(project_path, 'manage.py')

  
    for app_name in app_names:
        print(f" Creating app '{app_name}'...")
        run_command(f"python manage.py startapp {app_name}", cwd=project_path)

    print("\n Project and apps created successfully!")
    print(f" Project directory: {project_path}")
    print(" Next steps:")
    print(f"  1. cd {project_path}")
    print("  2. python manage.py runserver")

def main():
    print(" Django Project Scaffolder\n")

    project_name = input("Enter project name: ").strip()
    app_list = input("Enter app name(s) (comma-separated): ").strip()
    base_dir = input("Enter base directory path (leave blank for current folder): ").strip()

    if not project_name.isidentifier():
        print(" Invalid project name. Use only letters, numbers, and underscores.")
        return

    if not app_list:
        print(" At least one app name is required.")
        return

    app_names = [app.strip() for app in app_list.split(",") if app.strip().isidentifier()]

    if not app_names:
        print(" No valid app names provided.")
        return

    if not base_dir:
        base_dir = os.getcwd()

    if not os.path.exists(base_dir):
        print(" The base directory does not exist.")
        return

  
    try:
        import django
    except ImportError:
        print(" Django is not installed. Run 'pip install django' first.")
        return

    create_django_project(project_name, app_names, base_dir)

if __name__ == "__main__":
    main()
