"""Experimental phase"""

import os.path
import sys
from typing import Optional

from ashcrypt.utils.safepack import file as af
from ashcrypt.utils.safepack import text as at

print("Welcome to the CLI")

commands = (
    "Commands : \n"
    "\tq: to quit the program \n"
    "\tc : view commands\n"
    "\te: for encryption\n"
    "\td : for decryption\n"
    "\tef : to encrypt a file\n"
    "\tdf : to decrypt a file\n"
)

global key


def input_selection(
    q=Optional[int],
    c=Optional[int],
    e=Optional[int],
    d=Optional[int],
    ef=Optional[int],
    df=Optional[int],
):
    global encflag, decFlag, file_decFlag, file_encFlag
    if q == 1:
        sys.exit()
    if c == 1:
        print(commands)
    if e == 1:
        file_decFlag = False
        file_encFlag = False
        decFlag = False
        encflag = True
        enc_f()
    if d == 1:
        file_decFlag = False
        file_encFlag = False
        encflag = False
        decFlag = True
        dec_f()
    if ef == 1:
        decFlag = False
        encflag = False
        file_decFlag = False
        file_encFlag = True
        file_enc()
    if df == 1:
        encflag = False
        decFlag = True
        file_encFlag = False
        file_decFlag = True
        file_dec()
    else:
        pass


def input_wrap(inp):
    inp = inp.lower()
    if inp == "c":
        input_selection(c=1)
        return "c"
    if inp == "q":
        input_selection(q=1)
        return "q"
    if inp == "e":
        input_selection(e=1)
        return "e"
    if inp == "d":
        input_selection(d=1)
        return "d"
    if inp == "ef":
        input_selection(ef=1)
        return "ef"
    if inp == "df":
        input_selection(df=1)
        return "df"
    else:
        return None


def intro():
    while True:
        print("Program started running..")
        print("Press c to view commands : ")
        while True:
            n = input("Press..\n")
            input_wrap(n)


def keysetup():
    outer = True
    inner = True
    while outer:
        global key
        key = ""
        i = input("Do you have a key ?(y/n) : ")
        input_wrap(i)
        if i.lower() == "n":
            print("Here's your key : ")
            key = at.Crypt.genkey()
            print(key)
            inner = False
            outer = False
        elif i.lower() == "y":
            while inner:
                print("insert your key here : ")
                kk = input()
                input_wrap(kk)
                if at.Crypt.keyverify(kk) == 1:
                    print("Key selected\n")
                    key = kk
                    inner = False
                    outer = False
                else:
                    print("Enter a valid key !\n")


encflag = True


def enc_f():
    keysetup()
    while encflag:
        print()
        global key
        print("press c to view commands.. ")
        message = input("Encrypt a message : ")
        input_wrap(message)
        a = at.Crypt(message, key=key)
        enc = a.encrypt()
        if (enc[0]) == 1:
            print("Success ! Here's the message : ")
            print("\t", enc[1], "\n")
        else:
            print("Error occurred during the encryption process\n")


decFlag = True


def dec_f():
    keysetup()
    while decFlag:
        print()
        global key
        print("press c to view commands.. ")
        message = input("Decrypt a message : ")
        input_wrap(message)
        a = at.Crypt(message, key=key)
        dec = a.decrypt()
        if (dec[0]) == 1:
            print("Success ! Here's the message : ")
            print("\t", dec[1], "\n")
        else:
            print("Error occurred during the decryption process\n")


file_encFlag = True


file_decFlag = True


def file_dec():
    keysetup()
    while file_decFlag:
        print()
        global key
        pre = input(
            "Running file decryption mode..\nPress the known commands or 'Enter' to continue.. : "
        )
        print()
        input_wrap(pre)
        if pre == "":
            print("You can use the commands AFTER entering the file name.. ")
            filename = input("Enter full file name to be Decrypted : ")
            target = af.CryptFile(filename, key)
            a = target.decrypt()
            if a == 1:
                print("File successfully decrypted + removed .crypt extension")
                print(f"File is now named {os.path.splitext(filename)[0]}")
            if a == 2:
                print("Cannot decrypt the file  when it is already empty")
            if a == 3:
                print(
                    f'The file named : "{filename}" does not exists , try specifying the whole sys path'
                )
            if a == 0:
                print(
                    "Error in the decryption process. Check if the the file is distorted or it might just be "
                    "decrypted already"
                )
            if a == 4:
                print("Unknown Error has occurred ( system related ) \n")
            if a == 5:
                print("ERROR : Key is Not 256-bit")
            if a == 6:
                print("ERROR : File is already decrypted")
            elif a == 7:
                print("ERROR : Given a directory instead of a file")


def file_enc():
    keysetup()
    while file_encFlag:
        print()
        global key
        pre = input(
            "Running file encryption mode..\nPress the known commands or 'Enter' to continue.. : "
        )
        print()
        input_wrap(pre)
        if pre == "":
            print("You can use the commands AFTER entering the file name.. ")
            filename = input("Enter full file name to be Encrypted : ")
            target = af.CryptFile(filename, key)
            a = target.encrypt()
            if a == 1:
                print("File successfully encrypted + added '.crypt' extension")
                print(f"File is now named : '{filename}.crypt' ")
            if a == 2:
                print("Cannot encrypt the file  when it is already empty")
            if a == 3:
                print(
                    f'The file named : "{filename}" does not exists , try specifying the whole sys path'
                )
            if a == 0:
                print(
                    "Error in the encryption process. Check if the the file is distorted"
                )
            elif a == 4:
                print("Unknown Error has occurred\n")
            if a == 5:
                print("ERROR : Key is Not 256-bit")
            if a == 6:
                print("ERROR : File is already encrypted")
            elif a == 7:
                print("ERROR : Given a directory instead of a file")


if __name__ == "__main__":
    intro()
