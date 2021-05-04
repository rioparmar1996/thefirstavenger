from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Ironmanmark4"
mydatabase = "libposnew"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()



def SearchBook():
    search_books = Tk()
    search_books.title("Search Books")
    search_books.geometry("600x500")

    def search_b():

        selected = drop_menu.get()
        sql = ""
        if selected == "...":
            messagebox.showinfo("ERROR!! No Option Selected")
        if selected == "ISBN":
            sql = "SELECT * FROM book where ISBN = %s"
        if selected == "Book Name":
            sql = "SELECT * FROM book where BookTitle = %s"
        if selected == "Author Name":
            sql = "SELECT * FROM book where AuthorName = %s"

        searched = search_box.get()
        # sql = "SELECT * FROM book WHERE ISBN = %s"
        book = (searched,)
        result = cur.execute(sql, book)
        result = cur.fetchall()

        if not result:
            messagebox.showinfo("Sorry No Books found")
        else:
            bookDescription = Label(search_books, text="Description", width=20, height=2).grid(row=8, column=0,
                                                                                               sticky=E)
            bookTitle = Label(search_books, text="Title", width=20, height=2).grid(row=9, column=0)
            bookCategory = Label(search_books, text="Category", width=20, height=2).grid(row=10, column=0)
            bookAuthorName = Label(search_books, text="Author Name", width=20, height=2).grid(row=11, column=0)
            bookPublication = Label(search_books, text="Publication", width=20, height=2).grid(row=12, column=0)
            bookPrice = Label(search_books, text="Price", width=20, height=2).grid(row=13, column=0)
            bookIsbn = Label(search_books, text="ISBN", width=20, height=2).grid(row=14, column=0)

            global e1
            e1 = Entry(search_books, width=30, borderwidth=2)
            e1.grid(row=8, column=1)
            global e2
            e2 = Entry(search_books, width=30, borderwidth=2)
            e2.grid(row=9, column=1)
            global e3
            e3 = Entry(search_books, width=30, borderwidth=2)
            e3.grid(row=10, column=1)
            global e4
            e4 = Entry(search_books, width=30, borderwidth=2)
            e4.grid(row=11, column=1)
            global e5
            e5 = Entry(search_books, width=30, borderwidth=2)
            e5.grid(row=12, column=1)
            global e6
            e6 = Entry(search_books, width=30, borderwidth=2)
            e6.grid(row=13, column=1)
            global e7
            e7 = Entry(search_books, width=30, borderwidth=2)
            e7.grid(row=14, column=1)

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
                ISBN = i[6]
            e1.insert(0, Description)
            e2.insert(0, Title)
            e3.insert(0, Category)
            e4.insert(0, AuthorName)
            e5.insert(0, Publication)
            e6.insert(0, Price)
            e7.insert(0, ISBN)


    def clear_fields():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)

    # Entry box
    search_box = Entry(search_books)
    search_box.grid(row=0, column=1, padx=10, pady=10)

    search_label = Label(search_books, text="Search books ")
    search_label.grid(row=0, column=0, padx=10, pady=10)

    search_button = Button(search_books, text="Search books", command=search_b)
    search_button.grid(row=1, column=0, padx=10)

    # Drop-down Menu for search
    drop_menu = ttk.Combobox(search_books, value=["...", "ISBN", "Book Name", "Author Name"])
    drop_menu.current(0)
    drop_menu.grid(row=0, column=2)

    #button
    quitBtn = Button(search_books, text="CLEAR", bg='#f7f1e3', fg='black', command=clear_fields)
    quitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(search_books, text="QUIT", bg='#f7f1e3', fg='black', command=search_books.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    search_books.mainloop()