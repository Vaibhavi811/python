from tkinter import *
root= Tk()
root.title("Registration form")
root.geometry("900x600")

def getvals():
    print("Saving your response")
    with open(r"D:\python lab\record.txt","a") as f:
        f.write(f"{name.get(),phone.get(), gender.get(),emgcontact.get(),paymode.get(),food.get()}\n")

l= Label(root, text="Welcome to Harry Travels" ,bg="pink", fg="White", font="Timesnewroman 27 bold" )
l.grid(row=0, column=4)

l1= Label(root, text="Full Name",font="Timesnewroman 22 bold" )
l1.grid(row=1, column=0)
l2= Label(root, text="Phone",font="Timesnewroman 22 bold")
l2.grid(row=2,column=0)
l3= Label(root, text="Gender",font="Timesnewroman 22 bold")
l3.grid(row=3, column=0)
l4= Label(root, text="Emergency Contact",font="Timesnewroman 22 bold")
l4.grid(row=4, column=0)
l5= Label(root, text="Payment Mode",font="Timesnewroman 22 bold")
l5.grid(row=5, column=0)

name= StringVar()
phone= StringVar()
gender= StringVar()
emgcontact= StringVar()
paymode= StringVar()
food= IntVar()

e1= Entry(root, textvariable=name)
e2= Entry(root, textvariable=phone)
e3= Entry(root, textvariable=gender)
e4= Entry(root,textvariable=emgcontact)
e5= Entry(root, textvariable=paymode)

e1.grid(row=1, column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)
e5.grid(row=5,column=1)

c= Checkbutton(root, text="Want to prebook your meals?" ,font="Timesnewroman 18 italic", variable=food)
c.grid(row=6, column=4)

b= Button(root, text="Submit your response",font="Timesnewroman 22 bold" ,bg= "lightgrey", fg="White", command=getvals)
b.grid(row=7,column=4)

root.mainloop()