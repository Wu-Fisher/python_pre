# car game 
from tracemalloc import start


command=""
started=False
while True:
    command=input(">").lower()
    if command=="start":
        if started:
            print("Car is already start ")
        else:
            started= True
            print("Car started..")
    elif command=="stop":
        if started:
            print("Car stopped")
            started=False
        else:
            print("Car is not running")
    elif command=="help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command=="quit":
        break
    else :
        print("Sorry i dont understand")

