from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

def plot_graph():
    u= u_entry.get()
    a= a_entry.get()
    t= np.linspace(0,10,100)
    
    # equations
    v= u + a*t
    s= u*t + 0.5*a*t**2

    # Velocity time graph
    plt.figure(figsize=(6,4))
    plt.plot(t,v)
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.title("Velocity Time graph")
    plt.show()

    # Displacement time graph
    plt.figure(figsize=(6,4))
    plt.plot(t,s)
    plt.xlabel("Time")
    plt.ylabel("Displacement")
    plt.title("Displacement time graph")
    plt.show()

root= Tk()
root.title("Equations of Motion")
root.geometry("827x827")
label1= Label(root,text="Initial velocity(u)")
label1.grid(row=0,column=0)

label2= Label(root, text="Acceleration(a)")
label2.grid(row=1, column=0)

u_entry= IntVar()
a_entry= IntVar()

e1= Entry(root, textvariable=u_entry)
e1.grid(row=0,column=1)
e2= Entry(root, textvariable=a_entry)
e2.grid(row=1, column=1)

b= Button(root, text="Click me", command=plot_graph)
b.grid(row=2, column=0, columnspan=2)

root.mainloop()