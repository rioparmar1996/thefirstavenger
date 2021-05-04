from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Ironmanmark4"
mydatabase = "libposnew"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()


def showAll():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)

        def CreateUI(self):
            tv = Treeview(self)
            tv['columns'] = ('Description', 'Title', 'Category', 'AuthorName', 'Publication', 'Price', 'Isbn')
            tv.heading('#0', text='Description', anchor='center')
            tv.column('#0', anchor='center')
            tv.heading('#1', text='Title', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='Category', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='AuthorName', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='Publication', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='Price', anchor='center')
            tv.column('#5', anchor='center')
            tv.heading('#6', text='Isbn', anchor='center')
            tv.column('#6', anchor='center')
            tv.grid(sticky=(N, S, W, E))
            self.treeview = tv
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        def LoadTable(self):
            Select = "Select * from Book"
            cur.execute(Select)
            result = cur.fetchall()
            Description = ""
            Title = ""
            Category = ""
            AuthorName = ""
            Publication = ""
            Price = ""
            ISBN = ""
            for i in result:
                Description = i[0]
                Title = i[1]
                Category = i[2]
                AuthorName = i[3]
                Publication = i[4]
                Price = i[5]
                Isbn = i[6]
                self.treeview.insert("", 'end', text=Description,
                                     values=(Title, Category, AuthorName, Publication, Price, Isbn))

    root = Tk()
    root.title("Overview Page")
    A(root)
