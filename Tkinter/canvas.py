from tkinter import *
root= Tk()
root.title("Canvas")
root.geometry("827x827")

c= Canvas(root, width=500, height=600)
c.pack()
c.create_line(0,0,100,200, fill="Red")
c.create_rectangle(8,27,110,90, fill="Blue")
c.create_arc(35,42,70,77,start=45,extent=90, fill="Red")
c.create_polygon(110,220,150,240,135,270, fill="Pink")
c.create_oval(200,300,250,370, fill="Brown")
c.create_text(300,400, text="I love MYself", font="comicsansms 30 italic" , fill="Orange",)


root.mainloop()