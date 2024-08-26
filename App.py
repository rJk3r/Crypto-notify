# GUI

from pathlib import Path
import os

# get current directory
current_dir = Path(__file__).parent.resolve()

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

PROGRAM_PATH = Path(__file__).parent
ASSETS_PATH = PROGRAM_PATH / 'ASSETS'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Canvas component (Parent:App)
class CanvasComponent(Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.config(
            bg = "#263B53",
            height=600,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.place(
            x=0,
            y=0
        )

        self.create_rectangle(
            0.0,
            0.0,
            400.0,
            600.0,
            fill="#FFFFFF",
            outline="")

        self.create_rectangle(
            0.0,
            0.0,
            400.0,
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

        self.create_rectangle(
            6.0,
            4.0,
            51.0,
            49.0,
            fill="#FFFFFF",
            outline="")


# LoginButton component (Parent:App)
class LoginButtonComponent(Button):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        button_image_1: PhotoImage = PhotoImage(
            file=relative_to_assets("img/button_1.png"))
        self.config(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.title("CryptoNotify")  # Window name
        self.geometry("400x600") # Window size
        self.configure(bg = "#263B53") # Window background default color

        #canvas
        self.canvas = CanvasComponent(self)
        self.canvas.pack()

        # Login Button
        self.button_1 = LoginButtonComponent(self)
        self.button_1.place(    # set button size and position
            x=67.0,
            y=418.0,
            width=267.0,
            height=69.0
        )
        self.resizable(False, False)
        self.mainloop()  # Run window

    def launched(self):
        if (self.button_1.winfo_exists() == True):
                launchState = True
                return launchState
        else:
            launchState = False
            return  launchState


    def button_click(self):
        """Функция, вызываемая при нажатии на кнопку."""
        self.label.config(text="Кнопка нажата!")
