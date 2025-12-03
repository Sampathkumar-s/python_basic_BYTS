#Entry creation 
import tkinter as tk #import the tkinter library

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
entry1 = tk.Entry(root,width=30,border=2).place(x=200,y=75) #create an entry widget
entry2 = tk.Entry(root,width=30,border=2).place(x=200,y=95)

root.mainloop()