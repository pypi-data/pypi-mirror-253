import flet as ft

from EditorMDiv.src.file_handler import save_file


class MarkdownApp:

    def __init__(self, file_path: str, content: str):
        self.file_path: str = file_path
        self.title = "Markdown Editor"
        self.theme = "dark"
        self.content = content

    def run(self):
        ft.app(target=self.app)

    def app(self, page: ft.Page):
        page.title = self.title
        page.theme_mode = self.theme

        # Left hand side of the application
        text_field = ft.TextField(
            value=self.content,
            multiline=True,
            expand=True,
            border_color=ft.colors.TRANSPARENT,
            on_change=lambda e: self.update_preview(e, page, text_field, md)
        )

        # Right hand side of the application
        md = ft.Markdown(
            value=text_field.value,
            selectable=True,
            extension_set='gitHubWeb',
            on_tap_link=lambda e: page.launch_url(e.data)  # Opens the browser when clicked on a window
        )

        # Save file dialog
        def save_file_result(e: ft.FilePickerResultEvent):
            self.content = text_field.value
            save_file(self.file_path, self.content)

        page.add(
            ft.Row(  # Sets the markdown editor and viewer next to each other
                controls=[
                    # Left hand side
                    text_field,

                    # Side splitter
                    ft.VerticalDivider(color=ft.colors.GREY),

                    # Right hand side
                    ft.Container(
                        ft.Column(controls=[md], scroll='hidden'),
                        expand=True,
                        alignment=ft.alignment.top_left
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
                expand=True
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Save file", icon=ft.icons.SAVE,
                    on_click=lambda e: save_file_result(e)
                )
            ]
            )
        )

    @staticmethod
    def update_preview(e, page: ft.Page, text_field: ft.TextField, md: ft.Markdown):
        md.value = text_field.value
        page.update()
