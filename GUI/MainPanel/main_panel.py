from flet import *
import time
from GUI.Screens import HomeScreen
from GUI.Screens import GenerateKey
from GUI.Screens import Encryption
from GUI.Screens import Decryption
from GUI.Screens import Difference


class MainPanel:

    page.title = "Image Steganography"
    page.horizontal_alignment = "start"
    page.vertical_alignment = "start"
    current_page = "ENCRYPTION"

    def main(self, page: Page):
        def handle_home_screen(e):
            self.current_page = "HOME"
            wrapper[1] = HomeScreen().home_screen()
            page.update()

        def handle_comparison_screen(e):
            self.current_page = "COMPARISON"
            wrapper[1] = Difference(page).difference_panel()
            page.update()

        def handle_key_generation_screen(e):
            self.current_page = "GENERATEKEY"
            wrapper[1] = GenerateKey().generate_key()
            page.update()

        def handle_encryption_screen(e):
            print("Enc")
            self.current_page = "ENCRYPTION"
            wrapper[1] = Encryption(page).encryption()
            page.update()

        def handle_decryption_screen(e):
            self.current_page = "DECRYPTION"
            wrapper[1] = Decryption(page).decryption()
            page.update()


        def user_data(self, initials: str, name: str, description: str):
            print("user_data")
            return Container(
                content=Row(
                    controls=[
                        Container(
                            width=42,
                            height=42,
                            border_radius=8,
                            bgcolor="bluegrey900",
                            alignment=alignment.center,
                            content=Text(
                                value=initials,
                                size=20,
                                weight="bold",
                            ),
                        ),
                        Column(
                            spacing=1,
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    value=name,
                                    size=15,
                                    weight="bold",
                                    opacity=1,
                                    animate_opacity=200,
                                ),
                                Text(
                                    value=description,
                                    size=13,
                                    weight="w400",
                                    color="white54",
                                    opacity=1,
                                    animate_opacity=200,
                                ),
                            ],
                        ),
                    ]
                )
            )

        def contained_icon(self, icon_name, text):
            return Container(
                width=180,
                height=45,
                border_radius=10,
                # on_hover=lambda e: highlight_container(e),
                ink=True,
                content=Row(
                    controls=[
                        IconButton(
                            icon=icon_name,
                            icon_size=25,
                            icon_color="white54",
                            selected=False,
                            style=ButtonStyle(
                                shape={
                                    "": RoundedRectangleBorder(radius=7),
                                },
                                overlay_color={"": "transparent"},
                            ),
                        ),
                        Text(
                            value=text,
                            color="white54",
                            size=15,
                            opacity=1,
                            animate_opacity=200,
                        ),
                    ],
                ),
            )

        # def build(self):
        #     print("build")
        build = Container(
            width=200,
            height=580,
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    user_data("IS", "IS", "Image Steganography", "Hide Data into Image"),

                    Divider(height=5, color="white24"),
                    GestureDetector(
                        on_tap=handle_home_screen,
                        content=contained_icon(icons.HOME_ROUNDED, icons.HOME_ROUNDED, "Home", ),
                    ),
                    GestureDetector(
                        on_tap=handle_key_generation_screen,
                        content=contained_icon(icons.KEY_ROUNDED, icons.KEY_ROUNDED, "Generate Key"),
                    ),
                    GestureDetector(
                        on_tap=handle_encryption_screen,
                        content=
                        contained_icon(icons.LOCK_ROUNDED, icons.LOCK_ROUNDED, "Encryption"),
                    ),
                    GestureDetector(
                        on_tap=handle_decryption_screen,
                        content=
                        contained_icon(icons.LOCK_OPEN_ROUNDED, icons.LOCK_OPEN_ROUNDED, "Decryption"),
                    ),
                    GestureDetector(
                        on_tap=handle_comparison_screen,
                        content=
                        contained_icon(icons.CODE_ROUNDED, icons.CODE_ROUNDED, "Comparison"),
                    ),
                    Divider(height=5, color="white24"),
                ],
            ),
        )

        wrapper = [
                Container(
                    width=200,
                    height=580,
                    animate=animation.Animation(500, "decelerate"),
                    border_radius=10,
                    padding=10,
                    # content=ModernNavBar(animated_navBar),
                    content=build,
                ),
                HomeScreen().home_screen(),
                # GenerateKey().generate_key(),
                # Encryption(page).encryption(),
                # Decryption(page).decryption(),
                # Difference(page).difference_panel()
            ]



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
            Row(wrapper, alignment=alignment.center),
        )
        page.update()
