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
website_entry = ttk.Entry(frm, width=35)  # Use ttk.Entry for consistency
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
