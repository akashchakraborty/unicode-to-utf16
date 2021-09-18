import os
import sys
import time
import pyperclip as cp


def run(data):
    a = data.encode("utf-16")
    b=a.hex()
    cp.copy(b)
    print("UTF-16 DATA:\n",b)
def exit():
    banner = """
    Hey, Bye!
    Have a great testing ahead !
    """
    sys.exit(banner)
    
def main(text):
    if text == "X":
        exit()
    elif text == "x":
        exit()
    else:
        run(text)

if __name__ == "__main__":
    banner2 = """
                                         ___ ___                                             
 | | ._  o  _  _   _|  _    _|_  _    | | | |_   _   /| |_     _  _  ._      _  ._ _|_  _  ._ 
 |_| | | | (_ (_) (_| (/_    |_ (_)   |_| | |         | |_)   (_ (_) | | \/ (/_ |   |_ (/_ |  
                                                                                           
    """
    print(banner2)
    print("       Type 'X' to exit      ")
    while True:
        text = input("Enter the unicode: \n")
        main(text)
