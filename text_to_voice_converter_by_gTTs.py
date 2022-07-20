from tkinter import *
from gtts import gTTS
import os
from playsound import playsound

root = Tk()
root.geometry("900x400")
root.configure(bg='LIGHT GREEN')
root.title("TEXT TO SPEECH python UI")

top_frame = Frame(root, bg='White', width=900, height=100)
top_frame.place(x=0, y=0)

Label(top_frame, text="TEXT TO VOICE", font="arial 40 bold", bg="White", fg="black").place(x=200, y=10)


Msg = StringVar()

text_area = Text(root, font="Robote 20", bg="White", relief=GROOVE, wrap=WORD)
text_area.place(x=90, y=120, width=500, height=50)



def Text_to_speech():
    Message = text_area.get()
    speech = gTTS(text=Message)
    speech.save('Data.mp3')
    playsound('Data.mp3')


def Exit():
    root.destroy()
    os.remove('Data.mp3')


def Reset():
    Msg.set("")
    os.remove('Data.mp3')


Button(root, font='arial 15 bold',text="PLAY",width=20, command=Text_to_speech).place(x=550, y=220)
Button(root, font='arial 15 bold', text='RESET', width=20, command=Reset).place(x=550, y=340)
Button(root, font='arial 15 bold', text='EXIT', width=20, command=Exit).place(x=550, y=280)

root.mainloop()
