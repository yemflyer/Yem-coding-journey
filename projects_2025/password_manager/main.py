"""
✅ Step 1: Setup your project
Create a folder called password_manager/
Inside, create two files:

main.py – where your Python code will go

secret.key – this will be created by the code to store your encryption key

We’ll also use the cryptography library to encrypt/decrypt passwords:

Open terminal and run:

bash
Copy
Edit
pip install cryptography
"""

#Step2: Create a function to generate and save an encryption key
#Generate & save an encryption key

from cryptography.fernet import Fernet 

# This function creqtes qnd sqves qn ecryption key only ONCE
def generate_key():
    """Generate and save a key for encryption/decryption."""
    # Check if the key file already exists
    with open("secret.key", "wb") as key_file:
        key_file.write(Fernet.generate_key()) # Generate a key and write it to a file

def load_key():
    return open("secret.key", "rb").read() # Load the key from the file

generate_key() # Generate the key and save it to a file

#Step3:  Encrypting and Decrypting Passwords

key = load_key() # Load the key from the file
cipher =Fernet(key) # Create a Fernet cipher object using the key

def encrypt_password(password):
    """Encrypt the password using the Fernet cipher."""
    return cipher.encrypt(password.encode()) # Encrypt the password and return it

def decrypt_password(encrypted_password):
    """Decrypt the password using the Fernet cipher."""
    return cipher.decrypt(encrypted_password).decode() # Decrypt the password and return it as a string

"""🧠 Learning Tip: Play with these functions in a test file. Try encrypting your name or a fake password."""

#Step4: Create the GUI with Tkinter
import tkinter as tk
from tkinter import messagebox

#lets build the input fields.
root = tk.Tk()  # Create the main window
root.title("Password Manager")  # Set the title of the window

tk.Label(root, text ="Website:").grid(row=0, column=0)  # Label for website input
website_entry = tk.Entry(root, width=35) # Entry field for website
website_entry.grid(row=0, column=1, columnspan=2)   # Span two columns for the entry field

tk.Label(root, text="Username/Email:").grid(row=1, column=0)    # Label for username input
username_entry = tk.Entry(root, width=35)       # Entry field for username
username_entry.grid(row=1, column=1, columnspan=2)  # Span two columns for the entry field  

tk.Label(root, text="Password:").grid(row=2, column=0)  # Label for password input
password_entry = tk.Entry(root, width=21)       # Entry field for password
password_entry.grid(row=2, column=1)    # Entry field for password                      


#Step5: Saving data securely

def save_password():
    """Save the password to a file."""
    website = website_entry.get()  # Get the website from the entry field
    username = username_entry.get()  # Get the username from the entry field
    password = password_entry.get()  # Get the password from the entry field

    if not website or not username or not password:  # Check if any field is empty
        messagebox.showwarning("Please fill in all fields.")  # Show a warning message
        return  # If any field is empty, show a warning message
    
    encrypted_pw = encrypt_password(password)  # Encrypt the password

    with open("data.txt", "a") as file:
        file.write(f"{website} | {username} | {encrypted_pw.decode()}\n")
        # Write the website, username, and encrypted password to a file

    # Clear the entry fields after saving
    website_entry.delete(0, tk.END)  # Clear the website entry field
    username_entry.delete(0, tk.END)  # Clear the username entry field  
    password_entry.delete(0, tk.END)  # Clear the password entry field

    messagebox.showinfo("Success", "Password saved successfully!")  # Show a success message

    """🧠 Learn idea: open data.txt and see how the encrypted data looks!"""

    # Step 6: Retrieving saved passwords
    def search_password():
        """Search for a password by website."""
        website = website_entry.get()
        found = False # Flag to check if the website is found

        try:
            with open("data.txt", "r") as file:
                for line in file.readlines():
                    w, u, p  =line.strip().split(" | ") # Split the line into website, username, and password
                    if w == website:
                        decrypted_pw = decrypt_password(p.endcode()) # Decrypt the password
                        messagebox.showinfo("Password Found", f"Username: {u}\nPassword: {decrypted_pw}")
                        found = True
                        break
            if not found:
                messagebox.showinfo("Not found","No credentials found for this website.")
        
        except FileNotFoundError:
            messagebox.showerror("Error", "No data file found. Please save a password first.")
            # Show an error message if the data file is not found

    
    #Step 7: Create buttons for saving and searching passwords
    tk.Button(root, text = "Save Password", command=save_password).grid(row=3, column=1)  # Button to save the password
    tk.Button(root, text = "Search Password", command=search_password).grid(row=3, column=2)  # Button to search for a password

    root.mainloop()  # Start the Tkinter main loop to run the GUI

    """"
    ✅ Final Structure to Try Yourself
I suggest you try building it in this order:

Generate and load the key.

Build encryption and decryption functions.

Create a simple GUI with one input and a save button.

Add save and search logic step-by-step.

Test after each feature you add.

🚀 Ready to Try It Yourself?
You can:

Add a password generator button

Add master password protection

Export your saved data securely

Turn this into a .exe using pyinstaller
"""