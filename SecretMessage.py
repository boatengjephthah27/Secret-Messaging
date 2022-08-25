from curses.textpad import Textbox
from email.mime import image
from tkinter import *





# ***************************************** CONSTANTS ****************************************************

color = "#F9F9F9"
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"] 
    
numbers = ['0','1','2','3','4','5','6','7','8','9']






# ***************************************** FUNCTIONS ****************************************************




def encrypt(msg_, shift):
    encrypt_text = ""
    for char in msg_:
        if char in letters:
            post_now = letters.index(char)
            new_post = int(post_now + shift)
            if new_post > len(letters):
                new_post -= len(letters)
            new_msg = letters[new_post]
            encrypt_text += new_msg
        elif char in numbers:
            post_now = numbers.index(char)
            new_post = int(post_now + shift)
            if new_post > len(numbers):
                new_post -= len(numbers)
            new_msg = numbers[new_post]
            encrypt_text += new_msg
        else:
            encrypt_text += char

   

def decrypt(msg_, shift):
    decrypt_text = ""
    for char in msg_:
        if char in letters:
            post_now = letters.index(char)
            new_post = int(post_now - shift)
            if new_post < 0:
                new_post += len(letters)
            new_msg = letters[new_post]
            decrypt_text += new_msg
        elif char in numbers:
            post_now = numbers.index(char)
            new_post = int(post_now - shift)
            if new_post < 0:
                new_post += len(numbers)
            new_msg = numbers[new_post]
            decrypt_text += new_msg
        else:
            decrypt_text += char

   










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