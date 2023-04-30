import flet as ft

import Cryptography
import Steganography
from GUI.Constants import TextStyle
import os
import base64

class Decryption:
    def __init__(self, page):
        self.page = page
        super().__init__()

    image_file_path = ""
    image_name = ""
    information = "Choose Image File & Key that will used to encrypt the data and generate Stego Image..."
    key_file_name = ft.TextField(
        label="Key File Name",
        hint_text="Enter Key File Name",
        width=500.0,
        border_color=ft.colors.INDIGO_200,
    )
    key_data = ft.TextField(
        label="Key Value",
        hint_text="Enter Key Value",
        width=500.0,
        multiline=True,
        border_color=ft.colors.INDIGO_200,
        min_lines=1,
        max_lines=5,
    )

    output_window = ft.TextField(
        label="Decrypted Message",
        hint_text="Enter Your Message Here",
        width=500.0,
        read_only=True,
        value="",
        multiline=True,
        border_color=ft.colors.INDIGO_200,
        min_lines=5,
        max_lines=5,
    )
    response_message = ft.Text(
        "",
        color=ft.colors.GREEN_ACCENT,
    )
    def decryption(self):
        def handle_decrypt_text(e):
            if self.image_file_path == "":
                self.response_message.value = "Please Choose Stego Image..."
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            if len(self.key_file_name.value) == 0:
                self.response_message.value = "Key file is required..."
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            key = f"C:\secret\key\{self.key_file_name.value}.txt.enc"

            # check existance of key file
            if not os.path.exists(key):
                self.response_message.value = "Key File is not found!, If not generate please generate it!"
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            data_from_enc_file = Cryptography.Decrypter("").decrypt_file(key)
            if data_from_enc_file.decode("utf-8") != self.key_data.value:
                self.response_message.value = "Key Value is not Correct"
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            encrypted_data = Steganography.Decoding.decode(self.image_file_path)
            decoded = base64.b64decode(encrypted_data)

            plain_text = Cryptography.Decrypter("").decrypt(decoded)
            self.output_window.value = plain_text.decode("utf-8")
            self.output_window.update()

            self.response_message.value = "Decrypted!"
            self.response_message.color = ft.colors.GREEN_ACCENT
            self.response_message.update()

        def on_dialog_result(e: ft.FilePickerResultEvent):
            print("Selected files:", e.files)
            self.image_file_path = e.files[0].path
            self.image_file_name = e.files[0].name

        my_pick = ft.FilePicker(on_result=on_dialog_result)
        self.page.overlay.append(my_pick)
        return ft.Container(
            expand=True,
            content=ft.Column(
                [
                    ft.Text(
                        "Decryption",
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
                                    "Pick Encrypted Image File",
                                    icon=ft.icons.UPLOAD_FILE,
                                    on_click=lambda _: my_pick.pick_files(),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        width=500.0,
                    ),
                    self.key_file_name,
                    self.key_data,
                    ft.FilledButton(text="Decrypt Image", on_click=handle_decrypt_text),
                    ft.Container(
                        height=10.0,
                        width=10.0,
                    ),
                    self.output_window,
                    self.response_message,
                ],
                alignment=ft.alignment.top_left,
                expand=True,
            ),
            alignment=ft.alignment.center,
        )
