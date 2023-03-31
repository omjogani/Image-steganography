import flet as ft


class HomeScreen:
    def __init__(self):
        super().__init__()

    def home_screen(self):
        # return ft.Text(value="Hello World", color="green")
        return ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    ft.Container(
                        bgcolor=ft.colors.INDIGO_ACCENT,
                        padding=5,
                        width=600.0,
                        alignment=ft.alignment.center,
                        border_radius=10,
                        content=ft.Text(
                            "Welcome to Image Steganography",
                            size=35,
                        ),
                    ),

                    ft.Text(
                        "Image steganography is a technique that involves hiding secret data within an image without changing its perceptual qualities. The primary objective of steganography is to conceal the presence of information, rather than encrypting it, to prevent unauthorized access to data.",
                        text_align=ft.TextAlign.JUSTIFY,
                        width=600.0,
                    ),
                    ft.Container(
                        height=10.0,
                        width=10.0,
                    ),
                    ft.Container(
                        bgcolor=ft.colors.INDIGO_ACCENT_100,
                        padding=5,
                        width=600.0,
                        alignment=ft.alignment.center,
                        border_radius=10,
                        content=ft.Text(
                            "Encryption Process",
                            size=22,
                        ),
                    ),
                    ft.Container(
                        width=600.0,
                        content=ft.Row(
                            [
                                ft.Icon(name=ft.icons.EMAIL_ROUNDED, size=45.0),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_ROUNDED),
                                ft.Icon(name=ft.icons.LOCK_ROUNDED, size=45.0),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_ROUNDED),
                                ft.Icon(name=ft.icons.MAIL_LOCK_ROUNDED, size=45.0),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        ),
                    ),
                    ft.Text(
                        "Software using AES(Advanced Encryption Algorithm) for encryption & decryption of the data which helps to ensure confidentiality of the data, Encrypted Data then gets embedded into the image...",
                        text_align=ft.TextAlign.JUSTIFY,
                        width=600.0,
                    ),
                    ft.Container(
                        height=10.0,
                        width=10.0,
                    ),
                    ft.Container(
                        bgcolor=ft.colors.INDIGO_ACCENT_100,
                        padding=5,
                        width=600.0,
                        alignment=ft.alignment.center,
                        border_radius=10,
                        content=ft.Text(
                            "Decryption Process",
                            size=22,
                        ),
                    ),
                    ft.Container(
                        width=600.0,
                        content=ft.Row(
                            [
                                ft.Icon(name=ft.icons.EMAIL_ROUNDED, size=45.0),
                                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED),
                                ft.Icon(name=ft.icons.LOCK_ROUNDED, size=45.0),
                                ft.Icon(name=ft.icons.ARROW_BACK_ROUNDED),
                                ft.Icon(name=ft.icons.MAIL_LOCK_ROUNDED, size=45.0),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        ),
                    ),
                    ft.Text(
                        "At the Decryption Side, Encrypted data is extracted and provided to decryption function which will generate plain text from encrypted text with specific secret key...",
                        text_align=ft.TextAlign.JUSTIFY,
                        width=600.0,
                    ),
                ],
                alignment=ft.alignment.center,
                expand=True,
            ),
        )
