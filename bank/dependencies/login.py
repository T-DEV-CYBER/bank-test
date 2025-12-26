from  dependencies.input import get_action
import pathlib 
import json
from dependencies.logedin import login 
def log_in():
    print("--------------------------------------------------")
    print("welcome to login")
    print("press ctlr+c to exit")
    entering_uuid = True
    while entering_uuid:
        print("please type your uuid")
        login_uuid = get_action("int")
        filepath = str(login_uuid)+".json"
        file = pathlib.Path(filepath)
        if file.is_file() == True:
            with open(filepath,"r") as user:
                user_info = json.load(user)
                username = user_info["name"]
                real_password = user_info["password"]
            print(f"is your name {username}")
            print('press 1 if yes,0 if no')
            yes_or_no = get_action("int",2,zero_allowed=True)
            if yes_or_no == 1:
                entering_uuid = False
        else:
            print("that is not a valid uuid")
    print("great, now enter your password")
    tries = 3
    entering_password = True
    continueing = False
    while entering_password:
        login_password = get_action("int")
        if int(real_password) == int(login_password):
            entering_password = False
            continueing = True
        else:
            print("that is not a correct password")
            tries-=1
            if tries == 0:
                print("you no more have any tries,taking you back to home screen")
                entering_password = False
                continueing = False
    while continueing:
        login(login_uuid,login_password,True)

    

