import time
import random
def randomm(a,b):
    return random.uniform(a,b)

def get_action(type=None,max=None,money=None,zero_allowed=False,security_key=0,is_checking_security_key = False):
    time.sleep(randomm(0.5,1.0))
    if type == "str":
        time.sleep(randomm(1.5,2.5))
        return str(input("type here: "))
    if type == "int":
        if max == None:
            returning_integer = True
            while returning_integer:
                integer = input("type here: ")
                returning_integer_phase2 = False
                try:
                    returning_integer_phase2 = True
                    integer =  int(integer)
                except Exception:
                    print("that is not a number, try again")
                    time.sleep(randomm(0.5,1.5))
                if not zero_allowed == True:
                    if returning_integer_phase2 == True:
                        try:
                            if integer < 0:
                                print("the number has to be higher than 0, try again")
                                time.sleep(randomm(0.5,1.5))
                            else:
                                returning_integer = False
                                time.sleep(randomm(1.5,2.5))
                                return integer
                        except Exception:
                            print("an unknown error occured please try again")
                            time.sleep(randomm(0.5,1.5))
                else:
                    returning_integer_phase3 = True
        if not max == None:
            returning_integer = True
            while returning_integer:
                integer = input("type here: ")
                returning_integer_phase2 = False
                returning_integer_phase3 = False
                try:
                    returning_integer_phase2 = True
                    integer =  int(integer)
                except Exception:
                    print("that is not a number, try again")
                    time.sleep(randomm(0.5,1.5))
                if not zero_allowed == True:
                    if returning_integer_phase2 == True:
                        try:
                            if integer <= 0:
                                print("the number has to be higher than 0, try again")
                                time.sleep(randomm(0.5,1.5))
                            else:
                                returning_integer_phase3 = True
                        except Exception:
                            print("an unknown error occured please try again")
                            time.sleep(randomm(0.5,1.5))
                else:
                    returning_integer_phase3 = True
                if returning_integer_phase3 == True:
                    if integer > max:
                        if money == True:
                            print("you do not have enough money to do that, try again")
                            time.sleep(0.5)
                            print(f"you have {str(max)}naira")
                            
                        else:
                            print(f"the max number is {max}, please try again")
                            time.sleep(randomm(0.5,1.5))
                    else:
                        returning_integer = False
                        time.sleep(randomm(1.5,2.5))
                        return integer
    if is_checking_security_key == True:
        while is_checking_security_key:
            print("type your security key")
            key = get_action("int")
            time.sleep(randomm(2.5,3.5))
            if key == security_key:
                print("correct, proceeding to transfer now")
                time.sleep(randomm(1.5,2.5))
                return True
            else:
                print("incorrect security key, try again")
                time.sleep(randomm(0.5,1.5))