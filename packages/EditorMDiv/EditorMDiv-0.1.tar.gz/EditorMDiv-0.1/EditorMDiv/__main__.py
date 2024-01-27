from EditorMDiv.src.app import MarkdownApp
from EditorMDiv.src.arg_handler import *
from EditorMDiv.src.file_handler import *


def main():
    check_number_of_arguments(1)
    file = f"{os.getcwd()}/{retrieve_argument(1)}"
    check_file_extension(file, "md")
    file_content = load_file(file)
    markdown_app = MarkdownApp(file, file_content)
    markdown_app.run()
    save_file(file, markdown_app.content)
