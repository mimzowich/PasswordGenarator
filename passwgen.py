import random
import string
import tkinter as tk
from tkinter import ttk

# Original password generator function
def generate_password(length=8, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    character_pool = ""
    if use_upper:
        character_pool += upper_chars
    if use_lower:
        character_pool += lower_chars
    if use_digits:
        character_pool += digit_chars
    if use_symbols:
        character_pool += symbol_chars

    if not character_pool:
        return "Invalid options"

    return ''.join(random.choice(character_pool) for _ in range(length))

# GUI Application
class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x300")

        # Widgets
        self.label_length = ttk.Label(self, text="Password Length:")
        self.label_length.pack(pady=10)

        self.entry_length = ttk.Entry(self)
        self.entry_length.pack(pady=10)

        self.var_upper = tk.BooleanVar()
        self.check_upper = ttk.Checkbutton(self, text="Include Uppercase", variable=self.var_upper)
        self.check_upper.pack(pady=5)

        self.var_lower = tk.BooleanVar()
        self.check_lower = ttk.Checkbutton(self, text="Include Lowercase", variable=self.var_lower)
        self.check_lower.pack(pady=5)

        self.var_digits = tk.BooleanVar()
        self.check_digits = ttk.Checkbutton(self, text="Include Digits", variable=self.var_digits)
        self.check_digits.pack(pady=5)

        self.var_symbols = tk.BooleanVar()
        self.check_symbols = ttk.Checkbutton(self, text="Include Symbols", variable=self.var_symbols)
        self.check_symbols.pack(pady=5)

        self.button_generate = ttk.Button(self, text="Generate Password", command=self.generate)
        self.button_generate.pack(pady=20)

        self.label_result = ttk.Label(self, text="Generated Password:")
        self.label_result.pack(pady=10)

        self.entry_result = ttk.Entry(self)
        self.entry_result.pack(pady=10)

    def generate(self):
        length = int(self.entry_length.get())
        password = generate_password(length, self.var_upper.get(), self.var_lower.get(), self.var_digits.get(), self.var_symbols.get())
        self.entry_result.delete(0, tk.END)
        self.entry_result.insert(0, password)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
