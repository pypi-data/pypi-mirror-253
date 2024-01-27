import sys

from EditorMDiv.src.utils import get_colored_text


def check_number_of_arguments(expected_number: int) -> None:
    """
    Checks if enough arguments are provided.
    :param expected_number: the number of arguments expected
    """

    if len(sys.argv) - 1 != expected_number:
        print(get_colored_text(f"Expected {expected_number} arguments, {len(sys.argv) - 1} arguments provided.", "red"))
        exit(1)


def retrieve_argument(arg_number: int) -> str:
    """
    Retrieves the argument on a certain position
    :param arg_number: the position of the argument to retrieve
    :return: the argument as a string
    """

    if len(sys.argv) - 1 > arg_number:
        print(get_colored_text(f"Please provide a number between 0 - {len(sys.argv) - 1}, argument {arg_number} doesn't exists.", "red"))
        exit(1)

    return sys.argv[arg_number]
