import tkinter
import tkinter.messagebox

import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def workout_done():
    # create root frame for login1
    login1 = CTk()
    login1.title("FitnessX")
    login1.geometry(f"{375}x{812}+{50}+{80}")
    loginbg = ctk.CTkImage(Image.open("static/Congratulations_Page.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(login1, text="", corner_radius=5, image=loginbg,fg_color="#FFFFFF")
    bg_label.place(x=-1, y=0)
    b1_img = ctk.CTkImage(Image.open("./static/workout_done_button.png"),size=(359,104))
    b1 = ctk.CTkButton(login1, image=b1_img, fg_color="#FFFFFF",text="",hover=False,command=lambda: ctk.set_appearance_mode('dark'))
    b1.place(x=0, y=675)
    login1.resizable(False, False)
    login1.mainloop()


