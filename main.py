# Creating dictonaries for roommates use
roommates = {1: "Sarfaraz", 2: "Sashant", 3: "Prabhjot"}
log = {1: "Exercise", 2: "Diet"}

# log current date and time
def getdate():
    import datetime

    return datetime.datetime.now()


try:

    # Input the selected roommate and his option to log or retrieve
    print("Select your name:")
    for key, value in roommates.items():
        print(f"Press {key} for {value}")
    roommate = int(input())

    print(f"\nSelected roommate is {roommates[roommate]}")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    num = int(input())

    # If he wants to log a new diet or exercise in his file
    if num == 1:
        for key, value in log.items():
            print(f"Press {key} to log {value}")
        log_num = int(input())
        print(f"Selected Job : {log[log_num]}")
        f = open(roommates[roommate] + "_" + log[log_num] + ".txt", "a")
        add_more = "y"
        while add_more != "n":
            print(f"Enter {log[log_num]}")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            add_more = input("ADD MORE ? y/n:")
            continue
        f.close()

    # If he wants to retrieve his logged diet or exercise file
    elif num == 2:
        for key, value in log.items():
            print(f"Press {key} to retrieve {value}")
        log_num = int(input())
        print(f"{roommates[roommate]}-{log[log_num]} Report :")
        f = open(roommates[roommate] + "_" + log[log_num] + ".txt")
        content = f.readlines()
        for line in content:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")


except Exception as e:
    print("Wrong Input !!!")
