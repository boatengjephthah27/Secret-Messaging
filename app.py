from hashlib import new
import graphipcs as g, time as t     

intro_msg = g.intro
for columns in intro_msg:
    print(columns, end="")
    t.sleep(0.0005)

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"] 
    
numbers = ['0','1','2','3','4','5','6','7','8','9']


user_choice_msg = """

\nDo you want to 

Decode   or   Encode    

---:  """
for columns in user_choice_msg:
    print(columns, end="")
    t.sleep(0.009)

while True:
    user_choice = input().lower()
    if user_choice == "decode" or user_choice == "encode":
        break
    else:
        es = "\nWrong input option, Type from the given options! ---:   "
        for columns in es:
            print(columns, end="")
            t.sleep(0.009)

msg_paste_msg = "\nPaste/type your message    \n\n---:  "
for columns in msg_paste_msg:
    print(columns, end="")
    t.sleep(0.009)
msg_paste = input().lower()

shift_no_msg = "\nHow many secret shifts ---:   "
for columns in shift_no_msg:
    print(columns, end="")
    t.sleep(0.009)

while True:
    try:
        shift_no = int(input())
        break
    except:
        ex = "\nWrong input, Input must be an integer! ---:   "
        for columns in ex:
            print(columns, end="")
            t.sleep(0.009)

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

    enc_art = g.encrypt
    for columns in enc_art:
        print(columns, end="")
        t.sleep(0.0007)
    
    loading_dots = "......."
    for columns in loading_dots:
        print(columns, end="")
        t.sleep(0.7)

    out_msg = f"\n\n\tYour encrypted message is - \n\n{encrypt_text}\n\n"
    for columns in out_msg:
        print(columns, end="")
        t.sleep(0.05)

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

    dec_art = g.decrypt
    for columns in dec_art:
        print(columns, end="")
        t.sleep(0.0007)

    loading_dots = "......."
    for columns in loading_dots:
        print(columns, end="")
        t.sleep(0.7)

    out_msg = f"\n\n\tYour decrypted message is - \n\n{decrypt_text}\n\n"
    for columns in out_msg:
        print(columns, end="")
        t.sleep(0.05)




if user_choice == "decode":
    decrypt(msg_paste, shift_no)

elif user_choice == "encode":
    encrypt(msg_paste, shift_no)

































































































