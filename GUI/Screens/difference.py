import flet as ft

import Cryptography
from GUI.Constants import TextStyle
import cv2
from Steganography import DifferenceStego


class Difference:
    def __init__(self, page):
        self.page = page
        super().__init__()


    psnr = ft.Text(
        "",
        color=ft.colors.WHITE,
    )
    mse = ft.Text(
        "",
        color=ft.colors.WHITE,
    )
    ssim = ft.Text(
        "",
        color=ft.colors.WHITE,
    )
    response_message = ft.Text(
        "",
        color=ft.colors.GREEN_ACCENT,
    )

    information = "Choose Both Original & Stego Image to find difference between both images..."
    original_image_path = ""
    stego_image_path = ""
    def difference_panel(self):
        def handle_calculate_event(e):
            if self.original_image_path == "":
                self.response_message.value = "Please Choose Original Image"
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            if self.stego_image_path == "":
                self.response_message.value = "Please Choose Stego Image"
                self.response_message.color = ft.colors.RED_ACCENT
                self.response_message.update()
                return

            self.response_message.value = ""
            self.response_message.color = ft.colors.WHITE
            self.response_message.update()

            original = cv2.imread(self.original_image_path)
            compressed = cv2.imread(self.stego_image_path, 1)

            value = DifferenceStego.calculatePSNR(original, compressed)
            value2 = DifferenceStego.calculateMSE(original, compressed)
            value3 = DifferenceStego.calculateSSIM(original, compressed)
            # print(type(value))
            self.psnr.value = "PSNR: " + str(value)
            self.mse.value = "MSE: " + str(value2)
            self.ssim.value = "SSIM: " + str(value3)
            self.psnr.update()
            self.ssim.update()
            self.mse.update()
            # print(f"PSNR value is {value} unit")
            # print(f"MSE value is {value2} unit")
            # print(f"SSIM value is {value3} unit")
        def on_dialog_result1(e: ft.FilePickerResultEvent):
            print("Selected files:", e.files)
            self.original_image_path = e.files[0].path


        def on_dialog_result2(e: ft.FilePickerResultEvent):
            print("Selected files:", e.files)
            self.stego_image_path = e.files[0].path


        my_pick1 = ft.FilePicker(on_result=on_dialog_result1)
        self.page.overlay.append(my_pick1)
        my_pick2 = ft.FilePicker(on_result=on_dialog_result2)
        self.page.overlay.append(my_pick2)
        return ft.Container(
            expand=True,
            content=ft.Column(
                [
                    ft.Text(
                        "Compare Original & Stego Image",
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
                    ft.Container(
                        width=500.0,
                        content=ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Choose Original Image",
                                    icon=ft.icons.UPLOAD_FILE,
                                    on_click=lambda _: my_pick1.pick_files(),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        width=500.0,
                        content=ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Choose Stego Image",
                                    icon=ft.icons.UPLOAD_FILE,
                                    on_click=lambda _: my_pick2.pick_files(),
                                ),
                            ],
                        ),
                    ),
                    ft.FilledButton(text="Calculate", on_click=handle_calculate_event),
                    self.response_message,
                    self.psnr,
                    self.mse,
                    self.ssim,
                ],
                alignment=ft.alignment.top_left,
                expand=True,
            ),
            alignment=ft.alignment.center,
        )
