from cryptography.fernet import Fernet
import secrets
import string


class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
        
        
    def create_key(self, path):
        self.key = Fernet.generate_key()
        try:
            with open(path, 'wb') as f:
                f.write(self.key)
        except IOError as e:
            print(f"Error writing key to file: {e}")
            
            
    def load_key(self, path):
        try:
            with open(path, 'rb') as f:
                self.key = f.read()
        except FileNotFoundError:
            print(f"Error: Key file not found at {path}")
        except IOError as e:
            print(f"Error reading key from file: {e}")
            
            
    def create_password_file(self, path):
        self.password_file = path
        # Removed initial_values logic
            
            
    def load_password_file(self, path):
        if self.key is None:
            print("Error: Key not loaded. Please load a key first.")
            return

        self.password_file = path 
        
        try:
            with open(path, 'r') as f:
                for line in f:
                    try:
                        site, encrypted_str = line.strip().split(":", 1)
                        self.password_dict[site] = encrypted_str # Store encrypted string
                    except Exception as e:
                        print(f"Error processing line: {line.strip()}. Details: {e}")
        except FileNotFoundError:
            print(f"Error: Password file not found at {path}")
        except IOError as e:
            print(f"Error reading password file: {e}")
                
                
    def add_password(self, site, password):
        if self.key is None:
            print("Error: Key not loaded. Please load or create a key first.")
            return

        # self.password_dict[site] = password # Old: storing plaintext
        
        if self.password_file is not None:
            try:
                with open(self.password_file, 'a+') as f:
                    encrypted_bytes = Fernet(self.key).encrypt(password.encode())
                    encrypted_str = encrypted_bytes.decode()
                    f.write(site + ":" + encrypted_str + "\n")
                    self.password_dict[site] = encrypted_str # New: storing encrypted string
            except IOError as e:
                print(f"Error writing to password file: {e}")
        else: # Handle case where password_file is None (e.g. not created/loaded yet)
             # Still encrypt and store in dict, but don't write to file
            try:
                encrypted_bytes = Fernet(self.key).encrypt(password.encode())
                encrypted_str = encrypted_bytes.decode()
                self.password_dict[site] = encrypted_str
            except Exception as e: # Catch potential encryption errors if key is bad, etc.
                print(f"Error encrypting password for {site} in memory. Details: {e}")
                
                
    def get_password(self, site):
        if self.key is None:
            print("Error: Key not loaded. Please load a key first.")
            return None

        encrypted_password_str = self.password_dict.get(site)

        if encrypted_password_str is None:
            print(f"Error: Password for '{site}' not found.")
            return None

        try:
            encrypted_password_bytes = encrypted_password_str.encode()
            decrypted_password_bytes = Fernet(self.key).decrypt(encrypted_password_bytes)
            decrypted_password_str = decrypted_password_bytes.decode()
            return decrypted_password_str
        except Exception as e:
            print(f"Error: Could not decrypt password for '{site}'. Details: {e}")
            return None
    
    def list_sites(self):
        return list(self.password_dict.keys())

    def delete_password(self, site):
        if site not in self.password_dict:
            print(f"Site '{site}' not found.")
            return False

        del self.password_dict[site]

        if self.password_file is not None:
            try:
                with open(self.password_file, 'r') as f:
                    lines = f.readlines()

                with open(self.password_file, 'w') as f:
                    for line in lines:
                        if not line.startswith(site + ":"):
                            f.write(line)
                print(f"Password for '{site}' deleted successfully.")
                return True
            except FileNotFoundError:
                # This case should ideally not happen if password_file is not None and site was in dict
                # from a loaded file, but as a safeguard:
                print(f"Site '{site}' removed from current session. Password file not found to update.")
                return True # Still true because it's removed from dict
            except IOError as e:
                print(f"Error writing to password file during deletion: {e}")
                # Password removed from dict, but file update failed.
                # Decide if this is True or False. For now, let's say True as dict is changed.
                # Or, potentially re-add to dict to maintain consistency?
                # For now, let's stick to: it's deleted from memory.
                print(f"Site '{site}' removed from current session, but an error occurred updating the password file.")
                return True
        else:
            print(f"Site '{site}' removed from current session. No password file set to update.")
            return True

    def generate_password(self, length=16):
        # Basic validation for length
        if not (8 <= length <= 128):
            print(f"Requested length {length} is invalid. Length must be between 8 and 128. Defaulting to 16.")
            length = 16

        alphabet = string.ascii_letters + string.digits + string.punctuation
        # Ensure alphabet is not empty if string.punctuation was empty for some reason (highly unlikely)
        if not alphabet:
            # Fallback if somehow all string constants are empty
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
    
    
def main():
    pm = PasswordManager()
    # password = {
    #     "email": "12345" ,
    #     "facebook": "facebookpassword" ,
    #     "youtube": "youtubepassword" ,
    #     "something": "myfavoutiepassword_123"
    # } # This dictionary is removed

    print("""What do you want to do?
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
""")


done = False


while not done:
    
    choice = input("Enter your choice: ")
    if choice == "1":
        path = input("Enter path: ")
        pm.create_key(path)
        
    elif choice == "2":
        path = input(" Enter path: ")
        pm.load_key(path)
        
    elif choice == "3":
        path = input("Enter path: ")
        pm.create_password_file(path)
        
    elif choice == "4":
        path = input("Enter path: ")
        pm.load_password_file(path)
        
    elif choice == "5":
        site = input("Enter the site: ")
        password = input("Enter the password: ")
        pm.add_password(site, password)
        
    elif choice == "6":
        site = input("What site do you want: ")
        print(f"password for {site} is {pm.get_password(site)}")

    elif choice == "7":
        sites = pm.list_sites()
        if sites:
            print("Stored sites:")
            for site_name in sites:
                print(f"- {site_name}")
        else:
            print("No sites stored yet.")

    elif choice == "8":
        site_to_delete = input("Enter the site name to delete: ")
        pm.delete_password(site_to_delete)

    elif choice == "9":
        try:
            length_str = input("Enter desired password length (default 16, min 8, max 128): ")
            length = int(length_str) if length_str else 16
            # generate_password method also validates, but good to have it here for immediate feedback
            if not (8 <= length <= 128):
                print("Invalid length provided. Using length 16.")
                length = 16
        except ValueError:
            print("Invalid input for length. Using default length 16.")
            length = 16

        new_password = pm.generate_password(length=length)
        print(f"Generated password: {new_password}")

        save_choice = input("Do you want to save this password? (y/n): ").lower()
        if save_choice == 'y':
            site_name = input("Enter the site name: ")
            if not site_name:
                print("Site name cannot be empty. Password not saved.")
            else:
                pm.add_password(site_name, new_password) # add_password handles key check and prints status
        else:
            print("Password not saved.")
        
    elif choice == "q":
        done = True
        print("Goodbye! See you later!")
        
    else:
        print("Invalid input!!!!")
        
        
if __name__ == "__main__":
    main()
        
