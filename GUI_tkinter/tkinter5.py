#Entry creation 
import tkinter as tk #import the tkinter library
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
#Graphical User Interface (GUI) class
#we need refernce to link to that object-root
#linked list / tree concept
root = tk.Tk() #create the main window object
root.title("My First GUI") #set the title of the window
root.geometry("400x300")#set the size of the window
tk.Label(root, text="Student Application",background="grey",fg="white",font=("Bookman old style",12),width=20,height=2,border=2).pack() #create a label widget and add it to the window
#grid method is used to place the widget in a grid layout
#fg- foreground color texr color
#font can be able to extented
label1 = tk.Label(root, text="Username:",font=("Bookman old style",12))
label1.place(x=100,y=70)#create a label widget
label2 = tk.Label(root, text="password:",font=("Bookman old style",12))
label2.place(x=100,y=90)#create a label widget
#place(100,90) x,y position of the window

def message():
    messagebox.showinfo("Information", "Submitted Successfully")
    username = entry1.get()
    password = entry2.get()
    course = entry3.get()
    messagebox.showinfo("Entered Data", f"Username: {username}\nPassword: {password}\nCourse: {course}")
def status():
    messagebox.showinfo("Information", "Cancelled Successfully")
    button2.config(text="Cancelled")
entry1 = tk.Entry(root,width=30,border=2)
entry1.place(x=200,y=75) #create an entry widget
entry2 = tk.Entry(root,width=30,border=2)
entry2.place(x=200,y=95)
button1 = tk.Button(root,text="Submit",font=("Bookman old style",12),bg="grey",fg="white",width=10,height=1,border=2,command=message)
button1.place(x=170,y=170)
button2 = tk.Button(root,text="Cancel",font=("Bookman old style",12),bg="grey",fg="white",width=10,height=1,border=2,command=status)
button2.place(x=270,y=170)
label1 = tk.Label(root, text="courses:",font=("Bookman old style",12)).place(x=100,y=110)
entry3 = tk.Entry(root,width=30,border=2).place(x=200,y=110)
courses = ["Python", "Java", "C++", "JavaScript", "Web Development"]
dropdown = ttk.Combobox(root, values=courses, width=27, state="readonly").place(x=200, y=110)
# radio button 
label4 = tk.Label(root, text="Gender:",font=("Bookman old style",12)).place(x=100,y=140)
rb1 = tk.Radiobutton(root, text="Male", value=1).place(x=200, y=140)
rb2 = tk.Radiobutton(root, text="Female", value=2).place(x=240, y=140)

root.mainloop()
