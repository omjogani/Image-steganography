# import customtkinter
# from PIL import Image
# import os
#
# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")
#
# root = customtkinter.CTk()
# root.geometry("500x350")
#
#
# def login():
#     print("Test")
#
#
# image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/background.jpg")
#
# backgroundImage = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
# backgroundImage.pack()
#
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)
#
# label = customtkinter.CTkLabel(master=frame, text="Login System", font=("SF Pro Text", 24))
# label.pack(pady=12, padx=10)
# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)
#
# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
# entry2.pack(pady=12, padx=10)
#
# button = customtkinter.CTkButton(master=frame, text="Login", command=login)
# button.pack(pady=12, padx=10)
#
# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx=10)
#
# root.mainloop()
#
import customtkinter
import os
from PIL import Image


class MainPanel(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Image Steganography")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../Assets/")
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "locked.png")),
            size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "background.jpg")),
            size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "background.jpg")),
            size=(20, 20))
        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "home.png")),
            dark_image=Image.open(os.path.join(image_path, "home.png")),
            size=(20, 20))
        self.key_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "key.png")),
            dark_image=Image.open(os.path.join(image_path, "key.png")),
            size=(20, 20))
        self.encryption_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "encryption.png")),
            dark_image=Image.open(os.path.join(image_path, "encryption.png")),
            size=(20, 20))
        self.decryption_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "encryption.png")),
            dark_image=Image.open(os.path.join(image_path, "encryption.png")),
            size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, text=" Image Steganography",
            image=self.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
            text="Home",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40,
            border_spacing=10, text="Key Generator",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.key_image, anchor="w",
            command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40,
            border_spacing=10, text="Encryption",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.encryption_image, anchor="w",
            command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40,
            border_spacing=10, text="Decryption",
            fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.decryption_image, anchor="w",
            command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=10, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="Hello There",
            image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame, text="CTkButton",
            image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.home_frame_button_3 = customtkinter.CTkButton(
            self.home_frame, text="CTkButton",
            image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.home_frame_button_4 = customtkinter.CTkButton(
            self.home_frame, text="CTkButton",
            image=self.image_icon_image, compound="top", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
