import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, use_letters, use_numbers, use_symbols, exclude_chars):
    # Define character pools based on user preferences
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_numbers:
        characters += string.digits         # Includes numbers 0-9
    if use_symbols:
        characters += string.punctuation    # Includes special characters like !, @, #, etc.

    # Exclude specified characters
    characters = ''.join(c for c in characters if c not in exclude_chars)

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type or adjust exclusions.")
        return None

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        exclude_chars = exclude_entry.get()

        # Ensure that length is a positive integer
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        # Generate the password and display it
        password = generate_password(length, use_letters, use_numbers, use_symbols, exclude_chars)
        if password:
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the GUI window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")

# Length input
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Character type options
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor="w")
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor="w")
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w")

# Exclude specific characters
tk.Label(root, text="Exclude Characters:").pack(pady=5)
exclude_entry = tk.Entry(root)
exclude_entry.pack(pady=5)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack(pady=10)

# Display generated password
tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, width=30, font=("Arial", 14), justify="center")
password_entry.pack(pady=5)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the GUI application
root.mainloop()
