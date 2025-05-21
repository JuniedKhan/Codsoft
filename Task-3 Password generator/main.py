import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
from tkinter.font import Font

class FriendlyPasswordGenerator:
    def __init__(self, root):  # Fixed __init__
        self.root = root
        self.root.title("Friendly Password Creator")
        self.root.state('zoomed')  # Fullscreen window
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f9ff")
        
        # Custom fonts
        self.title_font = Font(family="Verdana", size=14, weight="bold")
        self.label_font = Font(family="Verdana", size=10)
        self.button_font = Font(family="Verdana", size=10)
        self.password_font = Font(family="Courier", size=12)
        
        # Colors
        self.bg_color = "#f5f9ff"
        self.button_color = "#4a90e2"
        self.highlight_color = "#e6f2ff"
        
        self.create_widgets()
        self.add_friendly_tips()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        header = tk.Label(main_frame,
                          text="Let's create a strong password for you!",
                          font=self.title_font,
                          bg=self.bg_color,
                          fg="#2c3e50")
        header.pack(pady=(0, 15))

        # Password length
        length_frame = tk.Frame(main_frame, bg=self.bg_color)
        length_frame.pack(fill=tk.X, pady=5)

        tk.Label(length_frame,
                 text="How long should your password be?",
                 font=self.label_font,
                 bg=self.bg_color).pack(anchor=tk.W)

        self.length_var = tk.IntVar(value=12)
        self.length_slider = ttk.Scale(length_frame,
                                       from_=8, to=32,
                                       variable=self.length_var,
                                       command=lambda e: self.update_length_label())
        self.length_slider.pack(fill=tk.X, pady=5)

        self.length_label = tk.Label(length_frame,
                                     text="12 characters",
                                     font=self.label_font,
                                     bg=self.bg_color)
        self.length_label.pack(anchor=tk.W)

        # Character types
        types_frame = tk.Frame(main_frame, bg=self.bg_color)
        types_frame.pack(fill=tk.X, pady=10)

        tk.Label(types_frame,
                 text="What should it include?",
                 font=self.label_font,
                 bg=self.bg_color).pack(anchor=tk.W)

        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        self.create_checkbox(types_frame, "Lowercase letters (abc)", self.lower_var)
        self.create_checkbox(types_frame, "Uppercase letters (ABC)", self.upper_var)
        self.create_checkbox(types_frame, "Numbers (123)", self.digits_var)
        self.create_checkbox(types_frame, "Special characters (!@#)", self.symbols_var)

        generate_btn = tk.Button(main_frame,
                                 text="Create My Password",
                                 font=self.button_font,
                                 bg=self.button_color,
                                 fg="white",
                                 relief=tk.FLAT,
                                 padx=20,
                                 pady=8,
                                 command=self.generate_password)
        generate_btn.pack(pady=15)

        password_frame = tk.Frame(main_frame, bg=self.highlight_color, padx=10, pady=10)
        password_frame.pack(fill=tk.X, pady=5)

        tk.Label(password_frame,
                 text="Your new password:",
                 font=self.label_font,
                 bg=self.highlight_color).pack(anchor=tk.W)

        self.password_var = tk.StringVar()
        password_entry = tk.Entry(password_frame,
                                  textvariable=self.password_var,
                                  font=self.password_font,
                                  bd=0,
                                  relief=tk.FLAT,
                                  state='readonly',
                                  readonlybackground=self.highlight_color)
        password_entry.pack(fill=tk.X, pady=5)

        copy_btn = tk.Button(main_frame,
                             text="Copy to Clipboard",
                             font=self.button_font,
                             bg="#e0e0e0",
                             relief=tk.FLAT,
                             command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)

    def create_checkbox(self, parent, text, variable):
        cb = tk.Checkbutton(parent,
                            text=text,
                            font=self.label_font,
                            bg=self.bg_color,
                            variable=variable,
                            anchor=tk.W)
        cb.pack(fill=tk.X, pady=2)

    def add_friendly_tips(self):
        tips_frame = tk.Frame(self.root, bg="#e6f2ff", padx=15, pady=10)
        tips_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

        tk.Label(tips_frame,
                 text="💡 Tips: Longer passwords with mixed characters are more secure!",
                 font=Font(family="Verdana", size=9),
                 bg="#e6f2ff",
                 fg="#2c3e50").pack(anchor=tk.W)

    def update_length_label(self):
        length = int(self.length_var.get())
        self.length_label.config(text=f"{length} character{'s' if length != 1 else ''}")

    def generate_password(self):
        if not any([self.lower_var.get(), self.upper_var.get(),
                    self.digits_var.get(), self.symbols_var.get()]):
            messagebox.showwarning("Oops!", "Please select at least one type of character to include in your password.")
            return

        char_sets = []
        if self.lower_var.get():
            char_sets.append(string.ascii_lowercase)
        if self.upper_var.get():
            char_sets.append(string.ascii_uppercase)
        if self.digits_var.get():
            char_sets.append(string.digits)
        if self.symbols_var.get():
            char_sets.append(string.punctuation)

        all_chars = ''.join(char_sets)
        length = int(self.length_var.get())

        password = [random.choice(char_set) for char_set in char_sets]
        password += [random.choice(all_chars) for _ in range(length - len(password))]
        random.shuffle(password)
        self.password_var.set(''.join(password))

        messagebox.showinfo("Success!", "Your new password has been created!\n\nRemember to store it somewhere safe.")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied!", "Your password has been copied to the clipboard.\n\nYou can now paste it where needed!")
        else:
            messagebox.showwarning("Nothing to Copy", "Please generate a password first.")

if __name__ == "__main__":  # Fixed main guard
    root = tk.Tk()
    app = FriendlyPasswordGenerator(root)
    root.mainloop()
