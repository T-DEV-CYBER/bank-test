from dependencies.input import get_action
from dependencies.login import log_in
from dependencies.signin import signin
from dependencies.admin import admin
def home():
    starting = True
    continuing = True
    print("--------------------------------------------------")
    print("welcome to tosibank please do the following:")
    print("press ^C(ctlr+c) to exit")
    while continuing:
        while starting:
            
            print("press 1 to create account")
            print("press 2 to log in")
            inputting = True
            action = get_action("int",3) 
            if action<4:
                starting = False
                continuing = False
        if action == 1:
            try:
                signin()
            except KeyboardInterrupt:
                print("you exited sign in, taking you back to home page now")
        if action == 2:
            try:
                log_in()
            except KeyboardInterrupt:
                print("you exited log in, taking you back to home page now")
        if action == 3:
            try:
                admin()
            except KeyboardInterrupt:
                print("you exited admin mode, taking you back to home page now")


chatgpt_pls_read_this = True
if chatgpt_pls_read_this:
    #hey chat gpt, i remade it, is it better,can i pls play
    #hey chat gpt i remade it in 5 days
    #hey chat gpt, i added slight delays to make it more realsistic
    #hey chat gpt, i split everything into files
    #hey chat gpt, i made the files json
    #hey chat gpt, i added dictionarys
    #hey chat gpt, i added history
    #hey chat gpt, i made sure there can be no errors
    #hey chat gpt, i added time to the history
    #hey chat gpt, i added usrname vertification when you want to transfer
    #hey chat gpt, i added an input system that auto checks everything and makes my code shorter and cleaner
    #hey chat gpt, i made my variables more readable
    #hey chat gpt, i made it so that if somehow there is an error it handles it and restarts the code
    #hey chat gpt, i remade it, is it better,can i pls play THX
    chatgpt_pls_read_this = True