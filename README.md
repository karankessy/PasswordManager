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
- List all sites
- Delete a password
- Generate a new password
- Quit

## Key Management
- The script uses the Fernet symmetric encryption scheme from the cryptography library.
- You can generate a new key or load an existing key to encrypt and decrypt passwords.

## Password File
- Passwords are stored in a plaintext file with the site name and encrypted password separated by a colon.
- You can create a new password file or load an existing one.

## Security Note
- Ensure the security of your key file. Losing the key will result in losing access to all stored passwords.
- Use strong, unique passwords for each site to enhance security. The script also offers a feature to generate strong random passwords for you.
- Do not share your password file or key with anyone.

## Example Usage
    What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create a new password file
    (4) Load an existing password file
    (5) Add a new password
    (6) Get a password
    (7) List all sites
    (8) Delete a password
    (9) Generate a new password
    (q) Quit
    
    Enter your choice: 1
    Enter path: key.key
    
    Enter your choice: 3
    Enter path: passwords.txt
    
    Enter your choice: 5
    Enter the site: email
    Enter the password: mysecretemailpassword
    Password for email added.

    Enter your choice: 6
    What site do you want: email
    Password for email is mysecretemailpassword

    Enter your choice: 9
    Enter desired password length (default 16, min 8, max 128):
    Generated password: YourStrongGeneratedPassword!123
    Do you want to save this password? (y/n): y
    Enter the site name: new_secure_service
    Password for new_secure_service added.

    Enter your choice: 7
    Stored sites:
    - email
    - new_secure_service
    
    Enter your choice: q
    Goodbye! See you later!
