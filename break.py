from main import swap
import os

RUN = True

while RUN:
    plain_text = ""
    msg = input("\033[33mEnter the Ciphertext:\033[0m")
    for n in range(0,17576):
        plain_text += f"{n}: {swap(msg.lower(),n)}\n"
    file = os .open("break.txt",os.O_RDWR)
    os.write(file, plain_text.encode())
    os.close(file)