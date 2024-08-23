def start_game():

    user_input = input("Do you want to start the game? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        print("Initialization Complete")
    else:
        print("Initialization Failed")

start_game()