import tkinter

import tkinter.messagebox
import customtkinter as ctk
import re
import encrypt
import login
import register2
from PIL import ImageTk, Image
from customtkinter import *
import pymongo

# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# mongo connection
import os
from dotenv import load_dotenv
load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(
    mongodb_uri)
db = client['PYTHON_MPR']
col = db["mpr"]

# show password func


# register page 1 root frame
def register1():
    register1 = CTk()

    register1.title("Login Page")

    register1.geometry(f"{375}x{812}+{800}+{100}")
    register1bg = ctk.CTkImage(Image.open("./static/regbg2.png"), size=(375, 812))
    register1bg_label = ctk.CTkLabel(register1, text="", corner_radius=5, image=register1bg)
    register1bg_label.place(x=-5, y=0)
    register1.resizable(False, False)

    # textboxes

    registerfname_txt = ctk.CTkEntry(register1, border_width=1.5, border_color="#94a8fe",
                                     placeholder_text="Full Name", width=315, height=48, corner_radius=30,
                                     bg_color="#ffffff")
    registerfname_txt.place(x=30, y=148)
    registeremail_txt = ctk.CTkEntry(register1, border_width=1.5, border_color="#94a8fe",
                                     placeholder_text="Email", width=315, height=48, corner_radius=30,
                                     bg_color="#ffffff")
    registeremail_txt.place(x=30, y=211)
    registerpassword_txt = ctk.CTkEntry(register1, border_width=1.5, border_color="#94a8fe",
                                        placeholder_text="Password", width=315, height=48,
                                        corner_radius=30, bg_color="#ffffff", show='*')
    registerpassword_txt.place(x=30, y=274)

    registercpassword_txt = ctk.CTkEntry(register1, border_width=1.5, border_color="#94a8fe",
                                         placeholder_text="Confirm Password", width=315, height=48,
                                         corner_radius=30, bg_color="#ffffff", show='*')
    registercpassword_txt.place(x=30, y=337)

    # chkbox
    def showpassreg():
        if registerpassword_txt.cget("show") == "*" and registercpassword_txt.cget("show") == "*":
            registerpassword_txt.configure(show="")
            registercpassword_txt.configure(show="")
        else:
            registerpassword_txt.configure(show="*")
            registercpassword_txt.configure(show="*")

    registerchk_box = ctk.CTkCheckBox(register1, width=16, height=16, text=None, border_width=1.5,
                                      border_color="#94a8fe", command=showpassreg,
                                      corner_radius=30, bg_color="#ffffff")
    registerchk_box.place(x=25, y=395)

    chk_label = ctk.CTkLabel(register1, text="show password", text_color="#ADA4A5", fg_color="#FFFFFF", width=120)
    chk_label.place(x=56, y=395)

    #functions
    def registerfn():
        name = registerfname_txt.get()
        email = registeremail_txt.get()
        password = registerpassword_txt.get()
        cpassword = registercpassword_txt.get()

        if name == "" or email == "" or password == "" or cpassword == "":
            tkinter.messagebox.showerror(title="Invalid Parameters", message="Please Enter all parameters")
        elif password != cpassword:
            tkinter.messagebox.showerror(title="Error", message="Passwords do not match")
        elif not re.findall(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]', email):
            tkinter.messagebox.showerror(title="Error", message="Enter Valid Email")
        else:
            tkinter.messagebox.showinfo(title="", message="SUCCESS")
            col.insert_one({'name': name, "email": email, "password": encrypt.encrypt(password),"progressbar":[0.0,0.0,0.0,0.0,0.0,0.0,0.0]})
            register1.destroy()
            register2.register2(email)


    def loginfn():
        register1.destroy()
        login.login()


    # buttons
    reg_btn_img1 = ImageTk.PhotoImage(Image.open("./static/regb.png"), size=(315, 60))
    login_btn_img1 = ImageTk.PhotoImage(Image.open("./static/loginb.png"), size=(315, 60))

    login_btn1 = tkinter.Button(register1, image=login_btn_img1, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
                                command=loginfn)
    login_btn1.place(x=10, y=620)

    reg_btn1 = tkinter.Button(register1, image=reg_btn_img1, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
                              command=registerfn)
    reg_btn1.place(x=10, y=460)
    register1.mainloop()


if __name__ == "__main__":
    register1()
