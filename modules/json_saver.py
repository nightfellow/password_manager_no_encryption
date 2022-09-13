from tkinter import messagebox
import json


def pass_saver(website, email, user_name, password):
    new_data = {
        website: {
            "email": email,
            "username": user_name,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(user_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error!", message="Empty fields detected!!!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered for {website} website/service: "
                                               f"\n\nEmail: {email}\nUser Name: {user_name}\nPassword: {password}"
                                               f"\n\nIs it ok to save?")
        if is_ok:
            try:
                with open("./data/data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("./data/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)

                with open("./data/data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

        return is_ok
