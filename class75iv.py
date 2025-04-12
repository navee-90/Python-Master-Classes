from tkinter import *
def submit():
    msg="Hello "+txtName.get()+"\n Email is : "+txtEmail.get()
    lblmsg=Label(root,text=msg)
    lblmsg.place(relx=0.3,rely=0.35)
def showform():
    global root, txtName,txtEmail #global access
    root=Tk()
    root.geometry("900x360")
    root.option_add("*Font","aerial 14 bold")
    lblName=Label(root,text="Enter Name: ")
    lblName.place(relx=0.05,rely=0.05)
    txtName=Entry(root)
    txtName.place(relx=0.2,rely=0.05)
    lblEmail=Label(root,text="Enter Email: ")
    lblEmail.place(relx=0.05,rely=0.15)
    txtEmail=Entry(root)
    txtEmail.place(relx=0.2,rely=0.15)
    lblSubmit=Button(root,text="submit",command=submit)
    lblSubmit.place(relx=0.3,rely=0.25)
    root.mainloop()

showform()
    