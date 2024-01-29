import ast
import os
import glob
import sys
import subprocess


def is_virtual_env():
    """Check if Python is running in a virtual environment."""
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def get_virtual_env_name():
    """Get the name of the current virtual environment, if any."""
    if is_virtual_env():
        return os.path.basename(sys.prefix)
    return None


def can_import_module(module_name):
    """Try to import a module, return True if successful, False otherwise."""
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False


def extract_module_name(node):
    """Extracts top-level module names from AST nodes."""
    modules = []
    if isinstance(node, ast.Import):
        modules = [alias.name.split('.')[0] for alias in node.names]
    elif isinstance(node, ast.ImportFrom):
        if node.module:
            modules = [node.module.split('.')[0]]

    return set(modules)


def parse_file_for_modules(filename):
    """Parses a Python file and returns a set of third-party top-level modules."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read())
    except (SyntaxError, TabError) as e:
        print(f"Error in file {filename}: {e}")
        return set()

    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            modules.update(extract_module_name(node))

    return modules


def get_unique_modules_in_directory(directory):
    """Finds Python files in a directory and compiles a unique set of their third-party top-level imports, skipping the current virtual environment directory and modules that can be imported."""
    unique_modules = set()
    env_name = get_virtual_env_name()

    for filepath in glob.iglob(os.path.join(directory, '**', '*.py'), recursive=True):
        # Skip files in the current virtual environment
        if env_name and env_name in filepath:
            continue

        file_modules = parse_file_for_modules(filepath)
        for module in file_modules:
            if not can_import_module(module):
                unique_modules.add(module)

    return unique_modules


def save_requirements_file():
    """Uses pip freeze to save the current environment's packages to a requirements file."""
    filename = 'requirements.txt'
    with open(filename, 'w') as file:
        subprocess.run([sys.executable, '-m', 'pip', 'freeze'], stdout=file)
    print(f"Requirements file '{filename}' saved.")


def install_missing_modules(unique_modules):
    """Installs modules that are missing from the installed packages."""
    for module in sorted(unique_modules):
        print(f"Installing {module}...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {module}.")


def main():
    """Main function to process command line argument."""
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    unique_modules = get_unique_modules_in_directory(directory)

    if unique_modules:
        install_missing_modules(unique_modules)
        save_requirements_file()
    else:
        print("No third-party modules found to install.")


if __name__ == "__main__":
    main()
