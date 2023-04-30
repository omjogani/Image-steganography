import flet as ft

import Cryptography
from GUI.Constants import TextStyle


class GenerateKey:
    def __init__(self):
        super().__init__()

    key_file_name_box = ft.TextField(
        label="Key File Name",
        hint_text="Enter Key File Name",
        width=500.0,
        border_color=ft.colors.INDIGO_200,
    )

    key_value_box = ft.TextField(
        label="Key Value",
        hint_text="Enter Key Value",
        width=500.0,
        multiline=True,
        border_color=ft.colors.INDIGO_200,
        min_lines=1,
        max_lines=3,
    )

    response_message = ft.Text(
        "",
        color=ft.colors.GREEN_ACCENT,
    )

    information = "Enter File name without Extension, Enter Key Value that will be encrypted and stored in File."

    def generate_key(self):
        def handle_create_key_generation(e):
            if len(self.key_file_name_box.value) == 0:
                self.response_message.value = "Key file is required..."
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            if len(self.key_value_box.value) == 0:
                self.response_message.value = "Key value is required..."
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            fullpath = f'C:\secret\key\{self.key_file_name_box.value}'

            # Call to Key Generation Algorithm
            acknowledgement = Cryptography.KeyGeneration.createkeyfile(fullpath, self.key_value_box.value)
            if acknowledgement:
                # update Status
                self.response_message.value = "Key Generated Successfully..."
                self.response_message.color = ft.colors.GREEN_ACCENT
                self.response_message.update()
            else:
                self.response_message.value = "Something Went Wrong!"
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()

        return ft.Container(
            expand=True,
            content=ft.Column(
                [
                    ft.Text(
                        "Generate Key",
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
                    ),
                    self.key_file_name_box,
                    self.key_value_box,
                    ft.FilledButton(text="Generate", on_click=handle_create_key_generation),
                    self.response_message,
                ],
                alignment=ft.alignment.top_left,
                expand=True,
            ),
            alignment=ft.alignment.center,
        )
