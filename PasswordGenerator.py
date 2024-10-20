import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase5
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate and display the password
    password = generate_password(length)
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
