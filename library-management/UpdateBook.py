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

def update_book():
    update_book = Tk()
    update_book.title("Update Books")
    update_book.geometry("600x500")

    def edit_book():
        sql_c = """UPDATE book SET Description = %s, BookTitle = %s, Category = %s, AuthorName = %s, Publication = 
        %s, BookPrice = %s WHERE ISBN = %s """
        Description = e11.get()
        Title = e22.get()
        Category = e33.get()
        AuthorName = e44.get()
        Publication = e55.get()
        Price = e66.get()
        ISBN = e77.get()

        input = (Description, Title, Category, AuthorName, Publication, Price, ISBN)
        cur.execute(sql_c, input)

        con.commit()
        messagebox.showinfo("Record Updated!!")
        update_book.destroy()

    def search_up():
        search_edit = search_box.get()
        sqlcommand = "SELECT * FROM book WHERE ISBN = %s"
        name = (search_edit,)
        result2 = cur.execute(sqlcommand, name)
        result2 = cur.fetchall()

        if not result2:
            messagebox.showinfo("No Results")
        else:
            # print(result2)
            for x in result2:
                isbn = x[6]

            # result_label = Label(update_book, text=result2)
            # result_label.grid(row=2, column=0, padx=10)
            #
            # edit_button = Button(update_book, text="Edit")
            # edit_button.grid(row=3, column=0)

        bookDescription = Label(update_book, text="Description", width=20, height=2).grid(row=12, column=0, sticky=W)
        bookTitle = Label(update_book, text="Title", width=20, height=2).grid(row=13, column=0, sticky=W)
        bookCategory = Label(update_book, text="Category", width=20, height=2).grid(row=14, column=0, sticky=W)
        bookAuthorName = Label(update_book, text="Author Name", width=20, height=2).grid(row=15, column=0, sticky=W)
        bookPublication = Label(update_book, text="Publication", width=20, height=2).grid(row=16, column=0, sticky=W)
        bookPrice = Label(update_book, text="Price", width=20, height=2).grid(row=17, column=0, sticky=W)
        bookIsbn = Label(update_book, text="ISBN", width=20, height=2).grid(row=18, column=0, sticky=W)

        global e11
        e11 = Entry(update_book, width=30, borderwidth=2)
        e11.grid(row=12, column=1)
        e11.insert(0, result2[0][0])
        global e22
        e22 = Entry(update_book, width=30, borderwidth=2)
        e22.grid(row=13, column=1)
        e22.insert(0, result2[0][1])
        global e33
        e33 = Entry(update_book, width=30, borderwidth=2)
        e33.grid(row=14, column=1)
        e33.insert(0, result2[0][2])
        global e44
        e44 = Entry(update_book, width=30, borderwidth=2)
        e44.grid(row=15, column=1)
        e44.insert(0, result2[0][3])
        global e55
        e55 = Entry(update_book, width=30, borderwidth=2)
        e55.grid(row=16, column=1)
        e55.insert(0, result2[0][4])
        global e66
        e66 = Entry(update_book, width=30, borderwidth=2)
        e66.grid(row=17, column=1)
        e66.insert(0, result2[0][5])
        global e77
        e77 = Entry(update_book, width=30, borderwidth=2)
        e77.grid(row=18, column=1)
        e77.insert(0, result2[0][6])

        submit_button = Button(update_book, text="Submit", command=edit_book)
        submit_button.grid(row=20, column=0)

    def clear_fields():
        e11.delete(0, END)
        e22.delete(0, END)
        e33.delete(0, END)
        e44.delete(0, END)
        e55.delete(0, END)
        e66.delete(0, END)
        e77.delete(0, END)

    search_box = Entry(update_book)
    search_box.grid(row=0, column=1, padx=10, pady=10)

    search_box_label = Label(update_book, text="Search books to update using ISBN")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    search_up_button = Button(update_book, text="Search", command=search_up)
    search_up_button.grid(row=1, column=0, padx=10)

    # button
    quitBtn = Button(update_book, text="CLEAR", bg='#f7f1e3', fg='black', command=clear_fields)
    quitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(update_book, text="QUIT", bg='#f7f1e3', fg='black', command=update_book.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    update_book.mainloop()