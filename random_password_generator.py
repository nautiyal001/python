from ntpath import join
import random
import tkinter


#  Logic:-

def generate_password(len):

    validChar = "abcdefghijklmnopqrstuvwxy" \
                "" \
                "zABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()!"

    password = "".join(random.sample(validChar, len))

    display_result.delete(0, tkinter.END)
    display_result.insert(0, password)


def checkbox():
    if chk1.get() == 6:
        generate_password(6)
    elif chk2.get() == 10:
        generate_password(10)
    elif chk3.get() == 12:
        generate_password(12)
    else:
        generate_password(8)

    #  GUI Main window:-


main_window = tkinter.Tk()
main_window.title("Password Generator")

main_window.geometry('500x300')

padding = 50
main_window['padx'] = padding
main_window['pady'] = 10

# variables
chk1 = tkinter.IntVar()
chk2 = tkinter.IntVar()
chk3 = tkinter.IntVar()

# title text:-
title_text = tkinter.Label(text='Password Generator')
title_text.grid(row=0, column=0)

display_result = tkinter.Entry()
display_result.grid(row=1, column=0)

# check buttons:-

checkOne = tkinter.Checkbutton(text='6 Character', onvalue=6, offvalue=0, variable=chk1)
checkOne.grid(row=2, column=0)

checkTwo = tkinter.Checkbutton(text='10 Character', onvalue=10, offvalue=0, variable=chk2)
checkTwo.grid(row=3, column=0)

checkThree = tkinter.Checkbutton(text='12 Character', onvalue=12, offvalue=0, variable=chk3)
checkThree.grid(row=4, column=0)

# generate button:-
generate = tkinter.Button(text='Generate', command=checkbox)

generate.grid(row=6, column=0)

main_window.mainloop()