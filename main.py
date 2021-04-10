from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="libposnew"
)
mycursor = mydb.cursor()

root = Tk()
root.title("Infosec")
root.geometry("700x600")
theLabel = Label(root, text="LIBRARY MANAGEMENT")

bookDescription = Label(root, text="Description", width=20, height=2, bg="#a2cffe").grid(row=0, column=0, sticky=E)
bookTitle = Label(root, text="Title", width=20, height=2, bg="#a2cffe").grid(row=1, column=0)
bookCategory = Label(root, text="Category", width=20, height=2, bg="#a2cffe").grid(row=2, column=0)
bookAuthorName = Label(root, text="Author Name", width=20, height=2, bg="#a2cffe").grid(row=3, column=0)
bookPublication = Label(root, text="Publication", width=20, height=2, bg="#a2cffe").grid(row=4, column=0)
bookPrice = Label(root, text="Price", width=20, height=2, bg="#a2cffe").grid(row=5, column=0)
bookIsbn = Label(root, text="ISBN", width=20, height=2, bg="#54FA9B").grid(row=6, column=0)

e1 = Entry(root, width=30, borderwidth=2)
e1.grid(row=0, column=1)
e2 = Entry(root, width=30, borderwidth=2)
e2.grid(row=1, column=1)
e3 = Entry(root, width=30, borderwidth=2)
e3.grid(row=2, column=1)
e4 = Entry(root, width=30, borderwidth=2)
e4.grid(row=3, column=1)
e5 = Entry(root, width=30, borderwidth=2)
e5.grid(row=4, column=1)
e6 = Entry(root, width=30, borderwidth=2)
e6.grid(row=5, column=1)
e7 = Entry(root, width=30, borderwidth=2)
e7.grid(row=6, column=1)


def insertData():
    Description = e1.get()
    BookTitle = e2.get()
    Category = e3.get()
    AuthorName = e4.get()
    Publication = e5.get()
    BookPrice = e6.get()
    ISBN = e7.get()
    if Description != "" and ISBN != "" and BookTitle != "" and Category != "" and AuthorName != "" and Publication != "" and BookPrice != "":
        insert_Data = "Insert into Book (Description,BookTitle,Category,AuthorName,Publication,BookPrice,ISBN) value (%s,%s,%s,%s,%s,%s,%s)"
        value = (Description, BookTitle, Category, AuthorName, Publication, BookPrice, ISBN)
        mycursor.execute(insert_Data, value)
        mydb.commit()
        messagebox.showinfo("Info", "Record Inserted")
    else:
        messagebox.showinfo("Info", "Enter Valid Records")


def updateData():
    ISBN = e7.get()
    dbIsbn = ""
    Select = "Select * from Book where ISBN='%s'" % (ISBN)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    for i in result:
        ISBN = i[0]
        if (ISBN != dbIsbn):
            messagebox.askyesno("Information", "Record updated")
            Description = e1.get()
            BookTitle = e2.get()
            Category = e3.get()
            AuthorName = e4.get()
            Publication = e5.get()
            BookPrice = e6.get()
            Isbn = e7.get()
            update_Data = "Update Book set Description,BookTitle,Category,AuthorName,Publication,BookPrice where ISBN " \
                          "='%s'" % (Description, BookTitle, Category, AuthorName, Publication, BookPrice, Isbn)
            mycursor.execute(update_Data)
            mydb.commit()
            messagebox.showinfo("Info", "Record Updated")
        else:
            messagebox.askyesno("Information", "Record Doesn't exists")
            insertData()
            clearData()


def deleteData():
    ISBN = e7.get()
    delete = "Delete from Book where ISBN = '%s'" % (ISBN)
    mycursor.execute(delete)
    mydb.commit()
    messagebox.showinfo("Information", "Record Deleted")
    clearData()


def showRecord():
    ISBN = e7.get()
    dbISBN = ""
    Select = "Select ISBN from Book where ISBN ='%s'" % (ISBN)
    mycursor.execute(Select)
    result1 = mycursor.fetchall()
    for i in result1:
        dbISBN = i[0]
        Select1 = "Select Description,BookTitle,Category,AuthorName,Publication,BookPrice from Book where ISBN ='%s'" % (
            ISBN)
        mycursor.execute(Select1)
        result2 = mycursor.fetchall()
        Description = ""
        Title = ""
        Category = ""
        AuthorName = ""
        Publication = ""
        Price = ""
        ISBN = ""
        for i in result2:
            Description = i[0]
            Title = i[1]
            Category = i[2]
            AuthorName = i[3]
            Publication = i[4]
            Price = i[5]
        e1.insert(0, Description)
        e2.insert(0, Title)
        e3.insert(0, Category)
        e4.insert(0, AuthorName)
        e5.insert(0, Publication)
        e6.insert(0, Price)


def showAllRecord():
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
            mycursor.execute(Select)
            result = mycursor.fetchall()
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


def clearData():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)


button1 = Button(root, text="Insert", width=10, height=2, command=insertData).grid(row=0, column=3)
button2 = Button(root, text="Update", width=10, height=2, command=updateData).grid(row=1, column=3)
button3 = Button(root, text="Delete", width=10, height=2, command=deleteData).grid(row=2, column=3)
button4 = Button(root, text="Show Record", width=10, height=2, command=showRecord).grid(row=3, column=3)
button5 = Button(root, text="Show All", width=10, height=2, command=showAllRecord).grid(row=4, column=3)
button6 = Button(root, text="Clear", width=10, height=2, command=clearData).grid(row=6, column=3)


root.mainloop()
