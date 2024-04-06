## PasswordManager
## Introduction
This Python script serves as a basic password manager using the cryptography library. It allows users to generate and manage passwords securely.

## Installation
Ensure you have Python 3 installed on your system. Install the cryptography library using pip:

    pip install cryptography

### Usage
1. Run the script using Python 3:

       python3 password_manager.py

Follow the menu prompts to perform various actions:

- Create a new key
- Load an existing key
- Create a new password file
- Load an existing password file
- Add a new password
- Get a password
- Quit

## Key Management
- The script uses the Fernet symmetric encryption scheme from the cryptography library.
- You can generate a new key or load an existing key to encrypt and decrypt passwords.

## Password File
- Passwords are stored in a plaintext file with the site name and encrypted password separated by a colon.
- You can create a new password file with initial values or load an existing one.

## Securit Note
- Ensure the security of your key file. Losing the key will result in losing access to all stored passwords.
- Use strong, unique passwords for each site to enhance security.
- Do not share your password file or key with anyone.

## Example Usage
    What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create a new password file
    (4) Load an existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    
    Enter your choice: 1
    Enter path: key.key
    
    Enter your choice: 3
    Enter path: passwords.txt
    
    Enter your choice: 6
    What site do you want: email
    Password for email is b'12345'
    
    Enter your choice: q
    Goodbye! See you later!

