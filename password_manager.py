import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def load_key():
    file = open("key.key", "r")
    key = file.read()
    file.close()
    return key.encode()

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashlib.sha256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# write_key() # This is done only once, else each time u have a key that would be different.

master_pwd = input("What is the master password? ")
salt = load_key()  # Using the saved key as salt for KDF
key = derive_key(master_pwd, salt)
fer = Fernet(key)

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            un, pwd = line.rstrip().split("|")
            print(f"Username: {un}, Password: {fer.decrypt(pwd.encode()).decode()}")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("would you like to add a new password or view existing ones? (v for view, e for edit), press q to quit ")
    if mode == "q":
        break

    if mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        print("Invalid option. ")
        