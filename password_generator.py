import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generates a secure random password.

    :param length: Length of the password (default is 12)
    :param use_uppercase: Include uppercase letters (default is True)
    :param use_digits: Include digits (default is True)
    :param use_special_chars: Include special characters (default is True)
    :return: A secure random password
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define character pools
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Ensure at least one character from each selected pool is included
    pools = [lower_chars]
    if use_uppercase:
        pools.append(upper_chars)
    if use_digits:
        pools.append(digit_chars)
    if use_special_chars:
        pools.append(special_chars)

    if not any(pools):
        raise ValueError("At least one character type must be selected.")

    # Build the password
    all_chars = ''.join(pools)
    password = [random.choice(pool) for pool in pools]  # Ensure one from each selected pool
    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)  # Shuffle to randomize order

    return ''.join(password)


# Create the main window
window = tk.Tk()
window.title("Secure Password Generator")

# Set window size
window.geometry("400x300")

# Create and pack the UI components
tk.Label(window, text="Enter password length (minimum 4):").pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

tk.Label(window, text="Include uppercase letters?").pack(pady=5)
uppercase_var = tk.BooleanVar()
tk.Checkbutton(window, text="Yes", variable=uppercase_var).pack(pady=5)

tk.Label(window, text="Include digits?").pack(pady=5)
digits_var = tk.BooleanVar()
tk.Checkbutton(window, text="Yes", variable=digits_var).pack(pady=5)

tk.Label(window, text="Include special characters?").pack(pady=5)
special_chars_var = tk.BooleanVar()
tk.Checkbutton(window, text="Yes", variable=special_chars_var).pack(pady=5)

# Function to handle password generation
def on_generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError("Password length must be at least 4 characters.")

        password = generate_password(
            length=length,
            use_uppercase=uppercase_var.get(),
            use_digits=digits_var.get(),
            use_special_chars=special_chars_var.get()
        )
        messagebox.showinfo("Generated Password", f"Your secure password is: {password}")

    except ValueError as e:
        messagebox.showerror("Error", f"Error: {e}")

# Create and pack the "Generate Password" button
generate_button = tk.Button(window, text="Generate Password", command=on_generate_password)
generate_button.pack(pady=20)

# Run the main event loop
window.mainloop()
