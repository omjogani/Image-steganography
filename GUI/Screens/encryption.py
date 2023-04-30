import flet as ft

import Cryptography
import Steganography
from GUI.Constants import TextStyle
import os
import base64

class Encryption:
    def __init__(self, page):
        self.page = page
        super().__init__()

    information = "Choose Image File & Key that will used to encrypt the data and generate Stego Image..."
    image_path = ""
    image_file_name = ""
    key_file_name = ft.TextField(
        label="Key File Name",
        hint_text="Enter Key File Name",
        width=500.0,
        border_color=ft.colors.INDIGO_200,
    )

    key_data = ft.TextField(
        label="Enter Data",
        hint_text="Enter Your Message Here",
        width=500.0,
        multiline=True,
        border_color=ft.colors.INDIGO_200,
        min_lines=5,
        max_lines=5,
    )

    response_message = ft.Text(
        "",
        color=ft.colors.GREEN_ACCENT,
    )

    def encryption(self):
        def handle_encrypt_event(e):
            if self.image_path == "":
                self.response_message.value = "Please Choose Image..."
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            if len(self.key_file_name.value) == 0:
                self.response_message.value = "Key file is required..."
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            if len(self.key_data.value) == 0:
                self.response_message.value = "Data is required..."
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            key = f"C:\secret\key\{self.key_file_name.value}.txt.enc"

            # check existence of key file
            if not os.path.exists(key):
                self.response_message.value = "Key File is not found!, If not generate please generate it!"
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            encoded_string = self.key_data.value.encode()
            byte_array = bytearray(encoded_string)

            encrypted_data = Cryptography.Encrypter(key).encrypt(byte_array)
            destination_image_path = fr"C:\secret\stego\{self.image_file_name}"
            dummy = "hello there this is plain text from string"
            data_to_pass = base64.b64encode(encrypted_data).decode()


            # Steganography.Encoding.encode(self.image_path, str(encrypted_data), destination_image_path)
            Steganography.Encoding.encode(self.image_path, data_to_pass, destination_image_path)

            # plaintext = Cryptography.Decrypter(key).decrypt(encrypted_data)
            # print(plaintext)

            self.response_message.value = "Encrypted Image Saved..."
            self.response_message.color = ft.colors.GREEN_ACCENT
            self.response_message.update()

        def on_dialog_result(e: ft.FilePickerResultEvent):
            print("Selected files:", e.files)
            print("Selected file or directory:", e.files[0].path)
            self.image_path = e.files[0].path
            self.image_file_name = e.files[0].name
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
                    self.key_file_name,
                    self.key_data,
                    ft.FilledButton(text="Encrypt Image", on_click=handle_encrypt_event),
                    self.response_message,
                ],
                alignment=ft.alignment.top_left,
                expand=True,
            ),
            alignment=ft.alignment.center,
        )
