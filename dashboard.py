import tkinter
import tkinter.messagebox

import customtkinter as ctk
import pymongo
from customtkinter import *
from PIL import ImageTk, Image
import setting
import workout_fullbody
import demo_workout
import mealplanner
import chatbox

# mongo connection
client = pymongo.MongoClient(
    "mongodb+srv://sarthak0714:sarthak0714@cluster0714.9yk64zv.mongodb.net/?retryWrites=true&w=majority")
db = client['PYTHON_MPR']
col = db["mpr"]
email1 = "shri@gmail.com"
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def workout_done():
    # create root frame for login1
    login1 = CTk()
    login1.title("FitnessX")
    login1.resizable(False, False)

    def goback():
        login1.destroy()
        dashboard(email1)

    login1.geometry(f"{375}x{812}+{800}+{100}")
    loginbg = ctk.CTkImage(Image.open("static/Congratulations_Page.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(login1, text="", corner_radius=5, image=loginbg, fg_color="#FFFFFF")
    bg_label.place(x=-1, y=0)
    b1_img = ctk.CTkImage(Image.open("./static/workout_done_button.png"), size=(359, 104))
    b1 = ctk.CTkButton(login1, image=b1_img, fg_color="#FFFFFF", text="", hover=False, command=goback)
    b1.place(x=0, y=675)
    login1.mainloop()


def dashboard(email="shri@gmail.com"):
    # create root frame for db1
    global email1
    email1 = email
    db1 = CTk()
    db1.title("FitnessX")
    db1.geometry(f"{375}x{812}+{800}+{100}")
    # loginbg = ctk.CTkImage(Image.open("./static/loginpage(2).png"), size=(375, 812))
    bg_label = ctk.CTkLabel(db1, text="", corner_radius=5, height=812, width=385, fg_color="#F6F7F7")
    bg_label.place(x=-5, y=0)
    db1.resizable(False, False)

    db1.grid_columnconfigure(0, weight=1)
    db1.grid_rowconfigure(0, weight=1)

    # dashboard content
    scrollable_frame = ctk.CTkScrollableFrame(db1, width=375, height=732, border_width=0, fg_color="#FFFFFF")
    # div2 = ctk.CTkCanvas(db1, height=732, width=375, borderwidth=0, highlightthickness=0)
    scrollable_frame.place(x=0, y=0)
    b6_img = ctk.CTkImage(Image.open("static/dashboard_3.png"), size=(375, 1286))
    b6 = ctk.CTkLabel(scrollable_frame, text="", height=730, width=375, image=b6_img)
    scrollable_frame.grid(row=0, column=0, sticky="nsew")
    b6.grid(row=0, column=0)

    # fonts:
    font1 = ctk.CTkFont(family="Poppins", size=20, weight='bold')
    font2 = ctk.CTkFont(family="Poppins", size=16, weight='bold')
    font3 = ctk.CTkFont(family="Poppins", size=13, weight='normal')
    font4 = ctk.CTkFont(family="Poppins", size=10, weight='bold')

    # Enter the details:
    getdata = col.find_one({"email": email})

    fname = getdata["name"].split()[0].title()  # username
    height = getdata["height"]  # height in cm
    weight = getdata["weight"]  # weight in kg
    bmivalue = getdata["bmi"]  # round((weight / (height * height)) * 10000, 2)
    water_target = f"{8}L"
    step_target = f"{5000}"
    bmi_status = "You have a normal weight"
    total_calorie = getdata["calorie"]
    calorie_burn = 0
    calorie_left = f"{total_calorie - calorie_burn} Kcal\nleft"
    total_excersise = 15
    total_mins = 45

    progress = getdata["progressbar"]

    # bmi status:
    if 25 <= bmivalue < 30:
        bmi_status = "You are overweight         "
    elif 30 <= bmivalue:
        bmi_status = "You are obese  "
    elif 18.5 >= bmivalue:
        bmi_status = "You are underweight      "
    else:
        bmi_status = "You have normal weight"

    name = ctk.CTkLabel(scrollable_frame, text=fname, font=font1, text_color="#1D1617")
    name.place(x=20, y=30)
    bmi = ctk.CTkLabel(scrollable_frame, text=str(bmivalue), font=("Poppins", 14), text_color="#FFFFFF",
                       fg_color="#C58BF2")
    bmi.place(x=270, y=105)
    water_label = ctk.CTkLabel(scrollable_frame, text=water_target, text_color="#9DCEFF", font=font2)
    water_label.place(x=83, y=305)
    step_label = ctk.CTkLabel(scrollable_frame, text=step_target, text_color="#9DCEFF", font=font2)
    step_label.place(x=228, y=305)
    bmi_image = ctk.CTkImage(Image.open("./static/bluecolor.png"), size=(170, 28))
    bmi_status_label = ctk.CTkLabel(scrollable_frame, text=bmi_status, font=font3, image=bmi_image,
                                    text_color="#FFFFFF", justify="left")
    bmi_status_label.place(x=28, y=120)
    calorie_image = ctk.CTkImage(Image.open("./static/bluecolor.png"), size=(58, 30))
    calorie_label = ctk.CTkLabel(scrollable_frame, text=calorie_left, font=font4, image=calorie_image,
                                 text_color="#FFFFFF")
    calorie_label.place(x=238, y=745)
    exercise_img = ctk.CTkImage(Image.open("./static/lightbluecolor.png"), size=(150, 30))
    excersise = ctk.CTkLabel(scrollable_frame, font=font3, image=exercise_img, text_color="#7B6F72",
                             text=f"{total_excersise} Exercises | {total_mins}mins")
    excersise.place(x=30, y=923)

    # Graph

    sun = ctk.CTkProgressBar(scrollable_frame, orientation="vertical", progress_color="#92A3FD", fg_color="#E5E5E5",
                             corner_radius=10)
    sun.set(progress[0])
    sun.configure(width=22, height=140)
    sun.place(x=38, y=460)

    mon = ctk.CTkProgressBar(scrollable_frame, orientation="vertical", progress_color="#92A3FD", fg_color="#E5E5E5",
                             corner_radius=10)
    mon.set(progress[1])
    mon.configure(width=22, height=140)
    mon.place(x=84, y=460)

    tues = ctk.CTkProgressBar(scrollable_frame, orientation="vertical", progress_color="#92A3FD", fg_color="#E5E5E5",
                              corner_radius=10)
    tues.set(progress[2])
    tues.configure(width=22, height=140)
    tues.place(x=125, y=460)

    wed = ctk.CTkProgressBar(scrollable_frame, orientation="vertical", progress_color="#92A3FD", fg_color="#E5E5E5",
                             corner_radius=10)
    wed.set(progress[3])
    wed.configure(width=22, height=140)
    wed.place(x=168, y=460)

    thur = ctk.CTkProgressBar(scrollable_frame, orientation="vertical", progress_color="#92A3FD", fg_color="#E5E5E5",
                              corner_radius=10)
    thur.set(progress[4])
    thur.configure(width=22, height=140)
    thur.place(x=211, y=460)

    fri = ctk.CTkProgressBar(scrollable_frame, orientation="vertical", progress_color="#92A3FD", fg_color="#E5E5E5",
                             corner_radius=10)
    fri.set(progress[5])
    fri.configure(width=22, height=140)
    fri.place(x=252, y=460)

    sat = ctk.CTkProgressBar(scrollable_frame, orientation="vertical", progress_color="#92A3FD", fg_color="#E5E5E5",
                             corner_radius=10)
    sat.set(progress[6])
    sat.configure(width=22, height=140)
    sat.place(x=295, y=460)

    def completed():
        db1.destroy()
        workout_fullbody.fullbody()

    exercise_button = ctk.CTkButton(scrollable_frame, text="View More", width=35, height=25, corner_radius=30,
                                    text_color="#9DCEFF", fg_color="#FFFFFF", hover=False, command=completed)
    exercise_button.place(x=43, y=971)

    def completed1():
        db1.destroy()
        demo_workout.startpage(email1)

    exercise_button1 = ctk.CTkButton(scrollable_frame, text="View More", width=35, height=25, corner_radius=30,
                                     text_color="#9DCEFF", fg_color="#FFFFFF", hover=False, command=completed1)
    exercise_button1.place(x=43, y=1127)

    def viewprofile():
        db1.destroy()
        setting.profile(email1)

    def gomeal():
        db1.destroy()
        mealplanner.mealplanner(email1)

    def goachive():
        db1.destroy()
        chatbox.achievement_section(email)

    def godemo():
        db1.destroy()
        demo_workout.startpage(email1)

    def gohom():
        db1.destroy()
        dashboard(email1)

    # navigation bar
    div1 = ctk.CTkCanvas(db1, height=80, width=375, background="#FFFFFF", borderwidth=0, highlightthickness=0)
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
    db1.mainloop()


if __name__ == "__main__":
    dashboard()
