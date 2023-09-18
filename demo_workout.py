import tkinter
import tkinter.messagebox
import time
import customtkinter as ctk
import pymongo
from customtkinter import *
from PIL import ImageTk, Image, ImageGrab
import pyscreenshot

import chatbox
import dashboard
import mealplanner
import setting

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

totalminutes = 0
seconds = 0
stop = 0
cal = 80
totalex = 2
client = pymongo.MongoClient(
    "mongodb+srv://sarthak0714:sarthak0714@cluster0714.9yk64zv.mongodb.net/?retryWrites=true&w=majority")
db = client['PYTHON_MPR']
col = db["mpr"]
emailtest = "shri@gmail.com"


def startpage(email="shri@gmail.com"):
    global emailtest
    emailtest = email
    print(emailtest)
    getdata = col.find_one({"email": email})
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{812}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=100, weight='bold')
    userbg = ctk.CTkImage(Image.open("static/demoworkoutpage.png"), size=(375, 732))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)

    def gowk():
        user.destroy()
        workout()

    def goback():
        user.destroy()
        dashboard.dashboard(emailtest)

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(user, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=goback)
    back_btn.place(x=22, y=16)

    btn_start_img = ctk.CTkImage(Image.open("./static/startwkout.png"), size=(359, 103))
    btn_start = ctk.CTkButton(user, image=btn_start_img, hover=False, fg_color="#FFFFFF", command=gowk, cursor="hand2")
    btn_start.place(x=0, y=620)

    def goskipping():
        user.destroy()
        skipping()

    skipping_img = ImageTk.PhotoImage(Image.open("./static/skipping.png"), size=(311, 60))
    skipping_btn = tkinter.Button(user, image=skipping_img, borderwidth=0, activebackground="#ffffff",
                                  background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                  command=goskipping)
    skipping_btn.place(x=31, y=425)

    def gopushup():
        user.destroy()
        pushup()

    pushups_img = ImageTk.PhotoImage(Image.open("./static/pushups.png"), size=(311, 60))
    pushups_btn = tkinter.Button(user, image=pushups_img, borderwidth=0, activebackground="#ffffff",
                                 background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                 command=gopushup)
    pushups_btn.place(x=29, y=503)

    def viewprofile():
        user.destroy()
        setting.profile(emailtest)

    def gomeal():
        user.destroy()
        mealplanner.mealplanner(emailtest)

    def goachive():
        user.destroy()
        chatbox.achievement_section(emailtest)

    def godemo():
        user.destroy()
        startpage(emailtest)

    def gohom():
        user.destroy()
        dashboard.dashboard(emailtest)

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


def pushup():
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{588}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=100, weight='bold')
    userbg = ctk.CTkImage(Image.open("./static/Pushups (1).png"), size=(375, 588))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)

    def back():
        user.destroy()
        startpage()

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(user, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=back)
    back_btn.place(x=35, y=30)

    def skipping_steps():
        user.destroy()
        push_steps()

    steps_img = ImageTk.PhotoImage(Image.open("./static/how to do it.png"), size=(315, 60))
    steps_btn = tkinter.Button(user, image=steps_img, borderwidth=0,
                               activebackground="#ffffff",
                               background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                               command=skipping_steps)
    steps_btn.place(x=10, y=480)

    user.mainloop()


def push_steps():
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{588}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=100, weight='bold')
    userbg = ctk.CTkImage(Image.open("./static/Skipping-steps.png"), size=(375, 588))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)

    def back():
        user.destroy()
        pushup()

    back_img_forsteppage = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn_forsteppage = tkinter.Button(user, image=back_img_forsteppage, borderwidth=0,
                                          activebackground="#ffffff",
                                          background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                          command=back)
    back_btn_forsteppage.place(x=35, y=30)

    user.mainloop()


def skipping():
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{588}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=100, weight='bold')
    userbg = ctk.CTkImage(Image.open("./static/Skipping (1).png"), size=(375, 588))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)

    def skipping_steps():
        user.destroy()
        skip_steps()

    steps_img = ImageTk.PhotoImage(Image.open("./static/how to do it.png"), size=(315, 60))
    steps_btn = tkinter.Button(user, image=steps_img, borderwidth=0,
                               activebackground="#ffffff",
                               background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                               command=skipping_steps)
    steps_btn.place(x=10, y=450)

    def back():
        user.destroy()
        startpage()

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(user, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=back)
    back_btn.place(x=35, y=30)
    user.mainloop()


def skip_steps():
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{588}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=100, weight='bold')
    userbg = ctk.CTkImage(Image.open("./static/Skipping-steps.png"), size=(375, 588))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)

    def back():
        user.destroy()
        skipping()

    back_img_forsteppage = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn_forsteppage = tkinter.Button(user, image=back_img_forsteppage, borderwidth=0,
                                          activebackground="#ffffff",
                                          background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat",
                                          command=back)
    back_btn_forsteppage.place(x=35, y=30)

    user.mainloop()


