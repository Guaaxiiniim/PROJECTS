import pyautogui as pag
import time
import yaml

def main():
    print("Dota 2 Auto Accept Script\nWritten by Guaaxiiniim.\n")
    print("Reading config file...")
    with open("config.yaml", "r") as stream:
        try :
            config = yaml.safe_load(stream)
        except:
            pag.alert("Error! Can't load config.yaml")
            exit()

    print("Searching for accept button like object(s)...")
    found = False
    while True:
        coors = pag.locateCenterOnScreen(
            config["PATH_TO_IMG"], grayscale=config["GRAYSCALE"], confidence=config["CONFIDENCE"]
        )
        if coors == None:
            if found:
                pag.alert("Auto-accepted :3\nClick OK to continue.")
                print("Continue searching for accept button like object(s)...")
                found = False
            time.sleep(config["CHECK_INTERVAL"])
        else:
            if found:
                print("Accept-button-like object does not seem to disappear.")
            found = True
            print(
                "Found an accept button like object at\t{},\t{}".format(coors.x, coors.y))
            pag.click(
                x=coors.x,
                y=coors.y,
                interval=config["CHECK_INTERVAL"],
                clicks=config["NUM_OF_CLICKS"],
                button="left",
            )
            print("\t--> clicked.")
        

if __name__ == "__main__":
    main()
