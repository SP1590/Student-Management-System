from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox 
import sqlite3

def Database():

    global conn,cursor
    #creating database
    conn=sqlite3.connect('studentrecord.db')
    cr=conn.cursor()

    #creating database
    cr.execute("create table if not exists cgc(RID integer primary key autoincrement not null,fname text,lname text,gender text,address text,contact text)")


#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("1100x500")
    #setting title for window
    display_screen.title("CGC Final Project")
    global tree
    global SEARCH
    global fname,lname,gender,address,contact
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="#15244C")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="#0B4670")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Student Management System", font=('verdana', 18), width=600,bg="cyan")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="First Name  ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Last Name ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(LFrom,gender,*content).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Address ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",font=("Arial", 10, "bold"),command=register,bg="#15244C",fg="white").pack(side=TOP, padx=10,pady=5, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter fname to Search", font=('verdana', 10),bg="orange")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg="cyan")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="cyan")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg="cyan")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #create update button
    btn_delete = Button(LeftViewForm, text="Update", command=Update,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", "Contact", "Email","Rollno","Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Student Id', text="Id")
    tree.heading('Name', text="FirstName")
    tree.heading('Contact', text="LastName")
    tree.heading('Email', text="Gender")
    tree.heading('Rollno', text="Address")
    tree.heading('Branch', text="Contact")
    #setting width of the columns
    #With the help of stretch record will not overlap to each other
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
#function to update data into database
def Update():
    Database()

    #getting data
    fn=fname.get()
    ln=lname.get()
    gd=gender.get()
    ad=address.get()
    ct=contact.get()

    #apply validation
    if fn=='' or ln=='' or gd=='' or ad=='' or ct=='':
        messagebox.showerror("Warning","Plz Fill All The Fileds")
    else:
        #getting selected data
        curitem=tree.focus() #is used to focus on current data on TreeView
        contents=(tree.item(curitem))
        selecteditem=contents['values'] #values means selected item

        #update Query
        conn.execute("update cgc set fname=?,lname=?,gender=?,address=?,contact=? where rid=?",(fn,ln,gd,ad,ct,selecteditem[0]))
        #if u want to some changes in database then must be used commit()
        conn.commit()
        messagebox.showinfo("Succssfully","Student Record Updated")

        #here reset the tkinter field
        Reset()

        #after updated display the data on TreeView
        DisplayData()
    
    
    
def register():
    Database()
    #getting data
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()

    #apply validation

    if fname1=='' or lname1=='' or gender1=='' or address1=='' or contact1=='':
        message.showerror("Warning","Please Fill All The Record")

    else:
        #? represent columns
        conn.execute("insert into cgc(fname,lname,gender,address,contact) values(?,?,?,?,?)",(fname1,lname1,gender1,address1,contact1))

        #if u want to some changes in database then must be used commit()
        conn.commit()
        messagebox.showinfo("Successfully","Student Record Inserted")
    
    
def Reset():
    Database()
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    address.set("")
    contact.set("")
    
    
def Delete():
    Database()

    if not tree.selection():
        messagebox.showwarning("Warning","Select data to delete")
    else:
        result=messagebox.askquestion("Confirm","Are you sure want to delete the record")

    if result=='yes':
        curitem=tree.focus()
        content=(tree.item(curitem))
        selecteditem=content['values']
        tree.delete(curitem)

        cr=conn.execute("delete from cgc where rid=%d" % selecteditem[0])

        conn.commit()
    
#function to search data
def SearchRecord():
    Database()

    #check field is empty or not
    if SEARCH.get=='':
        
        messagebox.showerror("Warning","Field is emplty")
    elif SEARCH.get !='':
        #clear all before show current record
        tree.delete(*tree.get_children())
        cr=conn.execute("select * from cgc where fname like ?",('%' +str(SEARCH.get()) + '%',))

        #fetch all related record
        fetch=cr.fetchall()

        for data in fetch:
            tree.insert('','end',values=(data))
    
#defining function to access data from SQLite database
def DisplayData():
    Database()
    #how to clear data
    '''
    the get_children() is a method Treeview return a list of every row id, it will iterating for get all related record
    '''
    tree.delete(*tree.get_children())
    #execute Query
    cr=conn.execute("select * from cgc")

    #fetch/get/reteive all data from the database
    
    fetch=cr.fetchall()

    #loop for dispaly all data from fetch
    for data in fetch:
        tree.insert('','end',values=(data))

    

#calling function
DisplayForm()
if __name__=='__main__':
    #Running Application
    mainloop()
