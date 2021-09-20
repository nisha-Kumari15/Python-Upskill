import random 
import sys

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

   
SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""
THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""
FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""
SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""
THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

swapin = 0
swaplose = 0
ogwin = 0
oglose = 0

while True:
    doorwithcar = random.randint(1,3)
    print(ALL_CLOSED)
    while True:
        userinput = int(input("Enter the door number"))
        if userinput in range(1,4):
            break
        elif userinput == 0:
            print("Thanks for playing")
            sys.exit()
        else:
            print("Enter valid input")
    
    if doorwithcar == 1 and userinput == 1:
        doorshown = random.choice([2,3])
        if doorshown == 2:
            print(SECOND_GOAT)
        else:
            print(THIRD_GOAT)
    elif doorwithcar == 2 and userinput == 1:
        doorshown = 3
        print(THIRD_GOAT)
    elif doorwithcar == 3 and userinput == 1:
        doorshown = 2
        print(SECOND_GOAT)
    elif doorwithcar == 2 and userinput == 2:
        doorshown = random.choice([1,3])
        if doorshown == 1:
            print(FIRST_GOAT)
        else:
            print(THIRD_GOAT)
    elif doorwithcar == 3 and userinput == 2:
        doorshown = 1
        print(FIRST_GOAT)
    elif doorwithcar == 1 and userinput == 2:
        doorshown = 3
        print(THIRD_GOAT)
    elif doorwithcar == 3 and userinput == 3:
        doorshown = random.choice([1,2])
        if doorshown == 1:
            print(FIRST_GOAT)
        else:
            print(SECOND_GOAT)
    elif doorwithcar == 2 and userinput == 3:
        doorshown = 1
        print(FIRST_GOAT)
    elif doorwithcar == 1 and userinput == 3:
        doorshown = 2
        print(SECOND_GOAT)
    
    swap = input("Do you want to swap ?")
    if (swap.upper() == 'Y'):
        if(userinput == 1 and doorshown == 2):
            userinput = 3
        elif(userinput == 1 and doorshown == 3):
            userinput = 2
        elif(userinput == 2 and doorshown == 1):
            userinput = 3
        elif(userinput == 2 and doorshown == 3):
            userinput = 1
        elif(userinput == 3 and doorshown == 1):
            userinput = 2
        elif(userinput == 3 and doorshown == 2):
            userinput = 1
        else:
            print("ERROR")

    #Door with ladder
    if(doorshown == 1):
        print(FIRST_CAR_OTHERS_GOAT)
    elif(doorshown == 2):
        print(SECOND_CAR_OTHERS_GOAT)
    else:
        print(THIRD_CAR_OTHERS_GOAT)

    
    #Scoring
    if(userinput == doorshown and swap.upper() == 'Y'):
        swapin += 1
        print("Congrats! You won")
    elif(userinput == doorshown and swap.upper() == 'N'):
        ogwin += 1
        print("Congrats! You won")
    elif(userinput != doorshown and swap.upper() == 'Y'):
        swaplose += 1
        print("Sorry! Better luck next time")
    else:
        oglose += 1
        print("Sorry! Better luck next time")

    print("""Thanks for playing!
    Wins after swapping: {}
    Wins without swapping: {}
    Losses after swapping: {}
    Losses without swapping: {}""".format(swapin, ogwin, swaplose, oglose))

    successRateSwap = 0
    successRateOg = 0

    try:
        successRateSwap = round((swapin/(swapin + swaplose))*100)
    except ZeroDivisionError:
        successRateSwap = 0
    try:
        successRateOg = round((ogwin/(ogwin + oglose))*100)
    except ZeroDivisionError:
        successRateOg = 0

    print("""Success Rate if you swap: {}
           Success Rate if you don't swap: {}""".format(successRateSwap, successRateOg))


    
    
        


    
