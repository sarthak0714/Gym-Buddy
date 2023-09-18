import tkinter
import tkinter.messagebox
import customtkinter as ctk

import register
from register import *
from PIL import ImageTk, Image

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def login():
    # background
    m=ctk.CTk()
    m.geometry(f"{375}x{812}")
    imagestore = ctk.CTkImage(Image.open("./static/loginpage1.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(text="", corner_radius=5, image=imagestore)
    bg_label.place(x=0, y=0)
#
#     # textbox
#     email_txt = ctk.CTkEntry(border_width=1.5, border_color="#94a8fe",
#                                        placeholder_text="Email", width=315, height=48, corner_radius=30,
#                                        bg_color="#ffffff")
#     email_txt.place(x=38, y=129)
#     password_txt = ctk.CTkEntry(border_width=1.5, border_color="#94a8fe",
#                                           placeholder_text="Password", width=315, height=48, corner_radius=30,
#                                           bg_color="#ffffff", show='*')
#     password_txt.place(x=38, y=192)
#
#     # chkbox
#     chk_box = ctk.CTkCheckBox(width=16, height=16, text=None, border_width=1.5,
#                                         border_color="#94a8fe",
#                                         corner_radius=30, bg_color="#ffffff")
#     chk_box.place(x=30, y=250)
#
#     # buttons
#     reg_btn_img = ImageTk.PhotoImage(Image.open("./static/regb.png"), size=(315, 60))
#     reg_btn = tkinter.Button(image=reg_btn_img, borderwidth=0, activebackground="#ffffff",
#                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised",
#                              command=registerfn)
#     reg_btn.place(x=10, y=651)
#
#     login_btn_img = ImageTk.PhotoImage(Image.open("./static/loginb.png"), size=(315, 60))
#     login_btn = tkinter.Button(image=login_btn_img, borderwidth=0, activebackground="#ffffff",
#                                background="#ffffff", highlightthickness=0, cursor="hand2", relief="raised")
#     login_btn.place(x=10, y=513)
#
#         # show password func
#     def showpass():
#         if password_txt.cget("show") == "*":
#             password_txt.configure(show="")
#
#         else:
#             password_txt.configure(show="*")
#
# def registerfn():
#
#     rapp=register.rApp()
#     rapp.mainloop()

login()