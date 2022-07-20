from tkinter import *
from tkinter import messagebox
import pyttsx3
engine = pyttsx3.init()
win = Tk()
win.title(" text to voice converter")
win.configure(bg="#305065")
win.geometry("420x200")
def speak():
    t=entry1.get()
    engine.say(t)
    engine.runAndWait()
    engine.stop()
    if(t==""):
        messagebox.showerror("Error","Please enter the text")

#Label frame
lf = LabelFrame(win,text="Text to Voice",font="30",bd=5,bg="pink")
lf.pack(fill="both",expand="yes",padx=10,pady=10)
Label(lf,text="Text",font="30",padx=15).pack(side=LEFT)
#entry----user enter the text
text=StringVar()
entry1=Entry(lf,width=25,bd=5,font="20",textvariable=text)
entry1.pack(side=LEFT,padx=10)

#button
Button(lf,text="Voice",font=15,command=speak).pack(side=LEFT)
mainloop()
