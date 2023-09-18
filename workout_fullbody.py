from tkinter import *
import tkinter
import tkinter.messagebox
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image

import chatbox
import dashboard
import demo_workout
import mealplanner
import setting

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def fullbody(email="shri@gmail.com"):
    global workouts
    email1 = email
    workouts = customtkinter.CTk()
    workouts.geometry(f"{400}x{812}+{800}+{100}")

    scrollable_frame = customtkinter.CTkScrollableFrame(workouts, width=375, height=732, border_width=0,
                                                        fg_color="#FFFFFF")
    scrollable_frame.place(x=-5, y=0)
    scrollable_frame.grid(row=0, column=0, sticky="nsew")

    workoutpage = customtkinter.CTkImage(Image.open("./static/Workoutcard.png"), size=(375, 2461))
    bg_label = customtkinter.CTkLabel(scrollable_frame, text="", corner_radius=5, image=workoutpage, height=2461,
                                      width=375)
    bg_label.grid(row=0, column=0)

    def goback():
        workouts.destroy()
        dashboard.dashboard(email1)

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(scrollable_frame, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=goback)
    back_btn.place(x=35, y=40)

    details_img = ImageTk.PhotoImage(Image.open("./static/Detail-Navs.png"), size=(32, 32))
    details_btn = tkinter.Button(scrollable_frame, image=details_img, borderwidth=0, activebackground="#ffffff",
                                 background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    details_btn.place(x=316, y=40)

    schedule_img = ImageTk.PhotoImage(Image.open("./static/Schedule-Card.png"), size=(315, 50))
    schedule_btn = tkinter.Button(scrollable_frame, image=schedule_img, borderwidth=0, activebackground="#ffffff",
                                  background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    schedule_btn.place(x=35, y=453)

    difficulty_img = ImageTk.PhotoImage(Image.open("./static/Difficulity-Card.png"), size=(315, 50))
    schedule_btn = tkinter.Button(scrollable_frame, image=difficulty_img, borderwidth=0, activebackground="#ffffff",
                                  background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    schedule_btn.place(x=36, y=518)

    # BASIC EXERCISES

    warmup_img = ImageTk.PhotoImage(Image.open("./static/warmup.png"), size=(311, 60))
    warmup_btn = tkinter.Button(scrollable_frame, image=warmup_img, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    warmup_btn.place(x=31, y=867)

    jumpingjacks_img = ImageTk.PhotoImage(Image.open("./static/jumpingjacks.png"), size=(311, 60))
    jumpingjacks_btn = tkinter.Button(scrollable_frame, image=jumpingjacks_img, borderwidth=0,
                                      activebackground="#ffffff",
                                      background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                      command=description_jumping_jacks)
    jumpingjacks_btn.place(x=31, y=942)

    skipping_img = ImageTk.PhotoImage(Image.open("./static/skipping.png"), size=(311, 60))
    skipping_btn = tkinter.Button(scrollable_frame, image=skipping_img, borderwidth=0, activebackground="#ffffff",
                                  background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                  command=description_skipping)
    skipping_btn.place(x=31, y=1017)

    squats_img = ImageTk.PhotoImage(Image.open("./static/squats.png"), size=(311, 60))
    squats_btn = tkinter.Button(scrollable_frame, image=squats_img, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                command=description_squats)
    squats_btn.place(x=31, y=1092)

    standingcalves_img = ImageTk.PhotoImage(Image.open("./static/standingcalves.png"), size=(311, 60))
    standingcalves_btn = tkinter.Button(scrollable_frame, image=standingcalves_img, borderwidth=0,
                                        activebackground="#ffffff",
                                        background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    standingcalves_btn.place(x=31, y=1167)

    rest_img = ImageTk.PhotoImage(Image.open("./static/rest and drink.png"), size=(311, 60))
    rest_btn = tkinter.Button(scrollable_frame, image=rest_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    rest_btn.place(x=31, y=1242)

    # PUSHUPS

    incline_img = ImageTk.PhotoImage(Image.open("./static/inclinepushups.png"), size=(311, 60))
    incline_btn = tkinter.Button(scrollable_frame, image=incline_img, borderwidth=0, activebackground="#ffffff",
                                 background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    incline_btn.place(x=31, y=1341)

    pushups_img = ImageTk.PhotoImage(Image.open("./static/pushups.png"), size=(311, 60))
    pushups_btn = tkinter.Button(scrollable_frame, image=pushups_img, borderwidth=0, activebackground="#ffffff",
                                 background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                 command=description_pushups)
    pushups_btn.place(x=31, y=1416)

    # BICEPS

    bicepcurls_img = ImageTk.PhotoImage(Image.open("./static/Bicepcurls.png"), size=(315, 60))
    bicepcurls_btn = tkinter.Button(scrollable_frame, image=bicepcurls_img, borderwidth=0, activebackground="#ffffff",
                                    background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    bicepcurls_btn.place(x=29, y=1499)

    hammercurls_img = ImageTk.PhotoImage(Image.open("./static/Hammercurls.png"), size=(318, 59))
    hammercurls_btn = tkinter.Button(scrollable_frame, image=hammercurls_img, borderwidth=0, activebackground="#ffffff",
                                     background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    hammercurls_btn.place(x=27, y=1580)

    # SHOULDERS

    shoulderpress_img = ImageTk.PhotoImage(Image.open("./static/Shoulderpress.png"), size=(313, 59))
    shoulderpress_btn = tkinter.Button(scrollable_frame, image=shoulderpress_img, borderwidth=0,
                                       activebackground="#ffffff",
                                       background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    shoulderpress_btn.place(x=34, y=1648)

    armraises_img = ImageTk.PhotoImage(Image.open("./static/Armraises.png"), size=(311, 60))
    armraises_btn = tkinter.Button(scrollable_frame, image=armraises_img, borderwidth=0, activebackground="#ffffff",
                                   background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    armraises_btn.place(x=37, y=1723)

    lateralraises_img = ImageTk.PhotoImage(Image.open("./static/lateralraises.png"), size=(313, 59))
    lateralraises_btn = tkinter.Button(scrollable_frame, image=lateralraises_img, borderwidth=0,
                                       activebackground="#ffffff",
                                       background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    lateralraises_btn.place(x=37, y=1805)

    # BACK

    bentoverrows_img = ImageTk.PhotoImage(Image.open("./static/bentoverrows.png"), size=(314, 59))
    bentoverrows_btn = tkinter.Button(scrollable_frame, image=bentoverrows_img, borderwidth=0,
                                      activebackground="#ffffff",
                                      background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    bentoverrows_btn.place(x=36, y=1884)

    seatedrows_img = ImageTk.PhotoImage(Image.open("./static/seatedrows.png"), size=(313, 59))
    seatedrows_btn = tkinter.Button(scrollable_frame, image=seatedrows_img, borderwidth=0,
                                    activebackground="#ffffff",
                                    background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    seatedrows_btn.place(x=37, y=1961)

    # LEGS

    lunges_img = ImageTk.PhotoImage(Image.open("./static/Lunges.png"), size=(313, 59))
    lunges_btn = tkinter.Button(scrollable_frame, image=lunges_img, borderwidth=0,
                                activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    lunges_btn.place(x=38, y=2041)

    bulgarian_img = ImageTk.PhotoImage(Image.open("./static/bulgarian.png"), size=(313, 59))
    bulgarian_btn = tkinter.Button(scrollable_frame, image=bulgarian_img, borderwidth=0,
                                   activebackground="#ffffff",
                                   background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    bulgarian_btn.place(x=37, y=2121)

    # CHEST

    benchpress_img = ImageTk.PhotoImage(Image.open("./static/bench.png"), size=(316, 59))
    benchpress_btn = tkinter.Button(scrollable_frame, image=benchpress_img, borderwidth=0,
                                    activebackground="#ffffff",
                                    background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    benchpress_btn.place(x=34, y=2201)

    pecfly_img = ImageTk.PhotoImage(Image.open("./static/pecfly.png"), size=(313, 59))
    pecfly_btn = tkinter.Button(scrollable_frame, image=pecfly_img, borderwidth=0,
                                activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    pecfly_btn.place(x=37, y=2281)

    # START WORKOUT BUTTON

    startworkout_img = ImageTk.PhotoImage(Image.open("./static/startworkout.png"), size=(315, 60))
    startworkout_btn = tkinter.Button(scrollable_frame, image=startworkout_img, borderwidth=0,
                                      activebackground="#ffffff",
                                      background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat")
    startworkout_btn.place(x=27, y=2365)

    def viewprofile():
        workouts.destroy()
        setting.profile(email1)

    def gomeal():
        workouts.destroy()
        mealplanner.mealplanner(email1)

    def goachive():
        workouts.destroy()
        chatbox.achievement_section(email1)

    def godemo():
        workouts.destroy()
        demo_workout.startpage(email1)

    def gohom():
        workouts.destroy()
        dashboard.dashboard(email1)

    # navigation bar
    div1 = customtkinter.CTkCanvas(workouts, height=80, width=400, background="#FFFFFF", borderwidth=0,
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

    workouts.mainloop()


def description_jumping_jacks():
    workouts.withdraw()
    jumping_workout = Toplevel()
    jumping_workout.geometry(f"{375}x{588}+{800}+{100}")

    def back():
        jumping_workout.withdraw()
        workouts.deiconify()

    jumping_jacks = customtkinter.CTkImage(Image.open("./static/Jumping jacks.png"), size=(375, 588))
    bg_label1 = customtkinter.CTkLabel(jumping_workout, text="", corner_radius=5, image=jumping_jacks, height=588,
                                       width=375)
    bg_label1.grid(row=0, column=0)

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(jumping_workout, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=back)
    back_btn.place(x=35, y=40)

    jumping_workout.mainloop()


def description_squats():
    workouts.withdraw()
    squats = Toplevel()
    squats.geometry(f"{375}x{588}+{800}+{100}")

    def back():
        squats.withdraw()
        workouts.deiconify()

    squat = customtkinter.CTkImage(Image.open("./static/Squats (1).png"), size=(375, 588))
    bg_label1 = customtkinter.CTkLabel(squats, text="", corner_radius=5, image=squat, height=588,
                                       width=375)
    bg_label1.grid(row=0, column=0)

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(squats, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=back)
    back_btn.place(x=35, y=40)

    squats.mainloop()


def description_pushups():
    workouts.withdraw()
    pushups = Toplevel()
    pushups.geometry(f"{375}x{588}+{800}+{100}")

    def back():
        pushups.withdraw()
        workouts.deiconify()

    pushup = customtkinter.CTkImage(Image.open("./static/Pushups (1).png"), size=(375, 588))
    bg_label1 = customtkinter.CTkLabel(pushups, text="", corner_radius=5, image=pushup, height=588,
                                       width=375)
    bg_label1.grid(row=0, column=0)

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(pushups, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=back)
    back_btn.place(x=35, y=40)

    pushups.mainloop()


def description_skipping():
    workouts.withdraw()
    skipping = Toplevel()
    skipping.geometry(f"{375}x{588}+{800}+{100}")

    def back():
        skipping.withdraw()
        workouts.deiconify()

    skip = customtkinter.CTkImage(Image.open("./static/Skipping (1).png"), size=(375, 588))
    bg_label1 = customtkinter.CTkLabel(skipping, text="", corner_radius=5, image=skip, height=588,
                                       width=375)
    bg_label1.grid(row=0, column=0)

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(skipping, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=back)
    back_btn.place(x=35, y=40)

    steps_img = ImageTk.PhotoImage(Image.open("./static/how to do it.png"), size=(315, 60))
    steps_btn = tkinter.Button(skipping, image=steps_img, borderwidth=0,
                               activebackground="#ffffff",
                               background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                               command=skipping_steps)
    steps_btn.place(x=20, y=450)

    skipping.mainloop()


def skipping_steps():
    # skipping = description_skipping().skipping
    # skipping.withdraw()
    skipping_step = Toplevel()
    skipping_step.geometry(f"{390}x{728}+{800}+{100}")

    def back():
        # skipping.withdraw()
        skipping_step.withdraw()
        workouts.deiconify()

    skip_steps = customtkinter.CTkImage(Image.open("./static/Skipping-steps.png"), size=(390, 728))
    bg_label2 = customtkinter.CTkLabel(skipping_step, text="", corner_radius=5, image=skip_steps, height=728,
                                       width=390)
    bg_label2.grid(row=0, column=0)

    back_img_forsteppage = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn_forsteppage = tkinter.Button(skipping_step, image=back_img_forsteppage, borderwidth=0,
                                          activebackground="#ffffff",
                                          background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                          command=back)
    back_btn_forsteppage.place(x=35, y=40)

    skipping_step.mainloop()


if __name__ == "__main__":
    fullbody()
