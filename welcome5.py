import tkinter
import tkinter.messagebox

import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

import login

# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def wlc5():
    wlc5 = CTk()
    wlc5.title("Home Page")
    wlc5.geometry(f"{375}x{812}+{800}+{100}")
    wlc5bgimg = ctk.CTkImage(Image.open("./static/wlc5.png"), size=(375, 812))
    wlc5_bg = ctk.CTkLabel(wlc5, text="", corner_radius=5, image=wlc5bgimg )
    wlc5_bg.place(x=-5, y=0)
    wlc5.resizable(False, False)

    #func
    def wlc5fn():
        wlc5.destroy()
        login.login()

    # button
    wlc5btnimg = ImageTk.PhotoImage(Image.open("./static/100pbtn.png"))
    wlc5btn = tkinter.Button(wlc5, image=wlc5btnimg, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",command=wlc5fn)
    wlc5btn.place(x=285, y=710)
    wlc5.mainloop()


if __name__=="__main__":

    wlc5()