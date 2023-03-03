import flet as ft


class HomeScreen:
    def __init__(self):
        super().__init__()

    def home_screen(self):
        # return ft.Text(value="Hello World", color="green")
        return ft.Container(
            expand=True,

            content=ft.Column(
                [
                    ft.Text("Welcome to Image Steganography"),
                    ft.Text("Welcome to Image Steganography"),
                    ft.Text("Welcome to Image Steganography"),
                    ft.Text("Welcome to Image Steganography"),
                ],
                alignment=ft.alignment.top_left,
                expand=True,
            ),

            bgcolor=ft.colors.AMBER,
        )
