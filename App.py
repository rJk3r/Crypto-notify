# GUI

from pathlib import Path
import os

# get current directory
current_dir = Path(__file__).parent.resolve()

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, NW
from PIL import Image, ImageTk

PROGRAM_PATH = Path(__file__).parent
ASSETS_PATH = PROGRAM_PATH / 'ASSETS'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Canvas component (Parent:App)
class CanvasComponent(Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        # Default canvas background

        firstBG = Image.open(relative_to_assets("img/bg.png"))
        firstBG = firstBG.resize((400, 600))
        firstAppBg = ImageTk.PhotoImage(firstBG)

        # Logo

        logoIMG = Image.open(relative_to_assets("img/logo.png"))
        logoIMG = logoIMG.resize((45, 45))
        logoRectangleBG = ImageTk.PhotoImage(logoIMG)

        self.config(
                height=600,
                width=400,
                bd=0,
                highlightthickness=0,
                relief="ridge"
            )

        self.create_image(
            0,
            0,
            anchor=NW,
            image=firstAppBg
        )

        self.place(
            x=0,
            y=0
        )

        self.create_rectangle(
            0.0,
            0.0,
            400,
            53.0,
            fill="#171717",
            outline="")


        self.create_text(
            58.0,
            12.0,
            anchor="nw",
            text="Crypto notify",
            fill="#FFFFFF",
            font=("Inter Bold", 24 * -1)
        )

        self.create_image(
            6.0,
            4.0,
            anchor=NW,
            image=logoRectangleBG,
            )

        self.image = [firstAppBg, logoRectangleBG]


# LoginButton component (Parent:App)
class LoginButtonComponent(Button):
    def __init__(self, parent, appState,  *args, **kwargs):
        super().__init__(parent)
        button_image_1: PhotoImage = PhotoImage(
            file=relative_to_assets("img/button_1.png"))
        self.config(
            image=button_image_1,
            borderwidth=0,
            command=self.button_click,
            highlightthickness=0,
            relief="flat"
        )
        self.image = button_image_1

    def button_click(self):
        print(self.)
        pass
class App(Tk):
    def __init__(self, btnInstance,  *args, **kwargs):
        self.btnComponentInstance = btnInstance
        super().__init__(*args, **kwargs)
        self.launchState = False


        self.title("CryptoNotify")  # Window name
        self.geometry("400x600") # Window size
        self.configure(bg = "#263B53") # Window background default color

        #canvas
        self.canvas = CanvasComponent(self)
        self.canvas.pack()

        # Login Button
        self.button_1 = LoginButtonComponent(self, command=self.button_click)
        self.button_1.place(    # set button size and position
            x=67.0,
            y=418.0,
            width=267.0,
            height=69.0
        )
        self.resizable(False, False)
        self.mainloop()  # Run window

    def changeLaunchState(self):
        self.launchState = True
        pass


    def button_click(self):
        self.launchState = True
        return self.launchState
