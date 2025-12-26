from dependencies.input import get_action
import random
import json
from dependencies.login import log_in
from dependencies.logedin import get_formatted_datetime
def signin():
    print("--------------------------------------------------")
    print("welcome to the account creation setup(acs)")
    print("please type a name for the account")
    new_user_name = get_action("str")
    print("great!, now lets move on to setting a password")
    print("please type a password")
    new_user_password = get_action("str")
    print("good! your done setting up your account")
    print("remember these information, they will be need for it in the future")
    new_user_uuid = random.randint(111111111111,999999999999)
    new_user_security_code = random.randint(11111111,99999999)
    new_user_information = {"name":new_user_name,"password":new_user_password,"security code":new_user_security_code,"money":0}
    new_user_history = {1:f"{get_formatted_datetime()}: you just created the account"}
    with open(file = str(new_user_uuid)+".json", mode="x+") as new_user:
        json.dump(new_user_information,new_user,indent=4)
    with open(file = str(new_user_uuid)+"_history.json", mode="x+") as new_user_history_file:
        json.dump(new_user_history,new_user_history_file,indent=4)
    print(f"your uuid is {new_user_uuid} and your security code is {new_user_security_code}")