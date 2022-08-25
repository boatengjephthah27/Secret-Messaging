from curses.textpad import Textbox
from email.mime import image
from tkinter import *





# ***************************************** CONSTANTS ****************************************************

color = "#F9F9F9"







# ***************************************** FUNCTIONS ****************************************************









# ***************************************** GUI ****************************************************

app = Tk()
app.title("Secret Message")
app.config(
    bg=color,
    padx=20,
    pady=20
)


canvas = Canvas(
    width=300,
    height=172,
    bg=color,
    highlightthickness=0
)
canvas.grid(row=0, column=0, columnspan=2)

appimage = PhotoImage(file="pic.png")
canvas.create_image(
    150,86,
    image=appimage 
)


msglbl = Label(
    text="Your Message",
    bg=color,
    font=("arial", 24, "bold"),
    pady=10
)
msglbl.grid(row=1, column=0, columnspan=2)

msgin = Text(
    width=50,
    height=7,
    font=("courier", 16)
)
msgin.grid(row=2, column=0, columnspan=2)


outputlbl = Label(
    text="Output: Encoded/Decoded",
    bg=color,
    font=("arial", 24, "bold"),
    pady=10
)
outputlbl.grid(row=3, column=0, columnspan=2)

msgout = Text(
    width=50,
    height=7,
    font=("courier", 16)
)
msgout.grid(row=4, column=0, columnspan=2)


encode = Button(
    text="ENCODE",
    font=("courier", 20, "bold"),
    padx=4,
    pady=7,
    command=
)
encode.grid(row=5, column=0)

decode = Button(
    text="DECODE",
    font=("courier", 20, "bold"),
    padx=4,
    pady=7,
    command=
)
decode.grid(row=5, column=1)








app.mainloop()