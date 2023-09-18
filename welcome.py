import tkinter
import tkinter.messagebox

import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

import welcome2

# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def wlc():
    wlc = CTk()
    wlc.title("Home Page")
    wlc.geometry(f"{375}x{812}+{800}+{100}")
    wlcbgimg = ctk.CTkImage(Image.open("./static/welcome.png"), size=(375, 812))
    wlc_bg = ctk.CTkLabel(wlc, text="", corner_radius=5, image=wlcbgimg, )
    wlc_bg.place(x=-5, y=0)
    wlc.resizable(False, False)

    # function
    def welc1():
        wlc.destroy()
        welcome2.wlc2()

    # button
    getstrtedbtnimg = ImageTk.PhotoImage(Image.open("./static/homebtn.png"))
    getstarted = tkinter.Button(wlc, image=getstrtedbtnimg, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
                                command=welc1)
    getstarted.place(x=10, y=682)
    wlc.mainloop()


if __name__ == "__main__":
    wlc()
