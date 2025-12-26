import home
import traceback
debug = True
while True:
    try:
        home.home()
    except Exception as exeption:
        if debug == True:
            traceback.print_exc()
            print(f"error: {exeption}")
        print("AN ERROR OCCURED WHILE RUNNING")
        print("RESTARTING NOW...")
    except KeyboardInterrupt:
        print("YOU EXITED HOME, RESTARTING")
    