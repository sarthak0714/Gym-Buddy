import tkinter
import tkinter.messagebox
import re
import pymongo
import dashboard
import encrypt
import register
import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image
import os
from dotenv import load_dotenv
load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(
    mongodb_uri)
db = client['PYTHON_MPR']
col = db["mpr"]
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



# show password func
def login():
    def showpass():
        if password_txt.cget("show") == "*":
            password_txt.configure(show="")

        else:
            password_txt.configure(show="*")

    # create root frame for login1
    login1 = CTk()
    login1.title("Login Page")
    login1.geometry(f"{375}x{812}+{800}+{100}")
    loginbg = ctk.CTkImage(Image.open("./static/loginpage1.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(login1, text="", corner_radius=5, image=loginbg)
    bg_label.place(x=0, y=0)
    login1.resizable(False, False)

    # text boxes

    email_txt = ctk.CTkEntry(login1, border_width=1.5, border_color="#94a8fe",
                             placeholder_text="Email", width=315, height=48, corner_radius=30,
                             bg_color="#ffffff")
    email_txt.place(x=30, y=129)
    password_txt = ctk.CTkEntry(login1, border_width=1.5, border_color="#94a8fe",
                                placeholder_text="Password", width=315, height=48, corner_radius=30,
                                bg_color="#ffffff", show='*')
    password_txt.place(x=30, y=192)

    # chkbox
    chk_box = ctk.CTkCheckBox(login1, width=16, height=16, text=None, border_width=1.5,
                              border_color="#94a8fe", command=showpass,
                              corner_radius=30, bg_color="#ffffff")
    chk_box.place(x=30, y=250)
    chk_label = ctk.CTkLabel(login1, text="show password", text_color="#ADA4A5", fg_color="#FFFFFF", width=117)
    chk_label.place(x=60, y=250)

    # functions
    def regfn():
        login1.destroy()
        register.register1()

    def loginfn():
        email = email_txt.get()
        password = password_txt.get()
        if re.findall(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]', email):
            z = col.find_one({"email": email})
            strpas = encrypt.decrypt(z["password"])
            if strpas == password:
                tkinter.messagebox.showinfo(title="", message="SUCCESS")
                login1.destroy()
                dashboard.dashboard(email)
            else:
                tkinter.messagebox.showerror(title="Error", message="Enter Valid Password or Email")
        else:
            tkinter.messagebox.showerror(title="Error", message="Enter Valid Email")

    # buttons
    reg_btn_img = ImageTk.PhotoImage(Image.open("./static/regb.png"), size=(315, 60))
    reg_btn = tkinter.Button(login1, image=reg_btn_img, borderwidth=0, activebackground="#ffffff",
                             background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
                             command=regfn)
    reg_btn.place(x=10, y=651)

    login_btn_img = ImageTk.PhotoImage(Image.open("./static/loginb.png"), size=(315, 60))
    login_btn = tkinter.Button(login1, image=login_btn_img, borderwidth=0, activebackground="#ffffff",
                               background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
                               command=loginfn)
    login_btn.place(x=10, y=523)

    login1.mainloop()


if __name__ == "__main__":
    login()
