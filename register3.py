import tkinter

import tkinter.messagebox
import customtkinter as ctk
import pymongo
# from login import login
from PIL import ImageTk, Image
from customtkinter import *

import login
import os
from dotenv import load_dotenv
load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(
    mongodb_uri)
db = client['PYTHON_MPR']
col = db["mpr"]

# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def register3(email="shri@gmail.com"):
    register3 = CTk()

    register3.title("Login Page")

    register3.geometry(f"{375}x{812}+{800}+{100}")
    register3bg = ctk.CTkImage(Image.open("./static/register2.png"), size=(375, 812))
    register3bg_label = ctk.CTkLabel(register3, text="", corner_radius=5, image=register3bg)
    register3bg_label.place(x=-5, y=0)
    register3.resizable(False, False)

    # dropdown
    n = tkinter.StringVar(value="Do You Have Access to Equipments?")
    combobx1 = ctk.CTkComboBox(register3, border_width=1.5, border_color="#94a8fe",
                               width=315, height=48, corner_radius=30,
                               bg_color="#ffffff", variable=n, values=("YES", "NO"))
    combobx1.place(x=30, y=446)
    nn = tkinter.StringVar(value="What is your experience with working-out?")
    combobx2 = ctk.CTkComboBox(register3, border_width=1.5, border_color="#94a8fe",
                               width=315, height=48, corner_radius=30,
                               bg_color="#ffffff", variable=nn, values=("Beginner", "Intermediate", "Advanced"))
    combobx2.place(x=30, y=635)

    # entry text box
    hours_txt = ctk.CTkEntry(register3, border_width=1.5, border_color="#94a8fe",
                             placeholder_text="How many hours can you working out?", width=315, height=48,
                             corner_radius=30,
                             bg_color="#ffffff")

    hours_txt.place(x=30, y=512)

    days_txt = ctk.CTkEntry(register3, border_width=1.5, border_color="#94a8fe",
                            placeholder_text="How many days a week will you workout?", width=315, height=48,
                            corner_radius=30,
                            bg_color="#ffffff")
    days_txt.place(x=30, y=575)

    # FUNCTIONS FOR BUTTONS
    def register3fn():
        getdata = col.find_one({"email": email})
        equipment = combobx1.get()
        difficulty = combobx2.get()
        hours = int(hours_txt.get())
        days = int(days_txt.get())
        cal = int()
        bmr = float()
        if getdata["gender"] == 'Male':
            cal = int(
                88.362 + (13.397 * float(getdata["weight"])) + (4.799 * float(getdata["height"])) - (5.677 * float(19)))
            bmr = round((88.362 + (13.397 * float(getdata["weight"])) + (4.799 * float(getdata["height"])) - (
                        5.677 * float(19))), 2)
            print(cal)
        elif getdata["gender"] == 'Female':
            cal = int(
                447.593 + (9.247 * float(getdata["weight"])) + (3.098 * float(getdata["height"])) - (4.330 * float(19)))
            bmr = round(
                447.593 + (9.247 * float(getdata["weight"])) + (3.098 * float(getdata["height"])) - (4.330 * float(19)),
                2)

        if difficulty == "Beginner":
            cal = cal * 1.1

        elif difficulty == "Intermediate":
            cal = cal * 1.55

        elif difficulty == "Advanced":
            cal = cal * 1.9

        if equipment == "" or difficulty == "" or hours == "" or days == "":
            tkinter.messagebox.showerror(title="Error", message="Enter all parameters")
        else:
            col.update_one({"email": email}, {
                '$set': {"equipment": equipment, "difficulty": difficulty, "hoursspent": hours, "dayssepnt": days,
                         "calorie": int(cal), "bmr": bmr}},
                           upsert=True)
            tkinter.messagebox.showinfo(title="", message="SUCCESS")
            register3.destroy()
            login.login()

    # buttons
    reg_btn_img2 = ImageTk.PhotoImage(Image.open("./static/nextbtn.png"), size=(315, 60))

    reg_btn2 = tkinter.Button(register3, image=reg_btn_img2, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
                              command=register3fn)
    reg_btn2.place(x=10, y=700)

    register3.mainloop()


if __name__ == "__main__":
    register3()
