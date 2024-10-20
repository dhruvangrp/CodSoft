import random

def print_welcome():
    print("Welcome to Rock, Paper, Scissors!")
    print("================================")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("Let's begin!\n")

def get_user_choice():
    print("Your turn:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return ['rock', 'paper', 'scissors'][int(choice) - 1]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    result = determine_winner(user_choice, computer_choice)
    print(f"\nResult: {result}")

def play_again():
    while True:
        choice = input("\nDo you want to play another game? (yes/no): ").lower()
        if choice in ['yes', 'no', 'y', 'n']:
            return choice in ['yes', 'y']
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    print_welcome()
    while True:
        play_game()
        if not play_again():
            break
    print("\nThanks for playing!")
