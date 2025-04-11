 #Step 5: Saving data securely
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