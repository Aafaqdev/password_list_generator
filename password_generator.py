import itertools

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
            print(f"Generating passwords: {completed_combinations} out of {total_combinations} completed", end='\r')

    print("\nAll combinations generated.")
    return passwords

def main():
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

if __name__ == "__main__":
    main()
