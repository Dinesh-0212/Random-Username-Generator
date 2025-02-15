import random
import string

def generate_username(include_numbers=True, include_special_chars=True, length=10):
    adjectives = ["Cool", "Happy", "Brave", "Clever", "Witty", "Chill", "Funky", "Lively", "Mighty", "Swift"]
    nouns = ["Tiger", "Dragon", "Eagle", "Ninja", "Pirate", "Wizard", "Knight", "Shadow", "Falcon", "Panther"]
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    if include_numbers:
        username += str(random.randint(10, 99))
    if include_special_chars:
        username += random.choice("!@#$%^&*")
    return username[:length]

def save_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")
    print(f"Username '{username}' saved to {filename}.")

print("Welcome to the Random Username Generator!")
num_usernames =5
include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
length = int(input("Enter max username length: "))
usernames = []
for _ in range(num_usernames):
    username = generate_username(include_numbers, include_special_chars, length)
    usernames.append(username)
    print("Generated Username:", username)
save_option = input("Save usernames to file? (y/n): ").strip().lower()
if save_option == 'y':
    for username in usernames:
        save_to_file(username)
