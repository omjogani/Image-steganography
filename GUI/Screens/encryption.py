import flet as ft
from GUI.Constants import TextStyle


class Encryption:
    def __init__(self, page):
        self.page = page
        super().__init__()

    information = "Choose Image File & Key that will used to encrypt the data and generate Stego Image..."

    def encryption(self):
        def on_dialog_result(e: ft.FilePickerResultEvent):
            print("Selected files:", e.files)
            print("Selected file or directory:", e.path)
            # File path is available here: Om

        my_pick = ft.FilePicker(on_result=on_dialog_result)
        self.page.overlay.append(my_pick)
        return ft.Container(
            expand=True,
            content=ft.Column(
                [
                    ft.Text(
                        "Encryption",
                        size=TextStyle.HEADERFONTSIZE
                    ),
                    ft.Container(
                        height=10.0,
                        width=10.0,
                    ),
                    ft.Container(
                        width=500.0,
                        content=ft.Row(
                            [
                                ft.Icon(
                                    name=ft.icons.INFO_ROUNDED,
                                    color=ft.colors.INDIGO_200
                                ),
                                ft.Text(
                                    self.information,
                                    width=480.0,
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        width=500.0,
                        content=ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Pick Image File",
                                    icon=ft.icons.UPLOAD_FILE,
                                    on_click=lambda _: my_pick.pick_files(),
                                ),
                            ],
                        ),
                    ),

                    ft.Container(
                        width=500.0,
                    ),
                    ft.TextField(
                        label="Key File Name",
                        hint_text="Enter Key File Name",
                        width=500.0,
                        border_color=ft.colors.INDIGO_200,
                    ),

                    ft.TextField(
                        label="Enter Data",
                        hint_text="Enter Your Message Here",
                        width=500.0,
                        multiline=True,
                        border_color=ft.colors.INDIGO_200,
                        min_lines=5,
                        max_lines=5,
                    ),
                    ft.FilledButton(text="Encrypt Image"),
                ],
                alignment=ft.alignment.top_left,
                expand=True,
            ),
            alignment=ft.alignment.center,
        )
