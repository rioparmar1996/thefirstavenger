from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():

    bookDescription = bookInfo6.get()
    bookTitle = bookInfo2.get()
    bookCategory = bookInfo4.get()
    bookAuthorName = bookInfo3.get()
    bookPublication = bookInfo5.get()
    bookPrice = bookInfo7.get()
    bookISBN = bookInfo1.get()

    if bookDescription != "" and bookTitle != "" and bookCategory != "" and bookAuthorName != "" and bookPublication != "" and bookPrice != "" and bookISBN != "":
        insert_Data = "Insert into Book (Description,BookTitle,Category,AuthorName,Publication,BookPrice,ISBN) value (%s,%s,%s,%s,%s,%s,%s)"
        value = (bookDescription, bookTitle, bookCategory, bookAuthorName, bookPublication, bookPrice, bookISBN)
        cur.execute(insert_Data, value)
        con.commit()
        messagebox.showinfo("Info", "Record Inserted")
    else:
        messagebox.showinfo("Info", "Enter Valid Records")
    
    print(bookDescription)
    print(bookTitle)
    print(bookCategory)
    print(bookAuthorName)
    print(bookPublication)
    print(bookPrice)
    print(bookISBN)


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,bookInfo7,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Ironmanmark4"
    mydatabase = "libposnew"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#F8F9F9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#F8F9F9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD A BOOK",bg='#F8F9F9', fg='black', font=15)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#F8F9F9')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ISBN
    lb1 = Label(labelFrame,text="Book ISBN : ",bg='#F8F9F9', fg='black')
    lb1.place(relx=0.05,rely=0.02, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.02, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ",bg='#F8F9F9', fg='black')
    lb2.place(relx=0.05,rely=0.15, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.15, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ",bg='#F8F9F9', fg='black')
    lb3.place(relx=0.05,rely=0.30, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.30, relwidth=0.62, relheight=0.08)
        
    # Book Category
    lb4 = Label(labelFrame,text="Category",bg='#F8F9F9', fg='black')
    lb4.place(relx=0.05,rely=0.45, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # Book Publication
    lb5 = Label(labelFrame, text="Publication",bg='#F8F9F9', fg='black')
    lb5.place(relx=0.05, rely=0.60, relheight=0.08)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3, rely=0.60, relwidth=0.62, relheight=0.08)

    # Book Descriptions
    lb6 = Label(labelFrame, text="Description: ",bg='#F8F9F9', fg='black')
    lb6.place(relx=0.05, rely=0.75, relheight=0.08)

    bookInfo6= Entry(labelFrame)
    bookInfo6.place(relx=0.3, rely=0.75, relwidth=0.62, relheight=0.08)

    # Book Prize
    lb7 = Label(labelFrame, text="Price: ",bg='#F8F9F9', fg='black')
    lb7.place(relx=0.05, rely=0.90, relheight=0.08)

    bookInfo7 = Entry(labelFrame)
    bookInfo7.place(relx=0.3, rely=0.90, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#82E0AA', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#EC7063', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()