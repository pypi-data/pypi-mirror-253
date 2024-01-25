import pathlib


def print_repo_tree(repo_base_path: pathlib.Path) -> str:
    """Print the repository tree

    Args:
        repo_base_path: (pathlib.Path) the repository base path

    Returns:
        (str) the repository tree
    """
    return print_repo_tree_recursive(repo_base_path=repo_base_path, indent_level=0)


def print_repo_tree_recursive(repo_base_path: pathlib.Path, indent_level=0):
    """Print the repository tree excluding __pycache__ directories and .pyc files

    Args:
        repo_base_path: (pathlib.Path) the repository base path
        indent_level: (int) current indentation level

    Returns:
        (str) the repository tree
    """
    if not repo_base_path.is_dir():
        raise ValueError("The provided path is not a directory")

    output = []
    for item in sorted(repo_base_path.iterdir(), key=lambda x: (x.is_file(), x.name)):
        if item.name == '__pycache__' or item.suffix == '.pyc' or item.name == '.idea' or item.name == '.git':
            continue

        prefix = '    ' * indent_level + '- ' if indent_level > 0 else ''
        output.append(f"{prefix}{item.name}")

        if item.is_dir():
            output.append(print_repo_tree_recursive(item, indent_level + 1))

    return '\n'.join(output)


def count_repo_python_lines(repo_base_path: pathlib.Path) -> int:
    """Count the number of lines of python code in the repository

    Step 1: find all python files in the repository recursively
    Step 2: count the number of lines of each python file
    Step 3: sum up the number of lines of all python files

    Args:
        repo_base_path: (pathlib.Path) the repository base path

    Returns:
        (int) the number of lines of python code in the repository
    """

    def count_lines_in_file(file_path: pathlib.Path) -> int:
        """Count the number of lines in a single file."""
        with file_path.open('r', encoding='utf-8') as file:
            return sum(1 for _ in file)

    def count_lines_in_directory(directory: pathlib.Path) -> int:
        """Recursively count the number of lines in python files in the directory."""
        line_count = 0
        for path in directory.iterdir():
            if path.is_dir():
                # If it's a directory, recursively count lines in it
                line_count += count_lines_in_directory(path)
            elif path.is_file() and path.suffix == '.py':
                # If it's a python file, count lines in the file
                line_count += count_lines_in_file(path)
        return line_count

    return count_lines_in_directory(repo_base_path)


def touch_as_file(path: pathlib.Path):
    """touch the path as a file, if exists as a directory, raise error"""
    if path.exists():
        if path.is_dir():
            raise ValueError(f"Cannot touch {path}, it is a directory")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)


def touch_as_dir(path: pathlib.Path):
    """touch the path as a directory, if exists as a file, raise error"""
    if path.exists():
        if path.is_file():
            raise ValueError(f"Cannot touch {path}, it is a file")
    else:
        path.mkdir(parents=True, exist_ok=True)


__all__ = [
    'touch_as_dir',
    'touch_as_file',
    'print_repo_tree',
    'count_repo_python_lines',
]