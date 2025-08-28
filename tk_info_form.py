import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

lst = ["diploma", "bachelor", "master", "doctoral"]


def only_numbers(text):
    return text.isdigit() 

def only_letters(text):
    return text.isalpha() or text.isspace() or text == ""


def enter():
    user_name = name.get().strip()
    user_last_name = last_name.get().strip()
    user_age = age.get().strip()
    user_dob = date_of_birth.get().strip()
    user_education = education.get()
    user_marital = pos.get()
    user_employment = pos2.get()
    user_phone = phone.get().strip()
    user_bio = bio_box.get("1.0", tk.END).strip()   
    
    if not user_name or not user_last_name or not user_phone or not user_dob:
        messagebox.showerror("Error ", "Please fill in necessary informations ! ")
        return
    
    messagebox.showinfo("Success ", "Information saved successfully .")
    
    for widget in frame_right.winfo_children():
        widget.destroy()
    
    tk.Label(frame_right, text="Your information : ", font=("bold", 12)).pack(anchor="w")
    tk.Label(frame_right, text=f"Name :  {user_name}").pack(anchor="w")
    tk.Label(frame_right, text=f"Last Name :  {user_last_name}").pack(anchor="w")
    tk.Label(frame_right, text=f"Age :  {user_age}").pack(anchor="w")
    tk.Label(frame_right, text=f"Date of Birth :  {user_dob}").pack(anchor="w")
    tk.Label(frame_right, text=f"Phone Number :  {user_phone}").pack(anchor="w")
    tk.Label(frame_right, text=f"Education :  {user_education}").pack(anchor="w")
    tk.Label(frame_right, text=f"Marital Status :  {user_marital}").pack(anchor="w")
    tk.Label(frame_right, text=f"Employment Status :  {user_employment}").pack(anchor="w")
    if user_bio:
        tk.Label(frame_right, text=f"Bio :  {user_bio}").pack(anchor="w")
    
    name.delete(0, tk.END)
    last_name.delete(0, tk.END)
    age.delete(0, tk.END)
    phone.delete(0, tk.END)
    date_of_birth.set_date("")
    education.set("select...")
    pos.set("nothing")
    pos2.set("nothing")
    bio_box.delete("1.0", tk.END)   
    name.focus()

win = tk.Tk()
win.geometry("800x650")  
win.title("Information Form")

frame_left = tk.Frame(win, width=400, height=600)
frame_left.pack(side="left", fill="both", expand=False)

frame_right = tk.Frame(win, width=400, height=600, bg="lightgray")
frame_right.pack(side="right", fill="both", expand=True)


only_num = win.register(only_numbers)
only_txt = win.register(only_letters)

title_name = tk.Label(frame_left, text='Name : ', font='bold')
title_name.place(x=124, y=50)
tk.Label(frame_left, text="*", fg="red").place(x=193, y=50) 
name = tk.Entry(frame_left, validate="key", validatecommand=(only_txt, "%P"))
name.place(x=205, y=50)

title_last_name = tk.Label(frame_left, text='Last Name : ', font='bold')
title_last_name.place(x=81, y=90)
tk.Label(frame_left, text="*", fg="red").place(x=193, y=90)  
last_name = tk.Entry(frame_left, validate="key", validatecommand=(only_txt, "%P"))
last_name.place(x=205, y=90)

title_phone = tk.Label(frame_left, text='Phone Number : ', font='bold')
title_phone.place(x=46, y=130)
tk.Label(frame_left, text="*", fg="red").place(x=193, y=130)  
phone = tk.Entry(frame_left, validate="key", validatecommand=(only_num, "%P"))
phone.place(x=205, y=130)

title_age = tk.Label(frame_left, text='Age : ', font='bold')
title_age.place(x=140, y=170)
age = tk.Entry(frame_left, validate="key", validatecommand=(only_num, "%P"))
age.place(x=205, y=170)

title_date_of_birth = tk.Label(frame_left, text='Date of Birth : ', font='bold')
title_date_of_birth.place(x=64, y=210)
tk.Label(frame_left, text="*", fg="red").place(x=193, y=210)  
date_of_birth = DateEntry(frame_left, date_pattern='dd/mm/yyyy')
date_of_birth.place(x=205, y=210)

education = ttk.Combobox(frame_left, values=lst)
education.place(x=205, y=250)
education.set('select...')
title_education = tk.Label(frame_left, text='Education : ', font='bold')
title_education.place(x=87, y=247)

title_marital_status = tk.Label(frame_left, text='Marital Status : ', font='bold')
title_marital_status.place(x=53, y=290)
pos = tk.StringVar()
marital_status = tk.Radiobutton(frame_left, text="Married", value='married', variable=pos)
marital_status2 = tk.Radiobutton(frame_left, text="Single", value='single', variable=pos)
pos.set('nothing')
marital_status.place(x=200, y=290)
marital_status2.place(x=280, y=290)

title_employment_status = tk.Label(frame_left, text='Employment Status : ', font='bold')
title_employment_status.place(x=6, y=330)
pos2 = tk.StringVar()
employment_status = tk.Radiobutton(frame_left, text="Employed", value='employed', variable=pos2)
employment_status2 = tk.Radiobutton(frame_left, text="Unemployed", value='unemployed', variable=pos2)
pos2.set('nothing')
employment_status.place(x=200, y=330)
employment_status2.place(x=280, y=330)

title_bio = tk.Label(frame_left, text="Bio : ", font='bold')
title_bio.place(x=80, y=370)
bio_box = tk.Text(frame_left, width=30, height=4)
bio_box.place(x=135, y=370)

enter_btn = tk.Button(frame_left, text="Save Information", command=enter, bg="green", fg="white")
enter_btn.place(x=150, y=470)

name.focus()
win.mainloop()
