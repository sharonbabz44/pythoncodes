
command = ""
started=False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started=True
            print ("Car started, Ready to go!")
    elif command =="stop":
        print ("Relax, car has been stopped")
    elif command=="help":
        print ("""
start - to start the car
Stop - to stop the car
Quit- to exit
        """)
    elif command == "quit":
        break
    else:
        print ("I have no idea wht you want")

                


    



       
 
