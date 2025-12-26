import json
import pathlib
import time
import os
from dependencies.input import get_action
def get_formatted_datetime():
    format_string = "%m/%d/%Y|%H:%M"
    current_time_struct = time.localtime()
    formatted_output = time.strftime(format_string, current_time_struct)
    return formatted_output
def login(uuid,password,new = bool):
    with open(file=str(uuid)+".json",mode="r") as user:
        userinfo = json.load(user)
    with open(file=str(uuid)+"_history.json") as history:
        userhistory = json.load(history)
    print("--------------------------------------------------")
    if new == True:
        print(f"welcome {userinfo["name"]}")
        print("press ctlr+c to exit")
    print("press 1 to check your money")
    print("press 2 to transfer money")
    print("press 3 to check transfer history")
    login_action = get_action("int",3)
    if login_action == 3:
        print("--------------------------------------------------")
        print("")
        print("history:")
        for key in userhistory:
            value = userhistory[key]
            print(f"{key}: {value}")
        login(uuid,password,False)
    if login_action == 1:
        print("--------------------------------------------------")
        print("")
        print(f"money: you have {userinfo["money"]}naira")
        login(uuid,password,False)
    if login_action == 2:
        entering_uuid = True
        while entering_uuid:
            print("please type the uuid to send money to")
            user_send_id = get_action("int")
            filepath = str(user_send_id)+".json"
            file = pathlib.Path(filepath)
            if file.is_file() == True:
                with open(filepath,"r") as reciever:
                    reciever_username = json.load(reciever)  
                    name = reciever_username["name"]
                    print(f"is the account name {name}?")
                    print("type 1 for yes,0 for no")
                    yes_or_no = get_action("int",1,zero_allowed=True)
                    if yes_or_no == 1:
                        entering_uuid = False
            else:
                print("that is not a valid uuid")
        print(f"how much money do you want to send to {name}")
        money = userinfo["money"]
        login_send_Money = get_action("int",money,True)
        print("before we contine, type your security number")
        real_security_key = userinfo["security code"]
        is_security_key_correct = get_action(security_key=real_security_key,is_checking_security_key=True)
        userinfo["money"] = money - login_send_Money
        date = get_formatted_datetime()
        
        with open(file=str(uuid)+".json",mode='w') as user_file:
            json.dump(userinfo, user_file, indent=4)
        receiver_filepath = str(user_send_id)+".json"
        with open(receiver_filepath, mode='r') as sender_read:
            sender_info = json.load(sender_read)
        
        sender_info["money"] += login_send_Money
        
        with open(receiver_filepath, mode='w') as sender_write:
            json.dump(sender_info, sender_write, indent=4)
        user_history_filepath = str(uuid)+"_history.json"
        if os.path.getsize(user_history_filepath) > 0:
             with open(user_history_filepath, mode='r') as user_history_read:
                 user_history_data = json.load(user_history_read)
        else:
             user_history_data = {}
        new_entry_text = f"{date}: you transfered {login_send_Money}naira to {user_send_id}({name})"
        user_history_data[str(len(user_history_data) + 1)] = new_entry_text
        with open(user_history_filepath, mode='w') as user_history_write:
            json.dump(user_history_data, user_history_write, indent=4)
        receiver_history_filepath = str(user_send_id)+"_history.json"
        if os.path.getsize(receiver_history_filepath) > 0:
            with open(receiver_history_filepath, mode='r') as recieve_history_read:
                receive_history_data = json.load(recieve_history_read)
        else:
            receive_history_data = {}
        sender_name = userinfo["name"]
        new_entry_text_rec = f'{date}: {sender_name}({uuid}) sent {login_send_Money} to you'
        receive_history_data[str(len(receive_history_data) + 1)] = new_entry_text_rec
        with open(receiver_history_filepath, mode='w') as recieve_history_write:
            json.dump(receive_history_data, recieve_history_write, indent=4)
        print("succesful transfer")