from tkinter import *
from tkinter import messagebox

#Setting up Main Window
root=Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

from PIL import Image, ImageTk #Python Imaging library
#adding image and labels in the main window
upload=Image.open("A.jpg")
#resize the image using resize()method
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180,y=20)

label1=Label(root,
             text="Hey user! Welcome to Denomaination Counter Application.",
             bg='light blue')
label1.place(relx=0.5,y=340,anchor=CENTER)

#funtion to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert","Do you want to calculate Denomination count?"
    )
    if MsgBox=='ok':
        topwin()

#adding buttons to main window
button1= Button(root,text="Let's get started!",
                command=msg,
                bg='brown',
                fg='white')
button1.place(x=260,y=360)

#funtion for opening new/top window
def topwin():
    top=Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")
    label=Label(top, text="Enter total amount",bg='light grey')
    entry=Entry(top)
    lbl= Label(top,text="here are number of notes for each denomination",bg='light grey')

    l1=Label(top, text="2000", bg='light grey')
    l2=Label(top, text="500", bg='light grey')
    l3=Label(top, text="100", bg='light grey')

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())#65230
            note2000 = amount//2000 #65230//2000-32
            amount%=2000 #1230
            note500=amount//500#2
            amount%=500#230
            note100=amount//100#2

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t1.insert(END,str(note500))
            t1.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("Error","Please enter a valid number")

    btn = Button(top, text='Calculate',command=calculator,bg='brown',fg='white')

    #Centering widgets in the top menu
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()
