from tkinter import *
from tkinter import ttk
import pyperclip
from modules.pass_generator import generate_password
from modules.json_saver import pass_saver
from modules.json_finder import pass_finder

FONT_NAME = "Helvetica"
FONT_STYLE = (FONT_NAME, 28, "bold")


class ManagerInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
        lock_img = PhotoImage(file="./images/logo.png")
        canvas = Canvas(width=200, height=200, highlightthickness=0)
        canvas.create_image(100, 100, image=lock_img)
        self.r_text = canvas.create_text(100, 160, text="Password\nManager", fill="black", font=(FONT_NAME, 14, "bold"))

        # Labels
        website_label = ttk.Label(text="Website/Service: ")
        email_label = ttk.Label(text="Email: ")
        username_label = ttk.Label(text="Username: ")
        password_label = ttk.Label(text="Password: ")
        gen_password_label = ttk.Label(text="Generated Password: ")
        underline_label = ttk.Label(text="")
        underline_label_2 = ttk.Label(text="")

        # Entries
        self.website_entry = ttk.Entry(width=32)
        self.website_entry.focus()
        self.email_entry = ttk.Entry(width=32)
        self.user_name_entry = ttk.Entry(width=32)
        self.password_entry = ttk.Entry(width=32)
        self.gen_password_entry = ttk.Entry(width=32)

        # Buttons
        search_button = ttk.Button(width=8, text="Search", command=self.find_pass_func)
        add_button = ttk.Button(width=42, text="Add to DataBase", command=self.save_pass_func)
        gen_pass_cpy_button = ttk.Button(width=8, text="☚ Copy", command=self.copy_gen_password_func)
        gen_pass_button = ttk.Button(width=42, text="Generate Password", command=self.gen_pass_func)
        read_db_button = ttk.Button(width=42, text="Read Local DataBase")
        connect_to_db_button = ttk.Button(width=42, text="Connect to Web DataBase")

        # # Grids (placeholder of elements)
        canvas.grid(column=1, row=0)

        # Label Grids
        website_label.grid(column=0, row=1)
        email_label.grid(column=0, row=2)
        username_label.grid(column=0, row=3)
        password_label.grid(column=0, row=4)
        underline_label.grid(column=0, row=5)
        underline_label_2.grid(column=0, row=7)
        gen_password_label.grid(column=0, row=8)

        # Entry Grids
        self.website_entry.grid(column=1, row=1)
        self.email_entry.grid(column=1, row=2)
        self.user_name_entry.grid(column=1, row=3)
        self.password_entry.grid(column=1, row=4)
        self.gen_password_entry.grid(column=1, row=8)
        add_button.grid(column=1, row=6, columnspan=2)
        gen_pass_button.grid(column=1, row=9, columnspan=2)
        read_db_button.grid(column=1, row=10, columnspan=2)
        connect_to_db_button.grid(column=1, row=11, columnspan=2)

        # Button Grids
        search_button.grid(column=2, row=1)
        gen_pass_cpy_button.grid(column=2, row=8)

        self.window.mainloop()

    # # Functionality
    def gen_pass_func(self):
        self.gen_password_entry.delete(0, END)
        password = generate_password()
        self.gen_password_entry.insert(0, password)

    def copy_gen_password_func(self):
        pyperclip.copy(self.gen_password_entry.get())

    def save_pass_func(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        user_name = self.user_name_entry.get()
        password = self.password_entry.get()
        if pass_saver(website, email, user_name, password):
            self.website_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.user_name_entry.delete(0, END)
            self.password_entry.delete(0, END)

    def find_pass_func(self):
        website = self.website_entry.get()
        pass_finder(website)
