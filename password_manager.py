from cryptography.fernet import Fernet
import os
import base64
import json

# Generate a key using a password
def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32)[:32].encode())

# Encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

# Decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message.encode()).decode()

# Save passwords to a file
def save_passwords(filename, passwords):
    with open(filename, 'w') as f:
        json.dump(passwords, f)

# Load passwords from a file
def load_passwords(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as f:
        return json.load(f)

# Add or update a password
def add_password(filename, key, service, password):
    passwords = load_passwords(filename)
    passwords[service] = encrypt_message(password, key)
    save_passwords(filename, passwords)

# Get a password
def get_password(filename, key, service):
    passwords = load_passwords(filename)
    if service in passwords:
        return decrypt_message(passwords[service], key)
    return None

# Delete a password
def delete_password(filename, service):
    passwords = load_passwords(filename)
    if service in passwords:
        del passwords[service]
        save_passwords(filename, passwords)

# Main program
def main():
    master_password = input("Enter the master password: ")
    key = generate_key(master_password)
    filename = 'passwords.json'

    while True:
        print("\n1. Add/Update Password\n2. Get Password\n3. Delete Password\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            add_password(filename, key, service, password)
            print(f"Password for {service} saved.")
        elif choice == '2':
            service = input("Enter the service name: ")
            password = get_password(filename, key, service)
            if password:
                print(f"Password for {service}: {password}")
            else:
                print(f"No password found for {service}.")
        elif choice == '3':
            service = input("Enter the service name: ")
            delete_password(filename, service)
            print(f"Password for {service} deleted.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
