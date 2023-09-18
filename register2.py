import tkinter
import tkinter.messagebox
import customtkinter as ctk
import pymongo

import register3
from PIL import ImageTk, Image
from customtkinter import *

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

def register2(email="shri@gmail.com"):
    register2 = CTk()

    register2.title("Login Page")

    register2.geometry(f"{375}x{812}+{800}+{100}")
    register2bg = ctk.CTkImage(Image.open("./static/register2.png"), size=(375, 812))
    register2bg_label = ctk.CTkLabel(register2, text="", corner_radius=5, image=register2bg)
    register2bg_label.place(x=-5, y=0)
    register2.resizable(False, False)

    # dropdown
    n = tkinter.StringVar(value="Gender")
    combobx = ctk.CTkComboBox(register2, border_width=1.5, border_color="#94a8fe",
                              width=315, height=48, corner_radius=30,
                              bg_color="#ffffff", variable=n, values=("Male", "Female", "Other"))
    combobx.place(x=30, y=446)
    # entry text box
    dob_txt = ctk.CTkEntry(register2, border_width=1.5, border_color="#94a8fe",
                           placeholder_text="DOB DD/MM/YYYY", width=315, height=48, corner_radius=30,
                           bg_color="#ffffff")

    dob_txt.place(x=30, y=512)

    weight_txt = ctk.CTkEntry(register2, border_width=1.5, border_color="#94a8fe",
                              placeholder_text="Weight", width=245, height=48, corner_radius=30,
                              bg_color="#ffffff")
    weight_txt.place(x=30, y=575)

    height_txt = ctk.CTkEntry(register2, border_width=1.5, border_color="#94a8fe",
                              placeholder_text="Height", width=245, height=48, corner_radius=30,
                              bg_color="#ffffff")
    height_txt.place(x=30, y=635)

    # func for buttons
    def register3btn():
        gender = combobx.get()
        dob = dob_txt.get()
        weight = int(weight_txt.get())
        height = int(height_txt.get())
        bmivalue = round((weight / (height * height)) * 10000, 1)
        print(bmivalue)
        if gender=="" or dob=="" or weight=="" or height=="":
            tkinter.messagebox.showerror(title="Error", message="Enter all parameters")
        else:
            col.update_one({"email":email},{'$set': {"gender":gender,'weight':weight,"height":height,"dob":dob,"bmi":bmivalue}},upsert=True)
            tkinter.messagebox.showinfo(title="", message="SUCCESS")
            register2.destroy()
            register3.register3(email)



    # buttons
    reg_btn_img2 = ImageTk.PhotoImage(Image.open("./static/nextbtn.png"), size=(315, 60))

    reg_btn2 = tkinter.Button(register2, image=reg_btn_img2, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
                              command=register3btn)
    reg_btn2.place(x=10, y=700)

    register2.mainloop()


if __name__ == "__main__":
    register2()
