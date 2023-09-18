import tkinter
import tkinter.messagebox

import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

import welcome3

# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def wlc2():
    wlc2 = CTk()
    wlc2.title("Home Page")
    wlc2.geometry(f"{375}x{812}+{800}+{100}")
    wlc2bgimg = ctk.CTkImage(Image.open("./static/wlc2.png"), size=(375, 812))
    wlc2_bg = ctk.CTkLabel(wlc2, text="", corner_radius=5, image=wlc2bgimg )
    wlc2_bg.place(x=-5, y=0)
    wlc2.resizable(False, False)

    #func
    def welc2fn():
        wlc2.destroy()
        welcome3.wlc3()

    # button
    wlc2btnimg = ImageTk.PhotoImage(Image.open("./static/25pbtn.png"))
    wlc2btn = tkinter.Button(wlc2, image=wlc2btnimg, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",command=welc2fn)
    wlc2btn.place(x=285, y=710)
    wlc2.mainloop()


if __name__=="__main__":
    wlc2()