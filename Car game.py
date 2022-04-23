
#Car_Game
name= input('Please Write your name: ')
a = print(f'''Hi {name}, Welcome to the Car Game. Please select any of the option below:
start
stop
exit''')

command = ""
while True :
    command = input(">").lower()
    if command == "start":
        print("Car started, Ready to Go! ")
    elif command == "stop":
        print("car stopped.")
    elif command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        exit - to exit the game
        ''')
    elif command == "exit":
        break
    else:
        print("Command not recognised")
