from os import error
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
import sqlite3

connection = sqlite3.connect("passwords.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE if not exists Password (
    Id integer,
    Website text,
    Password text
    )""")


root = Tk()
root.title("Password Manager")
root.state("zoomed")

# Defining the frame
login_frame = Frame(root, bg="#FFF280", width=1920, height=1080)
textbox_frame = Frame(root, bg="#FFF280", width=1920, height=1080)

# Looping Frames
for frame in (login_frame, textbox_frame):
    frame.grid(row=0, column=0)

login_frame.tkraise()

# Style
style = Style(root)
style.layout("Treeview", [('Treeview', {'sticky': 'nswe'})])
style.configure("Treeview", background="#FFF280", fieldbackground="#FFF280", rowheight=34)
style.configure("Treeview", font=('Poppins', 16))
style.configure("Treeview.Heading", font=('Poppins'))
style.map("Treeview", background=[("selected", "#E37059")])

# Widgets inside the login_frame
Login = Label(login_frame, text="Login.", highlightthickness=0, font=("poppins", 40), bg="#FF6565", )
Name = Label(login_frame, text="Name", highlightthickness=0, font=("poppins", 22), bg="#FFF280")
Password = Label(login_frame, text="Password", highlightthickness=0, font=("poppins", 22), bg="#FFF280")

# Function for swapping frames
def swap(frame):
    frame.tkraise()
    text_variable = name_string.get()
    Welcome.config(text=text_variable)
connection.commit()

# Images for textbox_frame 
general_rect = PhotoImage(file="./namerect.png")

add_button_image = PhotoImage(file="./addbutton.png")
delete_button_image = PhotoImage(file="./deletebutton.png")

# Hover Images for textbox_frame 
add_button_image_hover = PhotoImage(file="./addbuttonhover.png")
delete_button_image_hover = PhotoImage(file="./deletebuttonhover.png")


# Hover buttons for textbox_frame
def hover_add(e):
    add_button.configure(image=add_button_image_hover)
def hover_delete(e):
    delete_button.configure(image=delete_button_image_hover)

def hover_add_leave(e):
    add_button.configure(image=add_button_image)
def hover_delete_leave(e):
    delete_button.configure(image=delete_button_image)



# Strings from entry box
add_name_string = StringVar()
add_name2_string = StringVar()
delete_name_string = IntVar()


# Labels for rectangle entries
add_name_label = Label(textbox_frame, highlightthickness=0, bg="#FFF280", image=general_rect)
add_name2_label = Label(textbox_frame, highlightthickness=0, bg="#FFF280", image=general_rect)
delete_name_label = Label(textbox_frame, highlightthickness=0, bg="#FFF280", image=general_rect)


# Entry widgets for textbox_frame
add_name_entry = Entry(textbox_frame, bd=0, bg="#FFF280", font="poppins 16", fg="#707070", width=25, insertbackground="#121212", selectbackground="#121212", textvariable=add_name_string)
add_name2_entry = Entry(textbox_frame, bd=0, bg="#FFF280", font="poppins 16", fg="#707070", width=25, insertbackground="#121212", selectbackground="#121212", textvariable=add_name2_string)
delete_name_entry = Entry(textbox_frame, bd=0, bg="#FFF280", font="poppins 16", fg="#707070", width=25, insertbackground="#121212", selectbackground="#121212", textvariable=delete_name_string)

# Entry widget functions on bind
def add_name_clear(e):
    add_name_entry.delete(0, END)
def add_name2_clear(e):
    add_name2_entry.delete(0, END)
def delete_name_clear(e):
    delete_name_entry.delete(0, END)

def delete_name_clear_first_without_0():
    delete_name_entry.delete(0, END)
delete_name_clear_first_without_0()

# Binding Entry widgets in textbox frame
add_name_entry.bind("<Button-1>", add_name_clear)
add_name2_entry.bind("<Button-1>", add_name2_clear)
delete_name_entry.bind("<Button-1>", delete_name_clear)

# Inserting values to entry box 
add_name_entry.insert(0, "Website Name")
add_name2_entry.insert(0, "Website Password")
delete_name_entry.insert(1, "Website Id")


#Placing the labels
add_name_label.place(relx=0.05, rely=0.2)
add_name2_label.place(relx=0.05, rely=0.27)
delete_name_label.place(relx=0.05, rely=0.425)

# Placing entry widgets in textbox_frame
add_name_entry.place(relx=0.055, rely=0.213)
add_name2_entry.place(relx=0.055, rely=0.283)
delete_name_entry.place(relx=0.055, rely=0.438)

# Widgets inside the treeview_frame
global treeview
treeview = Treeview(textbox_frame, height=25)


# Treeview widget settings
treeview["columns"] = ("ID", "Website", "Password")
treeview["show"] = "headings"
treeview.column("ID", anchor=CENTER, width=80)
treeview.column("Website", anchor=CENTER, width=400)
treeview.column("Password", anchor=W, width=400)

treeview.heading("ID", text="ID", anchor=CENTER)    
treeview.heading("Website", text="Website", anchor=CENTER)
treeview.heading("Password", text="Password", anchor=CENTER)

treeviewscrollbar = Scrollbar(textbox_frame, orient="vertical", command=treeview.yview)
treeviewscrollbar.place(relx=0.98, rely=0.1, relheight=0.75, relwidth=0.011)
treeview.configure(yscrollcommand=treeviewscrollbar.set)


treeview.place(relx=0.52, rely=0.1)

def trying():
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()

    cursor.execute("Select * from password")
    data2 = cursor.fetchall()

    for i in data2:
        print(i)

trying()
def inserting_treeview():
    import sqlite3
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()
    cursor.execute("Select * from password")
    data1 = cursor.fetchall()

    for j in data1:
        treeview.insert(parent="", index=j[0], values=(j[0], j[1], j[2]))

    connection.commit()
    connection.close()

inserting_treeview()
def query_treeview():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Password")
    data2 = cursor.fetchall()
    global count
    count = 1
    for record in data2:
        print("[" + "'" + str(record[0]) + "'" + "," + " '" + record[1] + " '" + "," + " '" + record[2] + "'" + "],")
        count += 1 
    conn.commit()
    conn.close()
query_treeview()
# Button Definitions
def add():
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()

    addname1 = str(add_name_string.get())
    addname2 = str(add_name2_string.get())

    id = len(treeview.get_children()) + 1
    treeview.insert(parent="", index=len(treeview.get_children()) + 1, values=(len(treeview.get_children()) + 1, add_name_string.get(), add_name2_string.get()))
    
    try:

        insert_query = ("Insert into Password (Id, Website, Password) Values (?, ?, ?) ")
        cursor.execute(insert_query, (id, addname1, addname2))

        connection.commit()
        connection.close()
    except:
        print("Error")

    var1 = "*"
    print(var1*50)


def delete():
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()

    focus = treeview.focus()

    id2 = treeview.item(focus)["values"][0]
    id3 = treeview.selection()[0]

    treeview.delete(id3)  
    try:
       delete_query = "Delete from password where id = ?"


       deletion = cursor.execute(delete_query, (id2,))

       connection.commit()
    except:
        raise error

    var1 = "*"
    print(var1*50)

# Buttons in textbox_frame
add_button = Button(textbox_frame, image=add_button_image, borderwidth=0, bg="#FFF280", activebackground="#FFF280", cursor="hand2", command=add)
delete_button = Button(textbox_frame, image=delete_button_image, borderwidth=0, bg="#FFF280", activebackground="#FFF280", cursor="hand2", command=delete)


# Placing buttons in textbox_frame
add_button.place(relx=0.05, rely=0.34)
delete_button.place(relx=0.05, rely=0.495)


# Binding buttons from textbox_frame
add_button.bind("<Enter>", hover_add)
delete_button.bind("<Enter>", hover_delete)

add_button.bind("<Leave>", hover_add_leave)
delete_button.bind("<Leave>", hover_delete_leave)


# Images
name_rect = PhotoImage(file="./namerect.png")
password_rect = PhotoImage(file="./passwordrect.png")

login_button_image = PhotoImage(file="./loginbutton.png")
login_button_hover_image = PhotoImage(file="./loginbuttonhover.png")

# Hover functions 
def login_hover(e):
    login_button.configure(image=login_button_hover_image)

def login_leave(e):
    login_button.configure(image=login_button_image)

# More functions

def validate(e):
    login_name = name_string.get()
    login_password = password_string.get()
    if login_name == "J" and login_password == "69":
        swap(textbox_frame)
    else:
        print("Incorrect Creds")

def name_entry_enter(e):
    login_name = name_string.get()
    if login_name == "Name":
        Name_entry.delete(0, 50)

def password_entry_enter(e):
    login_password = password_string.get()
    if login_password == "Password":
        Password_entry.delete(0, 50)
    Password_entry.configure(show="*")

# Buttons
login_button = Button(login_frame, image=login_button_image, borderwidth=0, bg="#FFF280", 
                      activebackground="#FFF280", cursor="hand2",
                      command= validate)



# Image Labels
name_rect_label = Label(login_frame, highlightthickness=0, bg="#FFF280", image=name_rect)
password_rect_label = Label(login_frame, highlightthickness=0, bg="#FFF280", image=password_rect)

# Placing Image Labels
name_rect_label.place(relx=0.35, rely=0.35)
password_rect_label.place(relx=0.35, rely=0.47)

# Entry input strings
name_string = StringVar()
password_string = StringVar()

# Entry boxes for login
Name_entry = Entry(login_frame, bd=0, bg="#FFF280", font="poppins 18", fg="#121212", width=25, insertbackground="#121212", selectbackground="#121212", textvariable=name_string)
Password_entry = Entry(login_frame, bd=0, bg="#FFF280", font="poppins 18", fg="#121212", width=25, insertbackground="#121212", selectbackground="#121212", textvariable=password_string)

# Validity

# Label for textbox_frame
Welcome = Label(textbox_frame, text="", highlightthickness=0, font=("poppins", 25), bg="#FF6565")
Welcome.place(relx=0.05, rely=0.1)

# Placing the widgets
Login.place(relx=0.35, rely=0.1)
Name.place(relx=0.35, rely=0.3)
Password.place(relx=0.35, rely=0.42)

Name_entry.insert(0, "Name")
Password_entry.insert(0, "Password")


Name_entry.place(relx=0.357, rely=0.3605)
Password_entry.place(relx=0.357, rely=0.4805)

login_button.place(relx=0.35, rely=0.54)


# Binding buttons
login_button.bind("<Enter>", login_hover)
login_button.bind("<Leave>", login_leave)

Name_entry.bind("<Button-1>", name_entry_enter)
Password_entry.bind("<Button-1>", password_entry_enter)

Password_entry.bind("<Return>", validate)


root.mainloop()