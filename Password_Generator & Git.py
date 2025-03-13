import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint
import re

# Check if words.txt exists; if not, download it.
if not isfile("words.txt"):
    print('Downloading words.txt ...')
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    with open('words.txt', 'w') as f:
        f.write(urlopen(url).read().decode('utf-8'))

words = open('words.txt', 'r').read().splitlines()
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', '?', ',', '.', '/']

# Password creation function
def create_password(num_words=2, num_numbers=4, num_specials=1):
    pass_str = ''
    
    for _ in range(num_words):
        pass_str += choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str += str(randint(0, 9))
    for _ in range(num_specials):
        pass_str += choice(special_chars)
    return pass_str

# Password strength evaluator
def evaluate_strength(password):
    # Basic criteria for strength
    length_score = len(password) / 20  # Each character counts for 1/20th of the strength
    upper_case_score = len(re.findall(r'[A-Z]', password)) > 0  # At least one uppercase letter
    number_score = len(re.findall(r'[0-9]', password)) > 0  # At least one number
    special_char_score = len(re.findall(r'[\!@#\$%\^&\*\(\)_\+\=\{\}\[\]\\|:;\"\'<>,./?]', password)) > 0  # At least one special character
    
    # Assign scores based on the criteria
    strength = length_score + upper_case_score + number_score + special_char_score
    
    # Normalize strength to be between 0 and 1
    strength = min(strength, 1)
    return strength

# Function to generate password and test its strength
def generate_password():
    try:
        num_words = int(word_entry.get())
        num_numbers = int(number_entry.get())
        num_specials = int(special_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for words, numbers, and specials.")
        return

    pass_str = create_password(num_words, num_numbers, num_specials)
    strength = evaluate_strength(pass_str)
    
    password_label.config(text=f'Generated Password: {pass_str}')
    strength_label.config(text=f'Password Strength: {strength:.2f}')

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place labels, entries, and buttons
tk.Label(root, text="Number of Words:").grid(row=0, column=0, padx=10, pady=10)
word_entry = tk.Entry(root)
word_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Numbers:").grid(row=1, column=0, padx=10, pady=10)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Special Characters:").grid(row=2, column=0, padx=10, pady=10)
special_entry = tk.Entry(root)
special_entry.grid(row=2, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Labels to display the generated password and its strength
password_label = tk.Label(root, text="Generated Password: ")
password_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

strength_label = tk.Label(root, text="Password Strength: ")
strength_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
