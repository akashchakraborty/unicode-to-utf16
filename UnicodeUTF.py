import os
import sys
import time
import pyperclip as cp


def run(data):
    try:
        a = data.encode("utf-16")
        b=a.hex()
        cp.copy(b)
        print("UTF-16 DATA:\n",b)
    except Exception as e:
        print(e)

def exit():
    try:
        banner = """
        Hey, Bye!
        Have a great testing ahead !
        """
        sys.exit(banner)
    except Exception as e:
        print(e)
    
def main(text):
    try:

        if text == "X":
            exit()
        elif text == "x":
            exit()
        else:
            run(text)
    except Exception as e:
        print(e)
        
try:
    banner2 = """
                                            ___ ___                                             
    | | ._  o  _  _   _|  _    _|_  _    | | | |_   _   /| |_     _  _  ._      _  ._ _|_  _  ._ 
    |_| | | | (_ (_) (_| (/_    |_ (_)   |_| | |         | |_)   (_ (_) | | \/ (/_ |   |_ (/_ |  
                                                                                            
        """
    print(banner2)
    print("                         Type 'X' to exit      ")
    while True:
        text = input("Enter the unicode: \n")
        main(text)
except Exception as e:
    print(e)