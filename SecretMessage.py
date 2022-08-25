from tkinter import *





# ***************************************** CONSTANTS ****************************************************

color = "#B9FFF8"







# ***************************************** FUNCTIONS ****************************************************









# ***************************************** GUI ****************************************************

app = Tk()
app.title("Secret Message")
app.config(
    bg=color
)


canvas = Canvas(
    width=400,
    height=400,
    # bg=color,
    # highlightthickness=0
)
canvas.grid(row=0, column=0)

msglbl = Label(
    text="Your Message"
)








app.mainloop()