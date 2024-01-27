class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_colored_text(text: str, color: str) -> str:
    """
    Returns for a given text and color, the text in color
    :param text: the text to color
    :param color: the color used to color the text
    :return: the colored text
    """

    if color.lower() == "red":
        return f"{Colors.FAIL}{text}{Colors.ENDC}"

    elif color.lower() == "blue":
        return f"{Colors.OKBLUE}{text}{Colors.ENDC}"

    else:
        return text
