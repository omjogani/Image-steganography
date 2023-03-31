from flet import *
import time
from GUI.MainPanel import ModernNavBar
from GUI.Screens import HomeScreen
from GUI.Screens import GenerateKey
from GUI.Screens import Encryption
from GUI.Screens import Decryption


class MainPanel:
    page.title = "Image Steganography"
    page.horizontal_alignment = "start"
    page.vertical_alignment = "start"

    def main(page: Page):
        def animated_navBar(e):
            if page.controls[0].width != 62:
                for item in (
                    page.controls[0]
                    .content.controls[0]
                    .content.controls[0]
                    .content.controls[1]
                    .controls[:]
                ):
                    item.opacity = 0
                    item.update()

                for item in page.controls[0].content.controls[0].content.controls[3:]:
                    if isinstance(item, Container):

                        item.content.controls[1].opacity = 0
                        item.content.update()

                time.sleep(0.2)

                page.controls[0].width = 62
                page.controls[0].update()

            else:
                page.controls[0].width = 200
                page.controls[0].update()

                time.sleep(0.2)

                for item in (
                    page.controls[0]
                    .content.controls[0]
                    .content.controls[0]
                    .content.controls[1]
                    .controls[:]
                ):
                    item.opacity = 1
                    item.update()

                for item in page.controls[0].content.controls[0].content.controls[3:]:
                    if isinstance(item, Container):

                        item.content.controls[1].opacity = 1
                        item.content.update()

        page.add(
            Row(
                [
                    Container(
                        width=200,
                        height=580,
                        animate=animation.Animation(500, "decelerate"),
                        border_radius=10,
                        padding=10,
                        content=ModernNavBar(animated_navBar),
                    ),
                    HomeScreen().home_screen(),
                    # GenerateKey().generate_key(),
                    # Encryption(page).encryption(),
                    # Decryption(page).decryption(),


                ],
                alignment=alignment.center,
            )
        )
        page.update()
