from dependencies.input import get_action
import os
import json
from pathlib import Path
def admin():
    print("--------------------------------------------------")
    print("welcome to admin mode")
    print("what would you like to do:")
    print("press ctlr+c to exit admin mode")
    print("press 1 to add money to an account")
    print("press 2 to remove money to an account")
    admin_action = str(get_action("int",2))
    if admin_action == str(1):
        print("what uuid do you want to add money to")
        entering_uuid = True
        while entering_uuid:
            admin_uuid = get_action("str")
            uuid_file = Path(admin_uuid+".json")
            if uuid_file.is_file():
                entering_uuid = False
            else:
                print("that is not a valid id, try again")
        with open(file = admin_uuid+".json",mode="r") as file:
            user_info = json.load(file)
        money = user_info["money"]
        print("how much money do you want to add to the account")
        admin_add_money = get_action("int")
        user_info["money"] = money+admin_add_money
        with open(file=admin_uuid+".json",mode="w+") as file:
            json.dump(user_info,file,indent=4)
        print("succesfull transfer")
    if admin_action == str(2):
        print("what uuid do you want to remove money from")
        entering_uuid = True
        while entering_uuid:
            admin_uuid = get_action("str")
            uuid_file = Path(admin_uuid+".json")
            if uuid_file.is_file():
                entering_uuid = False
            else:
                print("that is not a valid id, try again")
        with open(file = admin_uuid+".json",mode="r") as file:
            user_info = json.load(file)
        money = user_info["money"]
        print("how much money do you want to remove from the account")
        admin_add_money = get_action("int")
        user_info["money"] = money-admin_add_money
        if user_info["money"]<0:
            user_info["money"] = 0
        with open(file=admin_uuid+".json",mode="w+") as file:
            json.dump(user_info,file,indent=4)
        print("succesfull")

        