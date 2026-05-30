from tkinter import *
root= Tk()
root.title("Student Form")
root.geometry("900x900")

def get_vals():
    print(f"Username: {u_entry.get()}")
    print(f"Password: {p_entry.get()}")

l1=Label(root, text="Username")
l1.grid(row=0, column=0)
l2= Label(root, text="Password")
l2.grid(row=1,column=0)

u_entry= StringVar()
p_entry= StringVar()

e1= Entry(root,textvariable=u_entry)
e1.grid(row=0, column=1)
e2= Entry(root, textvariable=p_entry)
e2.grid(row=1,column=1)

b= Button(root, text="Login", command=get_vals)
b.grid(row=2, column=0, columnspan=2)
root.mainloop()
