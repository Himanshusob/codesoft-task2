import random
import string

def password_generator(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = password_generator(length)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()