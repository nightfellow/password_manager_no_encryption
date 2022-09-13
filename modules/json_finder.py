from tkinter import messagebox
import json


def pass_finder(website):

    if len(website) == 0:
        messagebox.showinfo(title="Error!", message="Empty fields detected!!!")
    else:
        try:
            with open("./data/data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="DB File not found", message="file not found!")
        else:
            if website in data:
                found_email = data[website]["email"]
                found_username = data[website]["username"]
                found_password = data[website]["password"]
                messagebox.showinfo(title=f"{website}", message=f"There is some data found: \n"
                                                                f"\nEmail: {found_email}"
                                                                f"\nUsername: {found_username}"
                                                                f"\nPassword: {found_password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} found!")
