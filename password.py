# import random
# import string

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# def save_password_to_file(password, filename):
#     with open(filename, 'w') as file:
#         file.write(password)

# def main():
#     password_length = int(input("\n Enter the desired password length: "))
#     password = generate_password(password_length)
#     print("Generated Password:", password)

#     save_to_file = input("Do you want to save this password to a file? (y/n): ").lower() == 'y'
#     if save_to_file:
#         filename = input("Enter the filename to save the password: ")
#         save_password_to_file(password, filename)
#         print(f"Password saved to '{filename}'.")

# if __name__ == "__main__":
#     main()

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename):
    with open(filename, 'a') as file:
        file.write({password})

def main():
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)


    save_to_file = input("Do you want to save this password to a file? (y/n): ").lower() == 'y'
    if save_to_file:
        filename = input("Enter the filename to save the password: ")
        save_password_to_file(password, filename)
        print(f"Password saved to '{filename}'.")

if __name__ == "__main__":
    main()

