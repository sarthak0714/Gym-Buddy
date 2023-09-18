# date_email
from tkinter import *
import tkinter
import tkinter.messagebox
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
import os

import dashboard
import mealplanner
import setting
from demo_workout import startpage

email1 = "shri@gmail.com"


def achievement_section(email="shri@gmail.com"):
    global email1
    email1 = email
    achievement = customtkinter.CTk()
    achievement.title("Achievement Section")
    achievement.geometry(f"{400}x{812}+{800}+{100}")

    scrollable_frame = customtkinter.CTkScrollableFrame(achievement, width=375, height=732, border_width=0,
                                                        fg_color="#FFFFFF")
    scrollable_frame.place(x=-5, y=0)
    scrollable_frame.grid(row=0, column=0, sticky="nsew")

    chatboxpage = customtkinter.CTkImage(Image.open("./static/Chatbox.png"), size=(400, 1640))
    bg_label = customtkinter.CTkLabel(scrollable_frame, text="", corner_radius=5, image=chatboxpage, height=4000,
                                      width=375)
    bg_label.grid(row=0, column=0)
    font1 = customtkinter.CTkFont(family="Poppins", size=18, weight='bold')
    ach_label = customtkinter.CTkLabel(scrollable_frame, text="Community Achievement", fg_color="#FFFFFF", font=font1,
                                       text_color="#1D1617")
    ach_label.place(x=90, y=12)

    def back():
        achievement.destroy()
        dashboard.dashboard(email1)

    back_img_forsteppage = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn_forsteppage = tkinter.Button(scrollable_frame, image=back_img_forsteppage, borderwidth=0,
                                          activebackground="#ffffff",
                                          background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                          command=back)
    back_btn_forsteppage.place(x=15, y=10)

    references = []  # <--
    for (root, dirs, files) in os.walk("C:/Users/Sumil/Desktop/we-go-jim/static/ac/"):
        if files:
            a = 43
            b = 70
            c = 45
            d = 50
            for file in files:
                path = os.path.join("C:/Users/Sumil/Desktop/we-go-jim/static/ac/", file)
                image = Image.open(path)
                n_image = image.resize((300, 500))
                photo = ImageTk.PhotoImage(n_image)
                img_label = tkinter.Label(scrollable_frame, image=photo)
                img_label.place(x=a, y=b)
                b = b + 560
                img_label.config(pady=30)
                # img_label.pack()
                references.append(photo)
                x = file.split("_")
                z = f"{x[7].title()}            {x[1]} {x[2]} {x[3]}"
                font2 = customtkinter.CTkFont(family="Poppins", size=16, weight="bold")
                title_label = customtkinter.CTkLabel(scrollable_frame, text=z, fg_color="#FFFFFF", font=font2,
                                                     text_color="#7B6F72", width=300)
                title_label.place(x=c, y=d)
                d = d + 560

    def viewprofile():
        achievement.destroy()
        setting.profile(email1)

    def gomeal():
        achievement.destroy()
        mealplanner.mealplanner(email1)

    def goachive():
        achievement.destroy()
        achievement_section(email1)

    def godemo():
        achievement.destroy()
        startpage(email1)

    def gohom():
        achievement.destroy()
        dashboard.dashboard(email1)

    # navigation bar
    div1 = customtkinter.CTkCanvas(achievement, height=80, width=400, background="#FFFFFF", borderwidth=0,
                                   highlightthickness=0)
    div1.place(x=0, y=728)
    b1_img = customtkinter.CTkImage(Image.open("static/icons8-fire-alt-32.png"), size=(36, 36))
    b2_img = customtkinter.CTkImage(Image.open("./static/icons8-gym-32.png"), size=(32, 32))
    b3_img = customtkinter.CTkImage(Image.open("./static/Activity.png"), size=(30, 30))
    b4_img = customtkinter.CTkImage(Image.open("./static/Profile.png"), size=(30, 30))
    b5_img = customtkinter.CTkImage(Image.open("./static/Component 1.png"), size=(104, 104))
    b1 = customtkinter.CTkButton(div1, image=b1_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                                 command=gomeal)
    b2 = customtkinter.CTkButton(div1, image=b2_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                                 command=godemo)
    b3 = customtkinter.CTkButton(div1, image=b3_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                                 command=goachive)
    b4 = customtkinter.CTkButton(div1, image=b4_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                                 command=viewprofile)
    b5 = customtkinter.CTkButton(div1, image=b5_img, text="", fg_color="#FFFFFF", hover=False, height=30, width=30,
                                 command=gohom)
    b1.place(x=20, y=21)
    b2.place(x=95, y=23)
    b3.place(x=255, y=25)
    b4.place(x=335, y=25)
    # b5.place(x=130,y=715)
    b5.place(x=140, y=-5)
    achievement.mainloop()


if __name__ == '__main__':
    achievement_section()
