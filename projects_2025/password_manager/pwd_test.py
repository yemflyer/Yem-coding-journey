from cryptography.fernet import Fernet

def generate_key():
    with open("secret.key", "wb") as key_file: 
        key_file.write(Fernet.generate_key())

def load_key():
    """Load the encryption key from file."""
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Generate key (only need to run this once)
# generate_key()  # Uncomment if you haven't generated a key yet


#📌 *Goal: Learn to generate and load an encryption key.*

# Load the key and create cipher suite
key = load_key()
cipher = Fernet(key)


def encrypt_password(password):
    """Encrypt a password string."""
    return cipher.encrypt(password.encode())  # String -> Bytes -> Encrypted Bytes

def decrypt_password(encrypted_password):
    """Decrypt encrypted data back to string."""
    return cipher.decrypt(encrypted_password).decode()

"""
Key Security Principle: why is .decode() out of the parenteses?
Never try to decode encrypted data - it's not text, it's binary data

Only decode after proper decryption when you know you have valid UTF-8 bytes
"""


"""
#How to run test code:
# Test the functions
if __name__ == "__main__":
    test_password = "blackclover$2025"  # Test password
    
    print("\n=== Testing Encryption/Decryption ===")
    
    # 1. Encrypt
    encrypted = encrypt_password(test_password)
    print(f"\nOriginal Password: {test_password}")
    print(f"Encrypted Password (bytes): {encrypted}")
    print(f"Encrypted Password (hex): {encrypted.hex()}")
    
    # 2. Decrypt
    decrypted = decrypt_password(encrypted)
    print(f"\nDecrypted Password: {decrypted}")
    
    # 3. Verify
    print("\n=== Test Result ===")
    if decrypted == test_password:
        print("✅ Success! Decrypted password matches original.")
    else:
        print("❌ Failure! Decrypted password doesn't match.")   
    
📌 *Goal: Practice secure encryption/decryption of strings.*
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Must import ttk explicitly

root = tk.Tk()
root.title("Password Manager")

# Create a frame with padding
frm = ttk.Frame(root, padding=10)
frm.grid()

# Website
ttk.Label(frm, text="Website:").grid(row=0, column=0)  # Fixed typo (ttK → ttk)
website_entry = ttk.Entry(frm, width=35)  # website_entry is a textbox in our gui
website_entry.grid(row=0, column=1, columnspan=2)

# Username
ttk.Label(frm, text="Username/Email:").grid(row=1, column=0)
username_entry = ttk.Entry(frm, width=35)  # Fixed: gridded to frm (not root)
username_entry.grid(row=1, column=1, columnspan=2)

# Password
ttk.Label(frm, text="Password:").grid(row=2, column=0)
password_entry = ttk.Entry(frm, width=21, show="*")  # Added show="*" to hide password
password_entry.grid(row=2, column=1)

root.mainloop()  # Start the Tkinter event loop

               #📌 *Goal: Build a simple GUI form using Tkinter.*



               ## 💾 Section 5: Save Passwords Securely
 
import os
from tkinter import messagebox
import tkinter as tk

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Error", "Please fill in all fields.")  # Added title
        return

    encrypted_pw = encrypt_password(password)  # Ensure this function exists!
    
    # Debug: Print file path
    file_path = os.path.join(os.getcwd(), "data.txt")
    print("Saving to:", file_path)  # Check where the file is being saved

    with open("data.txt", "a") as file:
        file.write(f"{website} | {username} | {encrypted_pw.decode()}\n")

    # Clear fields
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    messagebox.showinfo("Saved", "Password saved successfully!")
## 🔍 Section 6: Search for Saved Passwords

  def search_password():
        website = website_entry.get()
        found = False # Flag to check if the website is found

        try:
            with open("data.txt", "r") as file:
                for line in file.readlines():
                    w, u, p = line.strip().split(" | ")
                    if w == website:
                        decrypted_pw = decrypt_password(p.encode()) # Decrypt the password
                        messagebox.showinfo("Password Found", f"Username: {u}\nPassword: {decrypted_pw}")
                        found = True
                        break
            if not found:
                messagebox.showinfo("Error", "No credentials  for the website exists.")
        except FileNotFoundError:
            messagebox.showwarning("Error", "No data file found. Please save a password first.")

# Add a "Search" button to run `search_password()`

tk.Button(root, text="Save Password", command=save_password).grid(row=3, column=1)  # Button to save the password
tk.Button(root, text="Search Password", command=search_password).grid(row=3, column=2) # Button to search for a password

root.mainloop()  # Start the Tkinter main loop to run the GUI

#📌 *Goal: Implement a search function to retrieve saved passwords.
# *
## 🧼 Section 7: Polish and Test


## 🎓 Bonus Learning Challenges (Optional)