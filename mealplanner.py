import tkinter

import tkinter.messagebox
from random import randint

import customtkinter as ctk
import pymongo
# from login import login
from PIL import ImageTk, Image
from customtkinter import *

import dashboard

protein = ['Yogurt(1 cup)', 'Cooked meat(3 Oz)', 'Cooked fish(4 Oz)', '1 whole egg + 4 egg whites', 'Tofu(5 Oz)']
fruit = ['Berries(80 Oz)', 'Apple', 'Orange', 'Banana', 'Dried Fruits(Handfull)', 'Fruit Juice(125ml)']
vegetable = ['Any vegetable(80g)']
grains = ['Cooked Grain(150g)', 'Whole Grain Bread(1 slice)', 'Half Large Potato(75g)', 'Oats(250g)',
          '2 corn tortillas']
ps = ['Soy nuts(i Oz)', 'Low fat milk(250ml)', 'Hummus(4 Tbsp)', 'Cottage cheese (125g)', 'Flavored yogurt(125g)']
taste_en = ['2 TSP (10 ml) olive oil', '2 TBSP (30g) reduced-calorie salad dressin', '1/4 medium avocado',
            'Small handful of nuts', '1/2 ounce  grated Parmesan cheese',
            '1 TBSP (20g) jam, jelly, honey, syrup, sugar']



import login

import os
from dotenv import load_dotenv
load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(
    mongodb_uri)
db = client['PYTHON_MPR']
col = db["mpr"]
# from login import login_btn_img,reg_btn_img
ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def mealplanner(email="shri@gmail.com"):
    mealplanner = CTk()
    mealplanner.title("Meal Planner")
    mealplanner.geometry(f"{375}x{812}+{800}+{100}")
    mealplannerimg = ctk.CTkImage(Image.open("./static/mealplanner.png"), size=(375, 812))
    bg_label = ctk.CTkLabel(mealplanner, text="", corner_radius=5, image=mealplannerimg)
    bg_label.place(x=0, y=0)
    mealplanner.resizable(False, False)
    cal=col.find_one({"email":email})["calorie"]

    print(cal)
    def getdiet(cal):
        if cal < 2200:

            breakfast = "Breakfast: " + protein[randint(0, 4)] + " \n" + fruit[randint(0, 4)]

            lunch = "Lunch: " + protein[randint(0, 4)] + "  \n" + vegetable[0] + " \nLeafy Greens" + grains[
                randint(0, 4)] + " \n" + taste_en[randint(0,4)] + " \n" + fruit[randint(0, 4)]

            snack = "Snack: " + ps[randint(0, 4)] + " \n" + vegetable[0]

            dinner = "Dinner: 2 " + protein[randint(0, 4)] + "\n" + vegetable[0] + " \nLeafy Greens" + grains[
                randint(0, 4)] + " \n" + taste_en[randint(0, 4)]

        elif cal >= 2200 and cal < 5500:

            breakfast = "Breakfast: " + protein[randint(0, 4)] + "\n" + fruit[randint(0, 4)]

            lunch = "Lunch: " + protein[randint(0, 4)] + "\n" + vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + "\n" + taste_en[randint(0, 4)] + "\n" + fruit[randint(0, 4)]

            snack = "Snack: " + ps[randint(0, 4)] + "\n" + vegetable[0]

            dinner = "Dinner: 2 " + protein[randint(0, 4)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + "\n" + taste_en[randint(0, 4)]


        elif cal >= 5500:

            breakfast = "Breakfast: 2 " + protein[randint(0, 5)] + " \n" + fruit[randint(0, 5)] + "  \n" + grains[
                randint(0, 4)]

            lunch = "Lunch: " + protein[randint(0, 5)] + "\n" + vegetable[0] + " + Leafy Greens" + grains[
                randint(0, 4)] + "\n" + taste_en[randint(0, 5)] + "\n" + fruit[randint(0, 5)]

            snack = "Snack: " + ps[randint(0, 4)] + "\n" + vegetable[0]

            dinner = "Dinner: 2 " + protein[randint(0, 5)] + " + 2 " + vegetable[0] + " \n+ Leafy Greens + 2 " + grains[
                randint(0, 4)] + " + \n2 " + taste_en[randint(0, 5)]
        ll=[breakfast, lunch, snack, dinner]
        dietmeals=""
        for item in ll:
            dietmeals=dietmeals+ "⭕ " +item+"\n \n "
        print(dietmeals)
        return dietmeals

    dietmeal=getdiet(cal)
    mealcontent = ctk.CTkLabel(mealplanner, text=dietmeal ,font=ctk.CTkFont(family="Poppins", size=16,weight="bold"), text_color="#1D1617",justify="left",fg_color="#aeceff",padx=10,pady=10,corner_radius=10,bg_color="#ffffff")
    mealcontent.place(relx=.5, rely=.5, anchor="center")
    def goback():
        mealplanner.destroy()
        dashboard.dashboard(email)

    back_img = ImageTk.PhotoImage(Image.open("./static/Back-Navs.png"), size=(32, 32))
    back_btn = tkinter.Button(mealplanner, image=back_img, borderwidth=0, activebackground="#ffffff",
                              background="#ffffff", highlightthickness=0, cursor="hand2", relief="flat", command=goback)
    back_btn.place(x=30, y=40)


    mealplanner.mainloop()


if __name__ == '__main__':
    mealplanner()