def ex1():
    ex = CTk()
    ex.title("GYMBuddy")
    ex.geometry(f"{375}x{812}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=80, weight='bold')
    font2 = ctk.CTkFont(family="Poppins", size=22, weight='bold')
    userbg = ctk.CTkImage(Image.open("static/ex11.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(ex, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)
    sec_lab = ctk.CTkLabel(ex, text="sec", font=font2, text_color="#92A3FD",
                           fg_color="#FFFFFF")
    sec_lab.place(x=168, y=620)

    def start():
        global seconds
        ex.update()
        time.sleep(1)
        seconds += 1
        if stop == 0:
            textprint = f"{seconds}"
            if seconds <= 9:
                textprint = f"0{seconds}"
            seconds_label = ctk.CTkLabel(ex, text=textprint, font=font1, text_color="#92A3FD",
                                         fg_color="#FFFFFF", width=30)
            seconds_label.after(100, start)
            seconds_label.place(x=145, y=535)
        if stop == 1:
            seconds -= 1
            pass

    def pause():
        global stop
        t = 0
        if stop == 1:
            stop = 0
            start()
        else:
            stop = 1

    def done():
        global stop, seconds
        global totalminutes
        stop = 1
        ex.destroy()
        totalminutes += seconds
        seconds = 0
        stop = 0
        print(totalminutes)
        rest()

    start()

    exercise_img = ctk.CTkImage(Image.open("./static/playpause.png"), size=(190, 104))
    exercise_button = ctk.CTkButton(ex, text="", width=100, height=50, corner_radius=30, image=exercise_img,
                                    border_width=0,
                                    fg_color="#FFFFFF", hover=False, command=pause)
    exercise_button.place(x=-24, y=711)
    exercise1_img = ctk.CTkImage(Image.open("./static/nextbtn1.png"), size=(190, 104))
    exercise1_button = ctk.CTkButton(ex, text="", width=35, height=25, corner_radius=30, image=exercise1_img,
                                     fg_color="#FFFFFF", hover=False, command=done)
    exercise1_button.place(x=173, y=711)

    ex.resizable(False, False)
    ex.mainloop()


def workout():
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{812}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=100, weight='bold')
    userbg = ctk.CTkImage(Image.open("static/ready_img2.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)
    seconds_string = StringVar()
    seconds_string.set("00")
    seconds_label = ctk.CTkLabel(user, textvariable=seconds_string, font=font1, text_color="#92A3FD",
                                 fg_color="#FFFFFF")
    seconds_label.place(x=132, y=350)
    sec = StringVar()

    def runtime():
        clocktime = 3
        while clocktime > -1:
            totalmin, totalsec = divmod(clocktime, 60)
            seconds_string.set("{0:2d}".format(totalsec))
            user.update()
            time.sleep(1)
            clocktime -= 1
            sec = clocktime
            if sec == -1:
                user.destroy()
                ex1()

    runtime()

    user.resizable(False, False)
    user.mainloop()


def rest():
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{812}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=100, weight='bold')
    userbg = ctk.CTkImage(Image.open("static/restperiod.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)
    seconds_string = StringVar()
    seconds_string.set("00")
    seconds_label = ctk.CTkLabel(user, textvariable=seconds_string, font=font1, text_color="#92A3FD",
                                 fg_color="#FFFFFF")
    seconds_label.place(x=132, y=350)
    sec = StringVar()

    def runtime():
        clocktime = 10
        while clocktime > -1:
            totalmin, totalsec = divmod(clocktime, 60)
            seconds_string.set("{0:2d}".format(totalsec))
            user.update()
            time.sleep(1)
            clocktime -= 1
            sec = clocktime
            if sec == -1:
                user.destroy()
                ex2()

    runtime()
    global seconds
    seconds = 0

    user.resizable(False, False)
    user.mainloop()


def ex2():
    ex = CTk()
    ex.title("GYMBuddy")
    ex.geometry(f"{375}x{812}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=80, weight='bold')
    font2 = ctk.CTkFont(family="Poppins", size=22, weight='bold')
    userbg = ctk.CTkImage(Image.open("static/psh11.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(ex, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)
    sec_lab = ctk.CTkLabel(ex, text="sec", font=font2, text_color="#92A3FD",
                           fg_color="#FFFFFF")
    sec_lab.place(x=168, y=620)

    def start():
        global seconds
        ex.update()
        time.sleep(1)
        seconds += 1
        if stop == 0:
            textprint = f"{seconds}"
            if seconds <= 9:
                textprint = f"0{seconds}"
            seconds_label = ctk.CTkLabel(ex, text=textprint, font=font1, text_color="#92A3FD",
                                         fg_color="#FFFFFF", width=30)
            seconds_label.after(100, start)
            seconds_label.place(x=145, y=535)
        if stop == 1:
            seconds -= 1
            pass

    def pause():
        global stop
        t = 0
        if stop == 1:
            stop = 0
            start()
        else:
            stop = 1

    def done():
        global stop
        global totalminutes
        stop = 1
        ex.destroy()
        totalminutes += seconds
        totalminutes += 10
        print(totalminutes)
        final()

    start()

    exercise_img = ctk.CTkImage(Image.open("./static/playpause.png"), size=(190, 104))
    exercise_button = ctk.CTkButton(ex, text="", width=100, height=50, corner_radius=30, image=exercise_img,
                                    border_width=0,
                                    fg_color="#FFFFFF", hover=False, command=pause)
    exercise_button.place(x=-24, y=711)
    exercise1_img = ctk.CTkImage(Image.open("./static/nextbtn1.png"), size=(190, 104))
    exercise1_button = ctk.CTkButton(ex, text="", width=35, height=25, corner_radius=30, image=exercise1_img,
                                     fg_color="#FFFFFF", hover=False, command=done)
    exercise1_button.place(x=173, y=711)

    ex.resizable(False, False)
    ex.mainloop()


def final():
    col.update_one({"email": emailtest}, {"$set": {"progressbar.6": 0.5}}, upsert=True)
    # create root frame for login1
    user = CTk()
    user.title("GYMBuddy")

    user.geometry(f"{375}x{812}+{800}+{100}")
    font1 = ctk.CTkFont(family="Poppins", size=45, weight='bold')
    userbg = ctk.CTkImage(Image.open("static/achieve.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(user, text="", corner_radius=5, image=userbg, fg_color="#FFFFFF")
    bg_label.place(x=-5, y=0)
    # seconds_label = ctk.CTkLabel(user, textvariable=seconds_string, font=font1, text_color="#92A3FD",
    #                            fg_color="#FFFFFF")
    # seconds_label.place(x=132, y=350)
    totalmin, totalsec = divmod(totalminutes, 60)
    s = f"{totalmin}:{totalsec}"
    if totalmin < 10 and totalsec < 10:
        f"0{totalmin}:0{totalsec}"
    elif totalmin < 10 and 10 <= totalsec:
        f"0{totalmin}:{totalsec}"
    elif totalmin >= 10 and 10 > totalsec:
        f"{totalmin}:0{totalsec}"
    min_label = ctk.CTkLabel(user, text=s, font=font1, text_color="#92A3FD",
                             fg_color="#FFFFFF")
    min_label.place(x=270, y=530)
    cal_label = ctk.CTkLabel(user, text=f"{cal}", font=font1, text_color="#92A3FD",
                             fg_color="#FFFFFF")
    cal_label.place(x=175, y=530)
    ex_label = ctk.CTkLabel(user, text=f"0{totalex}", font=font1, text_color="#92A3FD",
                            fg_color="#FFFFFF")
    ex_label.place(x=60, y=530)
    awardedtime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(time.time()))
    fname = col.find_one({"email": emailtest})["name"].split()[0]

    # print(awardedtime)
    credit_label = ctk.CTkLabel(user, text=f"Awarded to {fname} on {awardedtime}\n by Team GYMBuddy",
                                fg_color="#FFFFFF", text_color="#7B6F72")
    credit_label.place(x=60, y=650)

    def screenshot():
        image_name = str(awardedtime).replace(" ", "_").replace(":", "_").split(",")[1] + "_" + fname + "_" + ".png"
        try:
            image = ImageGrab.grab(bbox=(807, 146, 1182, 933))  # 58, 140, 433, 812)
            image.save(f'./static/ac/{image_name}')
        except Exception as e:
            tkinter.messagebox.showinfo(title="ERROR404", message=f"Something went wrong\n Exception: {e}")
        print(image_name)

    def gohome():
        user.destroy()
        dashboard.dashboard(emailtest)

    b15_img = ctk.CTkImage(Image.open("./static/sharebtn1.png"), size=(190, 104))
    b15 = ctk.CTkButton(user, text="", command=screenshot, image=b15_img, width=60, height=40, fg_color="#FFFFFF",
                        hover=False)
    b15.place(x=-10, y=700)

    b16_img = ctk.CTkImage(Image.open("./static/homebtn1.png"), size=(190, 104))
    b16 = ctk.CTkButton(user, text="", command=gohome, image=b16_img, width=60, height=40, fg_color="#FFFFFF",
                        hover=False)
    b16.place(x=180, y=700)

    user.resizable(False, False)
    user.mainloop()


if __name__ == "__main__":
    startpage()
