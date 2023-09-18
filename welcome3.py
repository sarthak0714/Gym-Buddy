import tkinter
import tkinter.messagebox

import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

import welcome4

# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def wlc3():
    wlc3 = CTk()
    wlc3.title("Home Page")
    wlc3.geometry(f"{375}x{812}+{800}+{100}")
    wlc3bgimg = ctk.CTkImage(Image.open("./static/wlc3.png"), size=(375, 812))
    wlc3_bg = ctk.CTkLabel(wlc3, text="", corner_radius=5, image=wlc3bgimg )
    wlc3_bg.place(x=-5, y=0)
    wlc3.resizable(False, False)

    def wlc3fn():
        wlc3.destroy()
        welcome4.wlc4()


    # button
    wlc3btnimg = ImageTk.PhotoImage(Image.open("./static/50p.png"))
    wlc3btn = tkinter.Button(wlc3, image=wlc3btnimg, borderwidth=0, activebackground="#ffffff",
                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",command=wlc3fn)
    wlc3btn.place(x=285, y=710)
    wlc3.mainloop()

if __name__ == "__main__":
    wlc3()