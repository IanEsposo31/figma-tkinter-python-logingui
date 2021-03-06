
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("862x519")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    215.0000000000001,
    259.0,
    image=image_image_1
)

canvas.create_rectangle(
    431.0000000000001,
    0.0,
    862.0000000000001,
    519.0,
    fill="#F1C858",
    outline="")

canvas.create_text(
    601.0000000000001,
    366.0,
    anchor="nw",
    text="Dont have an account?",
    fill="#000000",
    font=("NATS", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    657.5000000000001,
    271.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=497.0000000000001,
    y=257.0,
    width=321.0,
    height=20
)

canvas.create_text(
    450.0000000000001,
    210,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("NATS", 18 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    657.5000000000001,
    211.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=497.0000000000001,
    y=200.0 ,
    width=321.0,
    height= 12
)

canvas.create_text(
    450.0000000000001,
    150,
    anchor="nw",
    text="Username:",
    fill="#000000",
    font=("NATS", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=570.0000000000001,
    y=314.0,
    width=182.0,
    height=45.0
)

canvas.create_text(
    600.0000000000001,
    115.0,
    anchor="nw",
    text="L O G I N",
    fill="#000000",
    font=("NATS", 24 * -1)
)
window.resizable(False, False)
window.mainloop()