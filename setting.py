import tkinter
import tkinter.messagebox

import customtkinter as ctk
import pymongo
from customtkinter import *
from PIL import ImageTk, Image

import chatbox
import dashboard
import demo_workout
import mealplanner
import login
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

sx = 0
sy = 0


def profile(email="shri@gmail.com"):
    global sx, sy
    # create root frame for login1
    userdata = col.find_one({"email": email})
    user = CTk()
    user.title("GYMBuddy")
    print(userdata)
    user.geometry(f"{375}x{812}+{800}+{100}")
    userbg = ctk.CTkImage(Image.open("static/userprofile.png"), size=(375, 732))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-1, y=0)

    # fonts:
    font1 = ctk.CTkFont(family="Poppins", size=20, weight='bold')
    font2 = ctk.CTkFont(family="sans serif", size=16, weight='bold')
    font3 = ctk.CTkFont(family="sans serif", size=14, weight='normal')
    font4 = ctk.CTkFont(family="sans serif", size=13, weight='normal')

    sx = sx + 1
    sy = sy + 1
    # Enter the details:

    fname = userdata["name"].split()[0].title()  # "Sumil Suthar"
    plan = userdata["difficulty"]  # "Lose a Fat Program"
    height = f"{userdata['height']} cm"  # height in cm
    weight = f"{userdata['weight']} kg"  # weight in kg
    age = f"{19}"
    bmi = f"{userdata['bmi']}"
    cstreak = f"{sx} days"
    tstreak = f"{sy} days"

    name = ctk.CTkLabel(user, text=fname, font=font1, text_color="#1D1617", fg_color="#FFFFFF")
    name.place(x=110, y=85)
    plan_label = ctk.CTkLabel(user, text=plan, font=font3, text_color="#7B6F72", fg_color="#FFFFFF")
    plan_label.place(x=110, y=109)
    height_label = ctk.CTkLabel(user, text=height, font=font2, text_color="#9DCEFF", fg_color="#FFFFFF")
    height_label.place(x=50, y=172)
    weight_label = ctk.CTkLabel(user, text=weight, font=font2, text_color="#9DCEFF", fg_color="#FFFFFF")
    weight_label.place(x=168, y=172)
    age_label = ctk.CTkLabel(user, text=age, font=font2, text_color="#9DCEFF", fg_color="#FFFFFF")
    age_label.place(x=288, y=172)
    bmi_label = ctk.CTkLabel(user, text=bmi, font=font2, text_color="#9DCEFF", fg_color="#FFFFFF")
    bmi_label.place(x=61, y=268)
    cstreak_label = ctk.CTkLabel(user, text=cstreak, font=font2, text_color="#9DCEFF", fg_color="#FFFFFF")
    cstreak_label.place(x=161, y=268)
    tstreak_label = ctk.CTkLabel(user, text=tstreak, font=font2, text_color="#9DCEFF", fg_color="#FFFFFF")
    tstreak_label.place(x=272, y=268)

    b11 = ctk.CTkButton(user, text="Personal Data", font=font4, fg_color="#FFFFFF", hover=False, text_color="#7B6F72",
                        width=84, height=18)
    b11.place(x=73, y=406)
    b12 = ctk.CTkButton(user, text="Achievement", font=font4, fg_color="#FFFFFF", hover=False, text_color="#7B6F72",
                        width=84, height=18)
    b12.place(x=73, y=437)
    b13 = ctk.CTkButton(user, text="Workout Progress", font=font4, fg_color="#FFFFFF", hover=False,
                        text_color="#7B6F72",
                        width=120, height=18, compound="left")
    b13.place(x=73, y=468)

    b21 = ctk.CTkButton(user, text="Contact Us  ", font=font4, fg_color="#FFFFFF", hover=False,
                        text_color="#7B6F72", corner_radius=0,
                        width=75, height=18)
    b21.place(x=75, y=604)

    def gologin():
        user.destroy()
        login.login()

    b23 = ctk.CTkButton(user, text="logout  ", font=font4, fg_color="#FFFFFF", hover=False,
                        text_color="#7B6F72", corner_radius=0,
                        width=49, height=18, command=gologin)
    b23.place(x=73, y=664)

    def goback():
        user.destroy()
        dashboard.dashboard(email)

    back_img = ctk.CTkImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_button = ctk.CTkButton(user, image=back_img, text="", fg_color="#FFFFFF", hover=False, height=32, width=32,
                                command=goback)
    back_button.place(x=21, y=21)

    # navigation bar
    def viewprofile():
        user.destroy()
        profile(email)

    def gomeal():
        user.destroy()
        mealplanner.mealplanner(email)

    def goachive():
        user.destroy()
        chatbox.achievement_section(email)

    def godemo():
        user.destroy()
        demo_workout.startpage(email)

    def gohom():
        user.destroy()
        dashboard.dashboard(email)

    # navigation bar
    div1 = ctk.CTkCanvas(user, height=80, width=375, background="#FFFFFF", borderwidth=0, highlightthickness=0)
    div1.place(x=0, y=728)
    b1_img = ctk.CTkImage(Image.open("static/icons8-fire-alt-32.png"), size=(36, 36))
    b2_img = ctk.CTkImage(Image.open("./static/icons8-gym-32.png"), size=(32, 32))
    b3_img = ctk.CTkImage(Image.open("./static/Activity.png"), size=(30, 30))
    b4_img = ctk.CTkImage(Image.open("./static/Profile.png"), size=(30, 30))
    b5_img = ctk.CTkImage(Image.open("./static/Component 1.png"), size=(104, 104))
    b1 = ctk.CTkButton(div1, image=b1_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                       command=gomeal)
    b2 = ctk.CTkButton(div1, image=b2_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                       command=godemo)
    b3 = ctk.CTkButton(div1, image=b3_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                       command=goachive)
    b4 = ctk.CTkButton(div1, image=b4_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                       command=viewprofile)
    b5 = ctk.CTkButton(div1, image=b5_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                       command=gohom)
    b1.place(x=15, y=21)
    b2.place(x=85, y=23)
    b3.place(x=240, y=25)
    b4.place(x=315, y=25)
    # b5.place(x=130,y=715)
    b5.place(x=125, y=-5)
    user.resizable(False, False)
    user.mainloop()


if __name__ == "__main__":
    profile()
