import re
import os
import subprocess

def extract_code(conversation, language):
    """
    Extract code snippets from a conversation based on the specified language.
    """
    try:
        code_pattern = re.compile(rf"```{language}(.*?)```", re.DOTALL)
        return code_pattern.findall(conversation)
    except Exception as e:
        print(f"Error occurred while extracting code snippets: {e}")
        return []

def build_flask_app(python_snippets):
    """
    Build a Flask app using the extracted Python code snippets.
    """
    app_structure = {
        'app/__init__.py': '',
        'app/models.py': '',
        'app/routes.py': '',
        'app/templates/index.html': '<!doctype html>\n<html>\n<head>\n<title>Home</title>\n</head>\n<body>\n<h1>Home Page</h1>\n</body>\n</html>',
        'app/static/style.css': 'body { font-family: Arial, sans-serif; }',
        'run.py': '',
        'config.py': 'class Config:\n    DEBUG = True\n',
        'requirements.txt': 'Flask\nFlask-Admin\nFlask-SQLAlchemy\n'
    }

    try:
        # Sample logic to organize extracted snippets into appropriate files
        for snippet in python_snippets:
            if 'from flask' in snippet or 'Flask(' in snippet:
                app_structure['app/__init__.py'] += snippet
            elif 'db = SQLAlchemy()' in snippet:
                app_structure['app/models.py'] += snippet
            elif 'def' in snippet:
                app_structure['app/routes.py'] += snippet

        # Create files with the extracted and organized content
        for file_path, content in app_structure.items():
            with open(file_path, 'w') as file:
                file.write(content)
    except Exception as e:
        print(f"Error occurred while building Flask app: {e}")

def create_project_directory(project_name):
    """
    Create a project directory with the given name.
    """
    try:
        os.makedirs(project_name, exist_ok=True)
        os.chdir(project_name)
    except Exception as e:
        print(f"Error occurred while creating project directory: {e}")

def install_dependencies():
    """
    Install dependencies specified in requirements.txt.
    """
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    except Exception as e:
        print(f"Error occurred while installing dependencies: {e}")

def initialize_git():
    """
    Initialize a Git repository and make an initial commit.
    """
    try:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    except Exception as e:
        print(f"Error occurred while initializing Git repository: {e}")

def main():
    project_name = input("Enter project name: ")
    conversation = input("Enter conversation with code snippets: ")

    # Extract Python code snippets
    python_snippets = extract_code(conversation, 'python')

    # Create project directory
    create_project_directory(project_name)

    # Build Flask app
    build_flask_app(python_snippets)

    # Install dependencies
    install_dependencies()

    # Initialize Git repository
    initialize_git()

    print(f"Flask app '{project_name}' successfully generated.")

if __name__ == "__main__":
    main()