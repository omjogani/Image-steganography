import flet as ft
from GUI.Constants import TextStyle


class GenerateKey:
    def __init__(self):
        super().__init__()

    information = "Enter File name without Extension, Enter Key Value that will be encrypted and stored in File."
    def generate_key(self):
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
                    ft.TextField(
                        label="Key File Name",
                        hint_text="Enter Key File Name",
                        width=500.0,
                        border_color=ft.colors.INDIGO_200,
                    ),
                    ft.TextField(
                        label="Key Value",
                        hint_text="Enter Key Value",
                        width=500.0,
                        multiline=True,
                        border_color=ft.colors.INDIGO_200,
                        min_lines=1,
                        max_lines=3,
                    ),
                    ft.FilledButton(text="Generate"),
                    # ft.DataTable(
                    #     columns=[
                    #         ft.DataColumn(ft.Text("Index"), numeric=True),
                    #         ft.DataColumn(ft.Text("File Name")),
                    #         ft.DataColumn(ft.Text("Path")),
                    #     ],
                    #     rows=[
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("1")),
                    #                 ft.DataCell(ft.Text("Key.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("2")),
                    #                 ft.DataCell(ft.Text("ENC.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("3")),
                    #                 ft.DataCell(ft.Text("EncKey.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("4")),
                    #                 ft.DataCell(ft.Text("Demo.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("1")),
                    #                 ft.DataCell(ft.Text("Key.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("2")),
                    #                 ft.DataCell(ft.Text("ENC.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("3")),
                    #                 ft.DataCell(ft.Text("EncKey.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #         ft.DataRow(
                    #             cells=[
                    #                 ft.DataCell(ft.Text("4")),
                    #                 ft.DataCell(ft.Text("Demo.key")),
                    #                 ft.DataCell(ft.Text("C:/Key/Key.key")),
                    #             ],
                    #         ),
                    #     ],
                    # ),


                ],
                alignment=ft.alignment.top_left,
                expand=True,
            ),
            alignment=ft.alignment.center,

            # bgcolor=ft.colors.BLUE,
        )
