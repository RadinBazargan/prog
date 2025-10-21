import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pymysql

lst = ["diploma", "bachelor", "master", "doctoral"]

def only_numbers(text):
    return text.isdigit()

def only_letters(text):
    return text.isalpha() or text.isspace() or text == ""

class Form:
    def __init__(self, root):
        self.root = root
        self.root.title("Information Form")
        self.root.geometry("800x650")

        self.only_num = root.register(only_numbers)
        self.only_txt = root.register(only_letters)

        self.JSON_FILE = r"data.json"

        self.create_form()
        self.form_frame.pack()

        self.btn_show = tk.Button(self.root, text="Show JSON File", command=self.show_json)
        self.text_box = tk.Text(self.root, wrap="word", height=15)

        self.create_login_form()

    def create_form(self):
        self.form_frame = tk.Frame(self.root)
        frm = self.form_frame

        tk.Label(frm, text='Name : ', font='bold').grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(frm, text="*", fg="red").grid(row=0, column=1, sticky="w", padx=7, pady=5)
        self.name = tk.Entry(frm, width=30, validate="key", validatecommand=(self.only_txt, "%P"))
        self.name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frm, text='Last Name : ', font='bold').grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(frm, text="*", fg="red").grid(row=1, column=1, sticky="w", padx=7, pady=5)
        self.last_name = tk.Entry(frm, width=30, validate="key", validatecommand=(self.only_txt, "%P"))
        self.last_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frm, text='Age : ', font='bold').grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.age = tk.Entry(frm, width=30, validate="key", validatecommand=(self.only_num, "%P"))
        self.age.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frm, text='Phone : ', font='bold').grid(row=3, column=0, sticky="w", padx=5, pady=5)
        tk.Label(frm, text="*", fg="red").grid(row=3, column=1, sticky="w", padx=7, pady=5)
        self.phone = tk.Entry(frm, width=30, validate="key", validatecommand=(self.only_num, "%P"))
        self.phone.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frm, text='Marital Status : ', font='bold').grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.pos = tk.StringVar(value='nothing')
        tk.Radiobutton(frm, text="Married", value='married', variable=self.pos).grid(row=4, column=1, sticky="w")
        tk.Radiobutton(frm, text="Single", value='single', variable=self.pos).grid(row=4, column=1)

        tk.Label(frm, text='Employment Status : ', font='bold').grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.pos2 = tk.StringVar(value='nothing')
        tk.Radiobutton(frm, text="Employed", value='employed', variable=self.pos2).grid(row=5, column=1, sticky="w")
        tk.Radiobutton(frm, text="Unemployed", value='unemployed', variable=self.pos2).grid(row=5, column=1)

        tk.Label(frm, text='Date of Birth : ', font='bold').grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.date_of_birth = DateEntry(frm, date_pattern='dd/mm/yyyy')
        self.date_of_birth.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(frm, text='Education : ', font='bold').grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.education = ttk.Combobox(frm, values=lst)
        self.education.grid(row=7, column=1, padx=5, pady=5)
        self.education.set('select...')

        tk.Label(frm, text="Bio : ", font='bold').grid(row=8, column=0, sticky="nw", padx=5, pady=5)
        self.bio_box = tk.Text(frm, width=30, height=4)
        self.bio_box.grid(row=8, column=1, padx=5, pady=5)

        self.enter_btn = tk.Button(frm, text="Save Information", command=self.save_info, bg="green", fg="white")
        self.enter_btn.grid(row=9, column=0, pady=10)

        self.login_btn = tk.Button(frm, text="login", command=self.show_login, bg="black", fg="white")
        self.login_btn.grid(row=9, column=1, pady=10)

    def create_login_form(self):
        self.login_frame = tk.Frame(self.root)
        frm = self.login_frame

        tk.Label(frm, text='User Name : ', font='bold').grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.user = tk.Entry(frm, width=30)
        self.user.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frm, text='Password : ', font='bold').grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.passwd = tk.Entry(frm, width=30, show="*")
        self.passwd.grid(row=1, column=1, padx=5, pady=5)

        self.ok_btn = tk.Button(frm, text="Login", command=self.check, bg="green", fg="white")
        self.ok_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def show_login(self):
        self.form_frame.pack_forget()
        self.login_frame.pack()

    def connection(self):
        return pymysql.connect(host="localhost", user="root", password="", database="form")

    def save_info(self):
        try:
            name = self.name.get().strip()
            last_name = self.last_name.get().strip()
            age = self.age.get().strip()
            phone = self.phone.get().strip()
            marital_status = self.pos.get()
            employment_status = self.pos2.get()
            bio = self.bio_box.get("1.0", tk.END).strip()
            date_of_birth = self.date_of_birth.get_date()
            education = self.education.get()

            if not name or not last_name or not phone:
                messagebox.showwarning("Warning", "Please fill necessary fields")
                return

            data = {
                "Name": name,
                "Last name": last_name,
                "Age": age,
                "Phone number": phone,
                "Marital status": marital_status,
                "Employment status": employment_status,
                "Bio": bio,
                "Date of birth": str(date_of_birth),
                "Education": education
            }
            with open(self.JSON_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            conn = self.connection()
            cursor = conn.cursor()
            sql = """INSERT INTO info (name, last_name, age, phone, marital_status, employment_status, bio, date_of_birth, education )
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (name, last_name, age, phone, marital_status, employment_status, bio, date_of_birth, education))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Information saved successfully!")
        except:
            messagebox.showerror("Error", "Something went wrong")

    def show_json(self):
        try:
            with open(self.JSON_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, json.dumps(data, indent=4, ensure_ascii=False))
        except :
            messagebox.showerror("Error", "Something went wrong")

    def check(self):
        user_name = self.user.get().strip()
        passwd = self.passwd.get().strip()
        try:
            con = self.connection()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM info WHERE name=%s AND phone=%s", (user_name, passwd))
            result = cursor.fetchone()
            cursor.close()
            con.close()

            if result:
                messagebox.showinfo("Success", "Login was successful")

                data = { "Name": result[0],
                "Last name": result[1],
                "Age": result[2],
                "Phone number": result[3],
                "Marital status": result[4],
                "Employment status": result[5],
                "Bio": result[6],
                "Date of birth": str(result[7]),
                "Education": result[8]
                }
                with open(self.JSON_FILE, "w", encoding="utf-8") as f:
                 json.dump(data, f, indent=4, ensure_ascii=False)
                
                self.login_frame.pack_forget()
                self.btn_show.pack(pady=10)
                self.text_box.pack(expand=True, fill="both", padx=10, pady=10)
            else:
                messagebox.showerror("Unsuccessful", "Login was unsuccessful")
        except :
            messagebox.showerror("Error","Database connection failed")

if __name__ == "__main__":
    win = tk.Tk()
    app = Form(win)
    win.mainloop()


