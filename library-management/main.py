from MainMenu import *
from SearchBook import *
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

import pymysql
# Add your own database name and password here to reflect in the code
mypass = "Ironmanmark4"
mydatabase="libposnew"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Login")
root.geometry("600x480")

def calladmin():
    usern = username_box.get()
    passw = password_box.get()
    if usern == "" or passw == "":
        messagebox.showinfo("Error", "All fields are required")
    else:
        try:
            cur.execute("select * from admin where AdminID=%s and Password=%s", (usern, passw))
            op = cur.fetchone()
            # print(op)
            if op == None:
                messagebox.showinfo("Error", "Invalid Username or Password")
            else:
                root.destroy()
                mainmenu()


        except EXCEPTION as es:
            messagebox.showerror("Error"f"Error Due to: {str(es)}")


def callstudent():
    usern = username_box.get()
    passw = password_box.get()
    if usern == "" or passw == "":
        messagebox.showinfo("Error", "All fields are required")
    else:
        try:
            cur.execute("select * from student where Userid=%s and Password=%s", (usern, passw))
            op = cur.fetchone()
            # print(op)
            if op == None:
                messagebox.showinfo("Error", "Invalid Username or Password")
            else:
                root.destroy()
                SearchBook()


        except EXCEPTION as es:
            messagebox.showerror("Error"f"Error Due to: {str(es)}")


bg = ImageTk.PhotoImage(file="lib.jpg")
bg_image = Label(root, image=bg).grid()

del_frame = Frame(root, bd=4, relief=RIDGE, bg="#BBD8FF")
del_frame.place(x=100, y=60, width=400, height=180)

# Label for username and password
username = Label(del_frame, text="USERNAME", bg="#BBD8FF", fg="black", font=15)
username.grid(row=12, column=0, sticky=W, padx=10, pady=10)
password = Label(del_frame, text="PASSWORD", bg="#BBD8FF", fg="black", font=15)
password.grid(row=14, column=0, sticky=W, padx=10, pady=10)

# Text boxes for username and password
global username_box
username_box = Entry(del_frame, font=15, bd=5, relief=GROOVE)
username_box.grid(row=12, column=1, pady=10, padx=10, sticky="w")

global password_box
password_box = Entry(del_frame, font=15, bd=5, relief=GROOVE)
password_box.grid(row=14, column=1, pady=10, padx=10, sticky="w")

usern = username_box.get()
passw = password_box.get()

# Login Button for student and admin
adminlogin = Button(del_frame, text="Admin Login", bg="black", fg="black", font=15, command=calladmin)
adminlogin.grid(row=20, column=0, pady=10, padx=10)

studentlogin = Button(del_frame, text="Student Login", fg="black", font=15, command=callstudent)
studentlogin.grid(row=20, column=1, pady=10, padx=10)

root.mainloop()

