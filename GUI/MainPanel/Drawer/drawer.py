from flet import *
from functools import partial
import pika

class ModernNavBar(UserControl):
    def __init__(self, func):
        self.func = func
        super().__init__()

    def handle_home_screen(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='update_ui')
        channel.basic_publish(exchange='', routing_key='update_ui', body='HOME')

    def highlight_container(self, e):
        if e.data == "true":
            e.control.bgcolor = "white10"
            e.control.update()

            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].color = "white"
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()

            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].color = "white54"
            e.control.content.update()

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
        print("containerd_icon")
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.highlight_container(e),
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
    def build(self):
        print("build")
        return Container(
            width=200,
            height=580,
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.user_data("IS", "Image Steganography", "Hide Data into Image"),
                    # Container(
                    #     width=30,
                    #     height=30,
                    #     bgcolor="bluegrey600",
                    #     border_radius=8,
                    #     on_click=partial(self.func),
                    #     content=Icon(
                    #         name=icons.DOUBLE_ARROW_ROUNDED,
                    #     )
                    # ),
                    Divider(height=5, color="white24"),
                    GestureDetector(
                        on_tap=self.handle_home_screen,
                        content=self.contained_icon(icons.HOME_ROUNDED, "Home",),
                    ),
                    self.contained_icon(icons.KEY_ROUNDED, "Generate Key"),
                    self.contained_icon(icons.LOCK_ROUNDED, "Encryption"),
                    self.contained_icon(icons.LOCK_OPEN_ROUNDED, "Decryption"),
                    self.contained_icon(icons.CODE_ROUNDED, "Comparison"),
                    Divider(height=5, color="white24"),
                ],
            ),
        )

