import tkinter
import tkinter.messagebox

import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

import welcome5

# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def wlc4():
    wlc4 = CTk()
    wlc4.title("Home Page")
    wlc4.geometry(f"{375}x{812}+{800}+{100}")
    wlc4bgimg = ctk.CTkImage(Image.open("./static/wlc4.png"), size=(375, 812))
    wlc4_bg = ctk.CTkLabel(wlc4, text="", corner_radius=5, image=wlc4bgimg )
    wlc4_bg.place(x=-5, y=0)
    wlc4.resizable(False, False)

    ##fn
    def wlc4fn():
        wlc4.destroy()
        welcome5.wlc5()

    # button
    wlc4btnimg = ImageTk.PhotoImage(Image.open("./static/75pbtn.png"))
    wlc4btn = tkinter.Button(wlc4, image=wlc4btnimg, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",command=wlc4fn)
    wlc4btn.place(x=285, y=710)
    wlc4.mainloop()
if __name__=="__main__":

    wlc4()