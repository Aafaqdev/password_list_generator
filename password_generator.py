import itertools
import sys

def generate_passwords(characters, min_length, max_length):
    passwords = []
    total_combinations = 0
    for length in range(min_length, max_length + 1):
        total_combinations += len(characters) ** length

    completed_combinations = 0
    for length in range(min_length, max_length + 1):
        for combo in itertools.product(characters, repeat=length):
            password = ''.join(combo)
            passwords.append(password)
            completed_combinations += 1
            print(f"\033[1;32;40mGenerating passwords: {completed_combinations} out of {total_combinations} completed\033[0m", end='\r')

    print("\n\033[1;35;40mAll combinations generated.\033[0m")
    return passwords

def print_stylish_message(message):
    print(f"\033[1;31;40m{message}\033[0m")

def display_menu():
    print_stylish_message("""
   _____       _                 _      _             
  / ____|     | |               | |    (_)            
 | |  __ _   _| |_ _ __ __ _  __| | ___ _ _ __   __ _ 
 | | |_ | | | | __| '__/ _` |/ _` |/ _ \ | '_ \ / _` |
 | |__| | |_| | |_| | | (_| | (_| |  __/ | | | | (_| |
  \_____|\__,_|\__|_|  \__,_|\__,_|\___|_|_| |_|\__, |
                                                  __/ |
                                                 |___/ 
    """)

    print("\033[1;31;40m1. \033[0mRandom Password Generator")
    print("\033[1;31;40m2. \033[0mFollow us on Github")
    print("\033[1;31;40m3. \033[0mExit the tool")

def main():
    display_menu()

    while True:
        choice = input("\033[1;31;40m\nEnter your choice: \033[0m")

        if choice == '1':
            alphabets = input("Enter alphabets: ")
            numbers = input("Enter numbers: ")
            special_characters = input("Enter special characters: ")
            min_length = int(input("Enter minimum length of password: "))
            max_length = int(input("Enter maximum length of password: "))
            file_name = input("Enter the file name to save passwords: ")

            characters = alphabets + numbers + special_characters

            passwords = generate_passwords(characters, min_length, max_length)

            with open(file_name, 'w') as file:
                for password in passwords:
                    file.write(password + '\n')

            print(f"{len(passwords)} passwords have been generated and saved to {file_name}.")
            display_menu()

        elif choice == '2':
            print("Follow us on GitHub: [link]")  # Replace [link] with your GitHub repository link
            display_menu()

        elif choice == '3':
            print("Exiting the tool. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please select a valid option.")
            display_menu()

if __name__ == "__main__":
    main()
