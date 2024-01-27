import os

from EditorMDiv.src.utils import get_colored_text


def check_file_exists(file_path: str) -> None:
    """
    Checks if a given file path exists
    :param file_path: the file to be checked
    """

    # Check if file exists
    if not os.path.exists(file_path):
        # Give error message that file doesn't exist
        print(get_colored_text(f"The file: {file_path} doesn't exists", 'red'))
        exit(1)


def check_file_extension(file: str, expected_extension: str) -> None:
    """
    Checks if the file has the expected extension
    :param file: the file to be checked
    :param expected_extension: the expected extension for the file
    """

    if '.' not in file:
        print(get_colored_text(f"File {file}, has no extension", 'red'))
        exit(1)

    split_file = file.split('.')
    extension = split_file[-1]

    if extension != expected_extension:
        print(get_colored_text(f"The file {file} has as extension {extension}, expected: {expected_extension}", 'red'))
        exit(1)


def load_file(file_path: str) -> str:
    """
    Opens a file for a given file path
    :param file_path: the file to open
    :return: the content of the file
    """

    # Check if the file exists
    check_file_exists(file_path)

    with open(file_path, 'r') as file:
        return file.read()


def save_file(file_path: str, content: str) -> None:
    """
    Saves the new content to a value
    :param file_path: the file where the content needs to be stored in
    :param content: the content to be stored
    """

    # Check if the file exists
    check_file_exists(file_path)

    with open(file_path, 'w') as file:
        file.write(content)
