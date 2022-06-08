import random

input("Welcome to Rock, Paper, Scissors!!! \n" 
                                +"Winning Rules of the Game: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n"
                                +" Press Enter to start.")
                                

user_score = 0
cpu_score = 0


while True:
    print()
    user_input = input("Enter a choice: 'R' for Rock, 'P' for Paper or 'S'  for Scissors: ").lower()
    possible_actions = ['s', 'p', 's']

    while user_input != "r" and user_input != "p" and user_input != "s":
            user_choice= input("Invalid input please try again: ")

    # declaration for showing exact choice of user
    if user_input == 'r':
        user_choice = "rock"
    elif user_input == 'p':
        user_choice = "paper"
    elif user_input == 's':
        user_choice = "scissors"
    

    

    # Declaration of computer
    comp_random_pick = random.choice(possible_actions)
    if comp_random_pick == 'r':
        cpu_choice = "rock"
    elif comp_random_pick == 'p':
        cpu_choice = "paper"
    elif comp_random_pick == 's':
        cpu_choice = "scissors"

    print()
    print("your choice:", user_choice)
    print("Computer's Choice:", cpu_choice)
    print()

    if user_choice == "rock":
        if cpu_choice == "rock":
            print("you both chose rock ==> Its a tie! Play again")
        elif cpu_choice == "paper":
            print("Paper beats rock ==> You lost!")
            cpu_score += 1
        elif cpu_choice == "scissors":
            print("Rock beats scissors ==> You win!")
            user_score += 1


    elif user_choice == "paper":
        if cpu_choice == "paper":
            print("You both chose paper ==> Its a tie! Play again")
        elif cpu_choice == "scissors":
            print("Scissors beats paper ==> You lost!")
            cpu_score += 1
        elif cpu_choice == "rock":
            print("paper beats rock ==> You win!")
            user_score += 1

    elif user_choice == "scissors":
        if cpu_choice == "scissors":
            print("You both chose sciossrs ==> Its a tie! Play again")
        elif cpu_choice == "rock":
            print("Rock beats scissors You lost ==> You lost!")
            cpu_score += 1
        elif cpu_choice == "paper":
            print("Scissors beats paper ==> You win!")
            user_score += 1

    print("You have", user_score, "wins")
    print("The computer has", cpu_score, "wins")
    print()

    repeat = input("Play again (Y/N) ").lower()
    while repeat != "n" and repeat != "y":
        repeat = input("invalid input please try again ").lower()

    if repeat == "n":
        break